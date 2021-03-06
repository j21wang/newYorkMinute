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

@app.route('/runTest', methods= ['GET'])
def derp():
    return render_template('debug.html')

@app.route('/findArticles', methods= ['POST'])
def findArticles():
    timeWindow = request.form.get('time', type=int)
    #topic = request.form.get('topic').replace(' ', '+')
    articles = []
    articlesValid = []
    i = 0
    check = 'url_' + str(i)

##Get the list of unkown size of arguments of urls to parse.
    while request.args.get(check) != None:
        articles.append(request.args.get(check))
        i = i + 1
        check = 'url_' + str(i)

## iterate through articles to analyze them.
    totalLow = 0
    totalHigh = 0
    articleLow = []
    articleHigh = []
    articleLS = []
    articleHS = []
    for j in range(0,len(articles)):
        parser_response = parser_client.get_article_content(articles[j])


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
            for l in range(0, len(sentenceList[k])):
                if sentenceList[k][l] in stopWords:
                    stopCount = stopCount + 1
        sum =  stopCount + totalCount

        high = sum/250
        low = sum/300

        highSec = int(((float(sum)/250) - high)*60)
        lowSec  = int(((float(sum)/300) - low)*60)
        totalHigh = totalHigh + float(sum)/250
        totalLow = totalLow + float(sum)/300
        if totalLow - timeWindow < 1 :
            articlesValid.append(j)
            articleLow.append(low)
            articleHigh.append(high)
            articleLS.append(highSec)
            articleHS.append(lowSec)

            print(articleLS)
        else :
            totalHigh = totalHigh - float(sum)/250
            totalLow = totalLow - float(sum)/300
            
    validArticleList=[]
    for j in range(0, len(articlesValid) ):
        validArticleList.append(articles[articlesValid[j]])

    print(validArticleList)

    ##Get titles##
    articleLinks = []

    for j in range(0, len(validArticleList)):
        articleLink = {}
        parser_response = parser_client.get_article_content(validArticleList[j])
        articleLink = {
                'title' : parser_response.content['title'].replace('\n', ' '),
                'author' : parser_response.content['author'],
                'link' : validArticleList[j],
                'lowM' : articleLow[j],
                'lowS' : articleLS[j],
                'highS': articleHS[j],
                'highM': articleHigh[j]
        }
        
        articleLinks.append(articleLink)

    print(articleLinks)

    return render_template('find.html', 
            time = timeWindow, 
            lowerBound = "%.2f" %totalLow, 
            upperBound = "%.2f"%totalHigh, 
            finalArticlesList = articleLinks
           ) 
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port)

