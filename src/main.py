import os
import tempfile
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'mmm is ok'

@app.route('/file', methods=['POST'])
def get_file():
    file = request.files['file'] # getting file from request
    filename, file_extension = os.path.splitext(file.filename) # for example: text.pdf -> text and .pdf
    _tmp = 'tmp_doc' + file_extension
    file.save(_tmp)

    os.remove(_tmp)
    return jsonify({
        'orig': filename,
        'tmp': _tmp
    })
