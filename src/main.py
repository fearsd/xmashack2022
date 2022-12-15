import os
import tempfile
from flask import Flask, request, jsonify
from convert import FileConverter

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'mmm is ok'

@app.route('/file', methods=['POST'])
def get_file():
    file = request.files['file'] # getting file from request
    _, file_extension = os.path.splitext(file.filename) # for example: text.pdf -> text and .pdf
    _tmp = 'tmp_doc' + file_extension
    file.save(_tmp)

    text = FileConverter().convert(_tmp, file_extension) # get raw text
    os.remove(_tmp)
    return jsonify({
        'text': text
    })

@app.route('/test_files')
def test_files():
    text = ""
    prefix = '../files/'
    for f in os.listdir(prefix):
        _, ext = os.path.splitext(f)
        text += FileConverter().convert(prefix+f, ext)
    return text

