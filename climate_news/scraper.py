from pygooglenews import GoogleNews
import time
import json
import pickle
# %%
def getNews(query, max_articles=20, time_period='1m'):
    gn = GoogleNews(lang = 'en', country = 'US')
    search = gn.search(query, when = time_period)
    search = search['entries'][:max_articles]
    rtn = {}
    for i in range(len(search)):
        rtn[i] = {'title':search[i].title,
                  'href':search[i]['links'][0]['href']}
    return rtn
# %%
def getNewsClimate(max_articles=20):
    gn = GoogleNews(lang = 'en', country = 'US')
    climate_news = gn.topic_headlines('CAAqBwgKMKeh0wEw-sE1')
    search = climate_news['entries'][:max_articles]
    rtn = {}
    for i in range(len(search)):
        rtn[i] = {'title':search[i].title,
                  'href':search[i]['links'][0]['href']}
    return rtn