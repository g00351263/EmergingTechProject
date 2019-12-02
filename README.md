Keras Flask Mnist Data App (Handwritten Digits Recognizer)

Student Name: Raja Naseer Ahmed Khan (G00351263) 
 
 
Contents: 
 
1. Project Emerging Tech 2019 Folder (contains project) (NOTE: Project has file name requirements.txt, use this to install dependencies using command line: pip install -r requirements.txt)  
 
2. Class Tutorial Folder (contains class video files) 3. Readme file (details how to run project) 4. Research file (with details of all links researched) 5. Mnist jupyter folder, contains notebook code of training and checking the mnist data. 
 
 
Very important Before you run any file: 
 
. TensorFlow and SciPy version were not stable hence, old version is used. Please use following commands example in case dependencies conflict. Use uninstall and install for any of them. 
 
TensorFlow Details: . To uninstall TensorFlow:  pip uninstall TensorFlow  To install old version use: pip install TensorFlow==1.13.1 
 
SciPy Details: . To uninstall SciPy:  pip uninstall SciPy  To install old version use: pip install SciPy==1.2 
 
 
How to Train Model MNIST: 
 
FROM COMMAND PROMPT: run the file with command (python train.py) from directory \model. This will create the json and h5 files. ------------------------------------------------------------------------------------------------------------------------------------ FROM COMMAND JUPYTER NOTEBOOK: Go to the project folder Project Emerging Tech 2019 and type command jupyter notebook. This will start the jupyter notebook in browser. Click on model directory and click on train.ipynb file. In the cell press shift Enter to run the file. 
 
 
How to Run Flask and Python App: 
 
 
FROM COMMAND PROMPT: Folder of Project : Project Emerging Tech 2019\flask mnist digit recognizer app/app.py run the file with command (python app.py) from directory root. This will start the server and the link to https://localhost:5000 can be copy pasted in browser to see the app. ------------------------------------------------------------------------------------------------------------------------------------ 
 
FROM COMMAND JUPYTER NOTEBOOK: Project required several modules to run together hence not possible to use Jupyter Notebook
