# STEP 1 - Pip/Yarn Install the following packages:

import json, jsonschema, os, logging, requests
from flask import Flask, Blueprint, jsonify, request, Response, json


# STEP 2 - Create a Flask app:
app = Flask(__name__)


#STEP 3 - Link our JSON files and folders:
path_to_json = 'characters/'

#STEP 4 - Create our endpoints:
@app.route('/')
def index():
    return 'Welcome to our Marvel and DC Universes API!'

@app.route('/homepage')
def homepage():
    return 'Welcome to our Marvel and DC Universes API!'

#STEP 5 - Creating our Marvel Universe endpoint:
@app.route('/universe/<string:unid>', methods=['GET'])
def marvel(unid):
    if unid == "1":
        with open(path_to_json + 'marvel_characters.json') as json_file:
            data = json.load(json_file)
            marvel_cast = json.dumps(data)
        return marvel_cast, 200
    elif unid == "2":
        with open(path_to_json + 'dc_characters.json') as json_file:
            data = json.load(json_file)
            dc_cast = json.dumps(data)
        return dc_cast, 200
    else:
        return 'You are in another dimension. Go back home, you unwelcome visitor!!!', 400

@app.route('/universe/Marvel/<string:charid>', methods=['GET'])
def marvel_char(charid):
    if charid == "1":
        with open(path_to_json + 'marvel_characters.json') as json_file:
            marvelcharacter = request.json
            name = marvelcharacter['name'] == "Captain America"
        return name, 200

#STEP 6 - Fetch specific character:
@app.route('/universe/<string:unid>/characters/<string:charid>', methods=['GET'])
def say_hello_to_me(unid, charid):
    if unid == "1":
        if charid == "1":
            return jsonify({"id":"1", "name": "Captain America", "alterego": "Tony Stark", "gender": "Male", "age":32})
        elif charid == "2":
            return jsonify({"id":"2", "name": "Spiderman", "alterego": "Peter Parker", "gender": "Male", "age":18})
        elif charid == "3":
            return jsonify({"id":"3", "name": "Black Widow", "alterego": "Natasha Romanoff","gender": "Female", "age": 27})
        else:
            return "No Marvel character found", 404
    if unid == "2":
        if charid == "1":
            return jsonify({
        "id": "1",
        "name": "Batman",
        "alterego": "Bruce Wayne",
        "gender": "Male",
        "age": 35
    })
        elif charid == "2":
            return jsonify({
        "id": "2",
        "name": "Superman",
        "alterego": "Clark Kent",
        "gender": "Male",
        "age": 27
    })
        elif charid == "3":
            return jsonify({
        "id":"3",
        "name": "The Flash",
        "alterego": "Barry Allen",
        "gender": "Male",
        "age": 25
    })
        elif charid == "4":
            return jsonify({
        "id":"4",
        "name": "Wonder Woman",
        "alterego": "Diana",
        "gender": "Female",
        "age": 25
    })
        else:
            return "No Marvel character found", 404
# if __name__ == '__main__':
#     app.run(debug=True)