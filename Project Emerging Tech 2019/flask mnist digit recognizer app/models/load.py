import os.path
import numpy as np
import keras.models
from keras.models import model_from_json
import tensorflow as tf


my_path = os.path.abspath(os.path.dirname(__file__))

## Compile graph from saved model
def init_model():


    json_file = open('models/digital_model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("models/digit_model.h5")
    print("Model succesfully loaded")
    
    loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    graph = tf.get_default_graph()
    
    return loaded_model,graph