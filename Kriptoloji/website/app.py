from flask import Flask, render_template, redirect, request

app = Flask(__name__)
proj_name = "ROSETTA"

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', project_name=proj_name)

@app.route('/decrypt')
def decrypt():
    return render_template('decrypt.hmtl', project_name=proj_name)

@app.route('/encrypt')
def encrypt():
    return render_template('decrypt.hmtl', project_name=proj_name)

@app.route('/uploadtxt', methods=["POST"])
def uploadtxt():


        return redirect('/')

        return redirect('/error')
@app.route('/upload', methods=["POST"])
def upload():

        return redirect("/")

        return redirect('/error')

@app.route('/error')
def error():
    return render_template('error.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567, debug=1)