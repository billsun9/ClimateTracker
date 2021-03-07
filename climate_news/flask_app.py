from flask import render_template, Flask, request
import numpy as np
from pygooglenews import GoogleNews
from scraper import getNews, getNewsClimate
from newspaper import Article

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
    
@app.route("/") # home page
def index():
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
    
    return render_template('index.html', 
                           title_1=title_1, title_2=title_2, title_3=title_3, title_4=title_4, title_5=title_5, title_6=title_6, title_7=title_7, title_8=title_8, title_9=title_9, title_10=title_10, 
                           href_1=href_1, href_2=href_2, href_3=href_3, href_4=href_4, href_5=href_5, href_6=href_6, href_7=href_7, href_8=href_8, href_9=href_9, href_10=href_10, 
                           sum_1=sum_1, sum_2=sum_2, sum_3=sum_3, sum_4=sum_4, sum_5=sum_5, sum_6=sum_6, sum_7=sum_7, sum_8=sum_8, sum_9=sum_9, sum_10=sum_10,
                           keywords_1=', '.join(keywords_1), keywords_2=', '.join(keywords_2), keywords_3=', '.join(keywords_3), keywords_4=', '.join(keywords_4), keywords_5=', '.join(keywords_5), keywords_6=', '.join(keywords_6), keywords_7=', '.join(keywords_7), keywords_8=', '.join(keywords_8), keywords_9=', '.join(keywords_9), keywords_10=', '.join(keywords_10))
if __name__ == '__main__':
    app.run(debug=True)