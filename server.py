import os

from pathlib import Path
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def home_page():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(
            basepath, 'images/', f.filename)
        f.save(upload_path)
        return

    

if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
