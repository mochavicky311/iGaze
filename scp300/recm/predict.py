from flask import request, render_template, redirect, url_for
from flask import jsonify
import base64
import numpy as np
import io
from PIL import Image
import tensorflow as tf 
from keras.preprocessing.image import img_to_array
import cv2 

session = tf.Session()
tf.keras.backend.set_session(session)

#create model 
global model
model = tf.keras.models.load_model("scp300/static/recm/cnn_modelv2.h5") 
global graph
graph = tf.get_default_graph()


# preprocess image  
def preprocess_image(image):
    print('processing image...')
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image = cv2.resize(image,(128,128))
    image = image.astype("float")/255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

# function to perform prediction
def predict_face_shape():
    image = cv2.imread( 'scp300/static/recm/save/face.jpg')
    processed_image = preprocess_image(image)
    
    with session.as_default():
        with graph.as_default():
            prediction = model.predict(processed_image)
    
    index = np.argmax(prediction)
    if index == 0:
        label = 'heart'
    elif index == 1:
        label = 'round'      
    else:
        label = 'square'

    return label 
       