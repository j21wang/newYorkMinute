from __future__ import print_function
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

import os

app = Flask(__name__)

@app.route('/')
def home():
    

    return render_template('test.html')

@app.route('/findArticles', methods= ['POST'])
def findArticles():
    timeWindow = int(request.form.get('time'))
    topic = request.form.get('topic').replace(' ', '+')

    return render_template('find.html', time = timeWindow, topic = topic)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port)

