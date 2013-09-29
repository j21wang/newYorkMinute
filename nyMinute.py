from __future__ import print_function
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from readability import ParserClient
parser_client = ParserClient('0b1c20f4e39f43ce74f477815c956088ec63ded5')

import os
import requests
import urllib

app = Flask(__name__)
stopWords = {}
with open('static/stop.txt') as stop:
    for line in stop:

        current = line.split()
        stopWords[current[0]] = current[0]


@app.route('/')
def home():
    

    return render_template('test.html')

@app.route('/findArticles', methods= ['POST'])
def findArticles():
    timeWindow = request.form.get('time', type=int)
    topic = request.form.get('topic').replace(' ', '+')
    articles = []
    articlesTime = []
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
        parser_response = parser_client.get_article_content(articles[j])

        print( type(parser_response.content['content']) )


        #htmlDoc = requests.get(articles[j]).text
        soup = BeautifulSoup(parser_response.content['content'])
        contentList = soup.find_all('p')
        sentenceList = []
        for k in range(0, len(contentList)):
            sentenceList.append( contentList[k].get_text().split()  )
        
        
        
        #sentence list is a 2d array basically.

        ## ANALYZE THE SOUP ##
        stopCount = 0
        totalCount = 0
        for k in range(0, len(sentenceList)):
            totalCount = totalCount + len(sentenceList[k])
            print(sentenceList[k])
            for l in range(0, len(sentenceList[k])):
                if sentenceList[k][l] in stopWords:
                    stopCount = stopCount + 1

        sum =  stopCount + totalCount
        metric = float(sum)/250

        print(metric)
    return render_template('find.html', time = timeWindow, topic = topic)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port)

