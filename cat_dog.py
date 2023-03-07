from tensorflow import keras
import pandas as pd 
import numpy as np
import os
import cv2

# MODEL LOAD
model_path = 'my_transferlearning_model.h5'
model = keras.models.load_model(model_path)

model.trainable = False

def path_to_img(path):
    path = "static/uploads/" + path
    path = os.path.join(os.getcwd(), path)
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (160, 160))
    return img


def predict_cat_or_dog(image_path):
    image = path_to_img(image_path)

    # EXPANDING DIMENTION TO (1,160,160,3)
    image = np.expand_dims(image, (0,))
    image = model.predict_step(image)

    pred = keras.activations.sigmoid(image)
    
    if pred < 0.5 :
        return 'cat'
    else :
        return 'dog'

# Testing

# print(os.getcwd())
# name = 'DOGFF.jpg'
# img = predict_cat_or_dog(name)

# print('\n', type(img),'\n')

