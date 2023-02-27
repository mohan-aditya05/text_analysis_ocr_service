from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ocr", methods=['POST'])
def ocr():
    file_bytes = request.get_data()
    file_hash = hash(file_bytes)

    
    
    return jsonify({
        "status":True
    })