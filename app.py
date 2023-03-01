from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request
import logging
from doc_preprocess import DocumentPreprocess

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ocr", methods=['POST'])
def ocr():
    file_bytes = request.files.get('file').read()

    doc_proc_obj = DocumentPreprocess(file_bytes)
    res = doc_proc_obj.process_document()
    
    return jsonify({
        "status": True,
        'text': res
    })

if __name__ == '__main__':
    app.run(host="localhost", port=5002, debug=True)