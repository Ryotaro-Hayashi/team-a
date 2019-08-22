import os
import random
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
#from werkzeug import secure_filename

app = Flask(__name__)
app.config['DEBUG'] = True

ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'JPG'])
UPLOAD_FOLDER = './images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# http://127.0.0.1:5000をルートとして、("")の中でアクセスポイント指定
# @app.route("hoge")などで指定すると、http://127.0.0.1:5000/hogeでの動作を記述できる。
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def result():
 if request.method == 'POST':
        img_file = request.files['image']
        if img_file and allowed_file(img_file.filename):
            #filename = secure_filename(img_file.filename)
            filename="result.jpg"
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return render_template('result.html', filename=filename)
        else:
            return ''' <p>許可されていない拡張子です</p> '''
 else:
        return render_template("index.html")



if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()
