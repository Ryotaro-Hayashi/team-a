import os
import random
from flask import Flask, render_template, request, redirect



app = Flask(__name__)
app.config['DEBUG'] = True

ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'JPG'])
UPLOAD_FOLDER = './static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/upload', methods=['GET','POST'])
def result():

 if request.method == 'POST':
        img_file = request.files['image']
        if img_file:
            filename="result.jpg"
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            return  render_template('result.html',path=path)
        else:
            return ''' <p>許可されていない拡張子です</p> '''
 else:
        return render_template("index.html")



if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()
