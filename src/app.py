#!/bin/python3 
import os
from flask import Flask, render_template, request
from cli import *

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    input = request.args.get('input')
    ce(input,request.remote_addr+'.mp4',request.remote_addr+'.key')
    if os.fileexist('ftest.mp4'):
        return render_template('template.html')
    else:
        return render_template('trysgain.html')

@app.route('/ui')
def ui():
    elist = open('db/maillist.csv','r').read().replace(' ','\n')
    return render_template('ui.html', elist=elist)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081,debug=1)
