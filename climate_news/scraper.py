from pygooglenews import GoogleNews
import time
import json
import pickle

def getNews(query, max_articles=20, time_period='1m'):
    gn = GoogleNews()
    search = gn.search(query, when = time_period)
    search = search['entries'][:max_articles]
    rtn = {}
    for i in range(len(search)):
        rtn[i] = {'title':search[i].title,
                  'href':search[i]['links'][0]['href']}
    return rtn
# %%

tmp = getNews("climate change", max_articles=20)
# %%
tmp2 = getNews("carbon emissions OR greenhouse gas OR co2 emissions", max_articles=20)
# %%
# climate_news = gn.topic_headlines('CAAqBwgKMKeh0wEw-sE1')
tmp3 = getNews("microsoft OR MSFT", max_articles=20)