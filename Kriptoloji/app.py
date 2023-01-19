from flask import Flask, render_template, redirect, request
import os
from cli import *
import time

app = Flask(__name__)
proj_name = "ROSETTA"

ALLOWED_EXTENSIONS = {'mp4', 'key'}
ERR_CODES = [400, 401, 403, 404, 500, 502, 503, 504]

def allowed_file(filename):
    return ('.' in filename) and (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', project_name=proj_name)

@app.route('/desifreleme')
def decrypt():
    return render_template('desifreleme.html', project_name=proj_name)


@app.route('/api')
def api():
    inputx = request.args.get('input')
    #complete_encryption(inputx,'static/data/'+request.remote_addr+'.mp4','static/data/'+request.remote_addr+'.key')
    if os.path.exists(request.remote_addr+'.mp4'):
        return render_template('template.html')
    else:
        return render_template('trysgain.html')

@app.route('/sifreleme')
def encrypt():
    return render_template('sifreleme.html', project_name=proj_name)

@app.route('/uploadtxt', methods=["POST"])
def uploadtxt():
    if request.method == "POST":
        metin = request.form["metin"]
        open('toEncrypt.txt', 'w+').write(metin)
        video_path, keyfile_data = complete_encryption("toEncrypt.txt", "ftest.mp4", "ftest.key")
        time.sleep(2)
    else:
        time.sleep(0.5)
        return redirect('/error')
@app.route('/upload', methods=["POST"])
def upload():   
    if request.method == "POST":
       dosya = request.files['dosya1']
       dosya2 = request.files['dosya2']
       dosya_adi = dosya.filename
       dosya_adi2 = dosya2.filename
       if allowed_file(dosya_adi):
           dosya.save('./static/data/'+dosya_adi)
       if allowed_file(dosya_adi2):
           dosya2.save('./static/data/'+dosya_adi2)
       #sonuc = complete_decryption('127.0.0.1.mp4', '127.0.0.1.key')
       os.system('python cli.py -d')
       return render_template('sonuc_desifreleme.html', project_name=proj_name)
    else:
       return redirect('/error')
    
@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567, debug=1)