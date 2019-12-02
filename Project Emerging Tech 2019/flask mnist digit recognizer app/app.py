## App Utilities
import os
from flask import Flask, render_template,request
from scipy.misc import imread, imresize
import numpy as np
import base64
import re
import sys

sys.path.append(os.path.abspath("./models"))
from load import *



app = Flask(__name__)
global model, graph
model, graph = init_model()

@app.route('/')
def dashboard():
    """Homepage View"""

    return render_template("index.html")

## Image Converter from str to b64
def convertImage(imgData1):
    imgstr = re.search(b'base64,(.*)', imgData1).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    imgData = request.get_data()

    ## transform
    convertImage(imgData)
    x = imread('output.png', mode='L')
    x = np.invert(x)
    x = imresize(x, (28, 28))
    x = x.reshape(1, 28, 28, 1)
    ## predict
    with graph.as_default():
        out = model.predict(x)
        print(np.argmax(out, axis=1))
        response = np.array_str(np.argmax(out, axis=1))
        response = ' '.join(map(str, response))
        response = response.replace('[', '')
        response = response.replace(']', '')
        return response


## APP INITIATION
if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)