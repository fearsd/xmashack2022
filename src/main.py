import os
import tempfile
from convert import FileConverter
from flask import Flask, request, jsonify
from pdf2image import convert_from_path



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

    text = FileConverter().convert(_tmp, file_extension) # get raw text
    os.remove(_tmp)
    return jsonify({
        'text': text
    })

@app.route('/test_files')
def test_files():
    text = ""
    prefix = '../images/'
    m = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg']
    for f in m:
        _, ext = os.path.splitext(f)
        text += FileConverter().convert(prefix+f, ext)
    # with tempfile.NamedTemporaryFile(suffix='txt') as f:
    #     f.write(text)
    return text

@app.route('/pdf', methods=['POST'])
def ts():
    file = request.files['file'] # getting file from request
    filename, file_extension = os.path.splitext(file.filename) # for example: text.pdf -> text and .pdf
    _tmp = 'tmp_doc' + file_extension
    file.save(_tmp)
    text = ""
    prefix = '../images/'
    pages = convert_from_path(_tmp, 500)
    img = []
    for m, page in enumerate(pages):
        page.save(f'../images/{m}.jpg', 'JPEG')
        img.append(f'../images/{m}.jpg')
    # m = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
    for f in img:
        _, ext = os.path.splitext(f)
        text += FileConverter().convert(prefix+f, ext)
    # with tempfile.NamedTemporaryFile(suffix='txt') as f:
    #     f.write(text)
    return text

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)