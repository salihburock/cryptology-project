from flask import Flask, render_template, redirect, request
import os
from cli import *
import time
bgvurl = "/static/bg.mp4" #"https://raw.githubusercontent.com/yigitoo/deniz/main/bg.mp4"
# comment line
app = Flask(__name__)
proj_name = "Rosetta’dan İnternet Çağına: Piksellerin Sonatı"

ALLOWED_EXTENSIONS = {'mp4', 'key'}
ERR_CODES = [400, 401, 403, 404, 500, 502, 503, 504]

def allowed_file(filename):
    return ('.' in filename) and (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', project_name=proj_name, bgvurl=bgvurl)

@app.route('/desifreleme')
def decrypt():
    return render_template('desifreleme.html', project_name=proj_name, bgvurl=bgvurl)


@app.route('/api')
def api():
    inputx = request.args.get('input')
    complete_encryption(inputx,'static/data/'+request.remote_addr+'.mp4','static/data/'+request.remote_addr+'.key')
    if os.path.exists(request.remote_addr+'.mp4'):
        return render_template('sifreleme_sonuc.html')
    else:
        return render_template('sifreleme.html')

@app.route('/sifreleme', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST': 
        text = request.form.get('textarea') 
        f = open('toEncrypt.txt','w+')
        f.write(text)
        print(text)
        video_path, keyfile_data = complete_encryption(data=text, outvideo="static/ftest.mp4", keyf="static/ftest.key")
        

    return render_template('sifreleme.html', project_name=proj_name, bgvurl=bgvurl)

@app.route('/sifreleme_sonuc', methods=["POST"])
def uploadtxt():
    if request.method == "POST":
        metin = request.form["metin"]
        print(metin)
        open('toEncrypt.txt', 'w+').write(metin)
        #video_path, keyfile_data = complete_encryption("toEncrypt.txt", "ftest.mp4", "ftest.key")
        time.sleep(2)
        return render_template('sifreleme_sonuc.html')
    else:
        time.sleep(0.5)
        return redirect('/error')
@app.route('/desifreleme_sonuc', methods=["POST"])
def upload(): 
    sonuc = "ROSETTA TAŞI!"
    return render_template("desifreleme_sonuc.html", sonuc=sonuc, bgvurl=bgvurl)  
    # if request.method == "POST":
    #    #dosya = request.files['dosya1']
    #    key = request.form['anahtartext']
    #    #dosya2 = request.files['dosya2']
    #    #dosya_adi = dosya.filename
    #    #dosya_adi2 = dosya2.filename
    #    #if allowed_file(dosya_adi):
    #    #    dosya.save('./static/data/'+dosya_adi)
    #    #if allowed_file(dosya_adi2):
    #    #    dosya2.save('./static/data/'+dosya_adi2)
    #    sonuc = complete_decryption('ftest.mp4','ftest.key')
    #    #os.system('python cli.py -d')
    #    return render_template('sonuc_desifreleme.html', project_name=proj_name, sonuc=sonuc)
    # else:
    #    return redirect('/error')
    
@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567, debug=1)
