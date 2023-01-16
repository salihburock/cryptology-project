#!/bin/python3 
from constants import Constants
import webview
from flask import Flask, render_template, request
from cli import complete_encryption, complete_decryption
import os

app = Flask(__name__, static_folder='gui_static', template_folder='gui_templates')

from pynput import keyboard


@app.route('/')
def ui():
    elist = open('db/maillist.csv','r').read().replace(' ','\n')
    return render_template('ui.html', elist=elist)

@app.route('/api')
def index():
    inputx = request.args.get('input')
    complete_encryption(inputx,request.remote_addr+'.mp4',request.remote_addr+'.key')
    if os.fileexist('ftest.mp4'):
        return render_template('template.html')
    else:
        return render_template('trysgain.html')

if __name__ == '__main__':
    consts = Constants()
    webview.create_window(f'{consts.title}', app, fullscreen=True)
    webview.start()
    #webview.start(debug=True)

'''if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=1)
'''
