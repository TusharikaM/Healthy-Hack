#!flask/bin/python
# import flask
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import base64
import json
# from datetime import datetime
import numpy as np
import cv2
import scipy
from keras.models import load_model
import tensorflow as tf
import subprocess

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
# CORS(app, support_credentials=True)

_score_thresh = 0.27


def init():
    global model, graph, jsonFile
    # load the pre-trained Image classification model
    print('Loading model...')
    model = load_model('../image_classification/simple_model_v2.h5')
    print('model loaded')
    graph = tf.get_default_graph()
    jsonFile = "data/foodDetails.json"

# Cross origin support


def sendResponse(responseObj):
    response = jsonify(responseObj)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    # response.headers.add('Access-Control-Allow-Headers', 'accept,content-type,Origin,X-Requested-With,Content-Type,access_token,Accept,Authorization,source')
    response.headers.add('Access-Control-Allow-Credentials', True)
    return response

# The Image classification method


def get_pred(imagePath):
    img_file = cv2.imread(imagePath)
    X = []
    y = []
    img_file = scipy.misc.imresize(arr=img_file, size=(60, 80, 3))
    img_arr = np.asarray(img_file)
    X.append(img_arr)

    X = np.asarray(X)

    X_train = np.array(X)
    X_train = X_train/255.0
    with graph.as_default():
        y_pred = model.predict(X_train)
    Y_pred_classes = np.argmax(y_pred, axis=1)

    map_characters = {1: 'coke', 2: 'doritos',
                      3: 'protein_bar', 4: 'lays', 5: 'fruit_snack'}
    prediction = map_characters.get(Y_pred_classes[0])
    print(prediction)
    return prediction

# API for classification
@app.route('/trackCalorie', methods=['POST'])
# @cross_origin(supports_credentials=True)
# @crossdomain(origin='*')
def upload_base64_img():

    content = request.get_json()
    # checking if the image is present or not.
    if 'image' not in content:
        # abort(400)
        # abort(Response('No Image data received'))
        return 'Image not received'

    imgdata = base64.b64decode(content['image'])
    filename = 'imgReceived/foodItem_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    # print("--------------------->>>>>>", filename)
    foodItem = get_pred(filename)
    # getting details of food item from the json file
    with open(jsonFile, "r") as dataFile:
        data = json.load(dataFile)
    calories_per_serving = data[foodItem]["calories"]
    totalCaloriesConsumed = data["user"]["total_calories_consumed"]
    count = data[foodItem]["count"]
    result = {
        "foodItem": foodItem,
        "calories": calories_per_serving,
        "count": count,
        "totalConsumed": totalCaloriesConsumed
    }
    # returning response to client
    return sendResponse(result)

# API for adding consumption
@app.route('/updateCount', methods=['POST'])
def increaseConsumption():
    content = request.get_json()
    foodItem = content['foodItem']
    # increase the count and calories consumption
    with open(jsonFile, "r") as dataFile:
        data = json.load(dataFile)
    data[foodItem]["count"] += 1
    data["user"]["total_calories_consumed"] += data[foodItem]["calories"]
    # Saving in json file
    with open(jsonFile, "w") as outputFile:
        json.dump(data, outputFile)
    # calling AWS to upload the json file
    subprocess.run(["aws", "s3", "cp", jsonFile, "s3://cal-count/"])
    # returning response to client
    return sendResponse({"success":"Ok"})


# if this is the main thread of execution first load the model and then start the server
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))
    init()
    app.run(threaded=True)

app.run(port=5000, debug=True)
