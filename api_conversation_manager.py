#!/usr/bin/env python
# coding: utf-8

# In[13]:


#chạy mining nhớ exclude intent
import time
import random
import numpy as np
from flask import Flask, request, jsonify
# from flask_pymongo import PyMongo
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

from intent_regconizer_activity import extract_and_get_intent
from information_extractor import extract_information
# app.config["MONGO_URI"] = "mongodb://caochanhduong:bikhungha1@ds261626.mlab.com:61626/activity?retryWrites=false"
# mongo = PyMongo(app)
def msg(code, mess=None):
    if code == 200 and mess is None:
        return jsonify({"code":200, "value": True})
    else:
        return jsonify({"code": code, "message": mess}), code



# In[14]:
@app.route('/')
def index():
    return """<h1>rLeT BOT</h1>"""

@app.errorhandler(404)
def url_error(e):
    print("---------------------")
    return msg(404, "cao chánh dương")

@app.errorhandler(500)
def server_error(e):
    return msg(500, "SERVER ERROR")



@app.route('/api/LT-conversation-manager', methods=['POST'])
def post_api():
    input_data = request.get_json(force=True)
    print(input_data)
    if "message" not in input_data.keys(): 
        return msg(400, "Message cannot be None")
    else:
        message = input_data["message"]
        result,probability=extract_and_get_intent(message)
        probability=probability.tolist()
    return jsonify({"code":200,"message":result,"probability":probability})

@app.route('/api/LT-conversation-manager/extract-information', methods=['POST'])
def post_api_extract_information():
    input_data = request.json
    print(input_data)
    if "message" not in input_data.keys(): 
        return msg(400, "Message cannot be None")
    else:
        message = input_data["message"]
        print(message)
        emails,phones,names=extract_information(message)
        print(emails)
        print(phones)
    return jsonify({"code":200,"emails":emails,"phones":phones,"names":names})

# @app.route("/api/LT-conversation-manager/messages",methods=['POST'])
# def user_profile():
#     input_data = request.json
#     print(input_data)
#     if "message" not in input_data.keys(): 
#         return msg(400, "Message cannot be None")
#     if "intent" not in input_data.keys():
#         return msg(400, "Intent cannot be None")
#     message = input_data["message"]
#     intent=input_data["intent"]
#     mongo.db.messages.insert_one({"message": message,"intent":intent})
#     return jsonify({"code":200,"message":message})

if __name__ == '__main__':
    app.run()


# In[ ]:




