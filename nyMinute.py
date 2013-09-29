from __future__ import print_function
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

import os
import requests
import urllib

app = Flask(__name__)

@app.route('/')
def home():
    

    return render_template('test.html')

@app.route('/findArticles', methods= ['POST'])
def findArticles():
    timeWindow = request.form.get('time', type=int)
    topic = request.form.get('topic').replace(' ', '+')
    articles = []
    i = 0
    check = 'argument' + str(i)
    print( request.args.get('test'))
    

##Get the list of unkown size of arguments of urls to parse.
    while request.args.get(check) != None:
        articles.append(request.args.get(check))
        i = i + 1
        check = 'argument' + str(i)
        print(articles)

## iterate through articles to analyze them.
    for j in range(0,len(articles)):
        htmlDoc = requests.get(articles[j]).text
        soup = BeautifulSoup(htmlDoc)
        contentList = soup.find_all('p', {'itemprop': 'articleBody'})
        sentenceList = []
        for k in range(0, len(contentList)):
            sentenceList.append( contentList[k].get_text().split()  )
            
        
        
        #sentence list is a 2d array basically.

        print (sentenceList[0])
        ## ANALYZE THE SOUP ##





    
    

    return render_template('find.html', time = timeWindow, topic = topic)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port)

