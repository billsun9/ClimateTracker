from flask import render_template, Flask, request
import numpy as np
from pygooglenews import GoogleNews
from scraper import getNews
from newspaper import Article
# %%
news = getNews("carbon emissions OR greenhouse gas OR co2 emissions", max_articles=20)

def extract(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return {"summary": article.summary, "keywords": article.keywords}
    except Exception as e:
        print(e)
        return {"summary": "", "keywords": []}
    # %%
l = extract(news[1]['href'])
# %%
app = Flask(__name__)

def extract(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return {"summary": article.summary, "keywords": article.keywords}
    except Exception as e:
        print(e)
        return {"summary": "", "keywords": []}
'''   
@app.route("/") # home page
def index():
    news = getNews("carbon emissions OR greenhouse gas OR co2 emissions", max_articles=20)
    curArticle = news[1]
    article_obj = extract(curArticle['href'])
    return render_template('index.html', title=curArticle['title'], link=curArticle['href'], 
                           summary=article_obj['summary'], keywords=', '.join(article_obj['keywords']))
'''

@app.route("/") # home page
def index():
    news = {'title': 'INSIGHT: Resilient energy demand may delay shift from fossil fuels - ICIS',
 'href': 'https://www.icis.com/explore/resources/news/2021/03/04/10613658/insight-resilient-energy-demand-may-delay-shift-from-fossil-fuels'}
    #news = getNews("carbon emissions OR greenhouse gas OR co2 emissions", max_articles=20)
    curArticle = news
    article_obj = extract(curArticle['href'])
    return render_template('index.html', title=curArticle['title'], link=curArticle['href'], 
                           summary=article_obj['summary'], keywords=', '.join(article_obj['keywords']))

if __name__ == '__main__':
    app.run(debug=False)
    
    # %%
from newspaper import Article
def extract(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return {"summary": article.summary, "keywords": article.keywords}
    except Exception as e:
        print(e)
        return {"summary": "", "keywords": []}
from scraper import getNews, getNewsClimate
news_ghg = getNews("greenhouse gases OR carbon emissions OR methane emissions", max_articles=6)
news_climate = getNewsClimate(max_articles=4)

title_1, title_2, title_3, title_4, title_5, title_6, title_7, title_8, title_9, title_10 = \
news_ghg[0]['title'], news_ghg[1]['title'], news_ghg[2]['title'], news_ghg[3]['title'], news_ghg[4]['title'], news_ghg[5]['title'], \
news_climate[0]['title'], news_climate[1]['title'], news_climate[2]['title'], news_climate[3]['title']

href_1, href_2, href_3, href_4, href_5, href_6, href_7, href_8, href_9, href_10 = \
news_ghg[0]['href'], news_ghg[1]['href'], news_ghg[2]['href'], news_ghg[3]['href'], news_ghg[4]['href'], news_ghg[5]['href'], \
news_climate[0]['href'], news_climate[1]['href'], news_climate[2]['href'], news_climate[3]['href']

nlp_1, nlp_2, nlp_3, nlp_4, nlp_5, nlp_6, nlp_7, nlp_8, nlp_9, nlp_10 = \
extract(href_1), extract(href_2), extract(href_3), extract(href_4), extract(href_5), extract(href_6), extract(href_7), extract(href_8), extract(href_9), extract(href_10)

sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9, sum_10 = \
nlp_1['summary'], nlp_2['summary'], nlp_3['summary'], nlp_4['summary'], nlp_5['summary'], nlp_6['summary'], nlp_7['summary'], nlp_8['summary'], nlp_9['summary'], nlp_10['summary']

keywords_1, keywords_2, keywords_3, keywords_4, keywords_5, keywords_6, keywords_7, keywords_8, keywords_9, keywords_10 = \
nlp_1['keywords'], nlp_2['keywords'], nlp_3['keywords'], nlp_4['keywords'], nlp_5['keywords'], nlp_6['keywords'], nlp_7['keywords'], nlp_8['keywords'], nlp_9['keywords'], nlp_10['keywords']

# %%
keywords_1=', '.join(keywords_1)
keywords_2=', '.(keywords_2)
keywords_3=', '.(keywords_3)
keywords_4=', '.(keywords_4)
keywords_5=', '.(keywords_5)
keywords_6=', '.(keywords_6)
keywords_7=', '.(keywords_7)
keywords_8=', '.(keywords_8)
keywords_9=', '.(keywords_9), keywords_10=', '.(keywords_10)