from flask import Flask, render_template

app = Flask(__name__)
title = "KODLARIN SEYYAHI | SORU-CEVAP OYUNU"
@app.route('/')
def index():
    return render_template('index.html', TITLE=title)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8899, debug=1)