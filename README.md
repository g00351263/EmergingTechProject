# Project Title

Handwritten Digits Recognizer Flask,Keras,TensorFlow App

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Very important Before you run any file: 
 
. TensorFlow and SciPy version were not stable hence, old version is used. Please use following commands example in case dependencies conflict. Use uninstall and install for any of them. 
 
TensorFlow Details: . To uninstall TensorFlow:  pip uninstall TensorFlow  To install old version use: pip install TensorFlow==1.13.1 
 
SciPy Details: . To uninstall SciPy:  pip uninstall SciPy  To install old version use: pip install SciPy==1.2 
```

### Installing

1. Project Emerging Tech 2019 Folder (contains project) (NOTE: Project has file name requirements.txt, use this to install dependencies using command line: pip install -r requirements.txt)  

```
## Running the tests

How to Train Model MNIST: 
 
FROM COMMAND PROMPT: run the file with command (python train.py) from directory \model. This will create the json and h5 files. ------------------------------------------------------------------------------------------------------------------------------------ FROM COMMAND JUPYTER NOTEBOOK: Go to the project folder Project Emerging Tech 2019 and type command jupyter notebook. This will start the jupyter notebook in browser. Click on model directory and click on train.ipynb file. In the cell press shift Enter to run the file. 
 
 
How to Run Flask and Python App: 
 
 
FROM COMMAND PROMPT: Folder of Project : Project Emerging Tech 2019\flask mnist digit recognizer app/app.py run the file with command (python app.py) from directory root. This will start the server and the link to https://localhost:5000 can be copy pasted in browser to see the app. ------------------------------------------------------------------------------------------------------------------------------------ 
 
FROM COMMAND JUPYTER NOTEBOOK: Project required several modules to run together hence not possible to use Jupyter Notebook
