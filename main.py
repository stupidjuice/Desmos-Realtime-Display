import cv2
import numpy as np
from PIL import Image
from mss import mss
from flask import Flask, jsonify, request
from flask_cors import CORS

MONITOR_WIDTH = 2560 #set to your monitor resolution
MONITOR_HEIGHT = 1440

RESIZE_WIDTH = 16 #set to the resoultion you want in desmos (dont set this too high!!!!)
RESIZE_HEIGHT = 9   

GRAPH_SCALE = 0.5 #resizes the graph because for some reason zooming out too much makes the pixels go woowoooowoowoooo

app = Flask(__name__)
CORS(app)

def GetLatex(left, right, top, bottom):
    #return("y<" + str(top) + "\\left\\{" + str(left) + "<x<" + str(right) +"\\right\\}\\left\\{" + str(bottom) + "<y<" + str(top) + "\\right\\}")
    return "\\operatorname{polygon}((" + str(left) + "," + str(top) + "), (" + str(left) + "," + str(bottom) + "), (" + str(right) + "," + str(bottom) + "), (" + str(right) + "," + str(top) + "))"

@app.route("/RenderImage")
def RenderImage():
    print("a")
    sct = mss()
    pixels = []

    screenshot = sct.grab({'top': 0, 'left': 0, 'width': MONITOR_WIDTH, 'height': MONITOR_HEIGHT})
    screenshot_resized = np.array(Image.fromarray(np.array(screenshot)).resize((RESIZE_WIDTH, RESIZE_HEIGHT)))

    screenshotHex = []
    xb=0
    for x in screenshot_resized:
        xb += 1
        yb = 0
        for y in x:
            yb += 1
            currentHex = ""

            listy = list(y)
            for i in range(len(listy)):
                if(listy[3-i] < 16):
                    currentHex += "0" + hex(listy[3-i])[2:]
                else:
                    currentHex += hex(listy[3-i])[2:]
                
            screenshotHex.append("#" + currentHex[2:])
            pixels.append(GetLatex(yb, yb+1, xb+1, xb))

            print(str(y) + currentHex)
    return jsonify({"pixelCount": len(pixels), "pixels": pixels, "colors": screenshotHex, "w": RESIZE_WIDTH, "h": RESIZE_HEIGHT, "scale": GRAPH_SCALE})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)