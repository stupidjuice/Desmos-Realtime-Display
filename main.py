import mss
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def GetLatex(left, right, top, bottom):
    return("y<" + str(top) + "\\left\\{" + str(left) + "<x<" + str(right) +"\\right\\}\\left\\{" + str(bottom) + "<y<" + str(top) + "\\right\\}")

@app.route("/RenderImage")
def RenderImage():
    pixels = []

    pixels.append(GetLatex(1,2,4,3))
    return jsonify({"pixelCount": len(pixels), "pixels": pixels})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)