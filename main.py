import cv2
import numpy as np
from PIL import Image
from mss import mss
from flask import Flask, jsonify, request
from flask_cors import CORS

MONITOR_WIDTH = 2560 #set to your monitor resolution
MONITOR_HEIGHT = 1440

RESIZE_WIDTH = 32 #set to the resoultion you want in desmos (dont set this too high!!!!)
RESIZE_HEIGHT = 18

GRAPH_SCALE = 0.5 #resizes the graph because for some reason zooming out too much makes the pixels go woowoooowoowoooo

app = Flask(__name__)
CORS(app)

def GetLatex(left, right, top, bottom):
    return("y<" + str(top) + "\\left\\{" + str(left) + "<x<" + str(right) +"\\right\\}\\left\\{" + str(bottom) + "<y<" + str(top) + "\\right\\}")

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
            currentHex = "#"
            for rgb in list(y):
                if(rgb < 16):
                    currentHex += "0" + hex(rgb)[2:]
                else:
                    currentHex += hex(rgb)[2:]
                
            screenshotHex.append(currentHex[:-2])
            pixels.append(GetLatex(yb, yb+1, xb+1, xb))

    print(screenshotHex)
    return jsonify({"pixelCount": len(pixels), "pixels": pixels, "colors": screenshotHex, "w": RESIZE_WIDTH, "h": RESIZE_HEIGHT, "scale": GRAPH_SCALE})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)