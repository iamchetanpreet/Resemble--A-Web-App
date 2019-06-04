from django.shortcuts import render
from newsapi import NewsApiClient
import pycountry
# Create your views here.
api = NewsApiClient(api_key='f932fef5da824b70821f481834712853')
# top_headlines = api.get_top_headlines(language='en')['articles']
# print(top_headlines)
# top=api.get_everything(q='modi',sort_by='relevancy',page=1,language='en')
#
# print(top)
class News():
    def __init__(self,id,sname,author,title,imageurl,date,time):
        self.id = id
        self.sname = sname
        self.author = author
        self.title = title
        self.imageurl = imageurl
        self.date = date
        self.time = time

countries=['ae','ar','at','au','be','bg','br','ca','ch','cn','co','cu','cz','de','eg',
'fr','gb','gr','hk','hu','id','ie','il','in','it','jp','kr','lt','lv','ma','mx','my','ng','nl','no','nz',
'ph','pl','pt','ro','rs','ru','sa','se','sg','si','sk','th','tr','tw','ua','us'
]
COUNTRY=False
CATEGORY =False
quer = None

categories = ['business','entertainment','general','health','science','sports','technology']

def topheadlines(request,pg=1):
    top = api.get_top_headlines(language='en',page=int(pg))
    mylist = top['articles']
    global countries
    global categories
    newslist= []
    for i in mylist:
        dt = i['publishedAt']
        date = dt[0:9]
        time = dt[11:18]
        m = News(i['source']['id'],i['source']['name'],i['author'],i['title'],i['urlToImage'],date,time)
        newslist.append(m)
    frontend = {
     'topnews':newslist,
     'countries':countries,
     'categories':categories,
     'pages15':list(range(1,16)),
     'pages30':list(range(16,31)),
    }
    return render(request,'news/news.html',frontend)

def topheadlines2(request,con='us',cat='general',pg=1):
    top = api.get_top_headlines(language='en',country=str(con),category=str(cat),page=int(pg))
    mylist = top['articles']
    newslist= []
    global countries
    global categories
    global COUNTRY
    COUNTRY=str(con)
    global CATEGORY
    CATEGORY=str(cat)
    for i in mylist:
        dt = i['publishedAt']
        date = dt[0:9]
        time = dt[11:18]
        m = News(i['source']['id'],i['source']['name'],i['author'],i['title'],i['urlToImage'],date,time)
        newslist.append(m)
    frontend = {
     'topnews':newslist,
     'countries':countries,
     'country':COUNTRY,
     'categories':categories,
     'category':CATEGORY,
     'pages15':list(range(1,16)),
     'pages30':list(range(16,31)),
    }
    return render(request,'news/news.html',frontend)

def searchnews(request,sort='relevancy',pg=1):

    query = str(request.GET.get('query', ''))
    global quer
    if query != '':
        quer = query
        every = api.get_everything(q=query,language='en',sort_by=sort,page=int(pg))
        mylist = every['articles']
        newslist= []
        for i in mylist:
            dt = i['publishedAt']
            date = dt[0:9]
            time = dt[11:18]
            m = News(i['source']['id'],i['source']['name'],i['author'],i['title'],i['urlToImage'],date,time)
            newslist.append(m)
        frontend = {
         'search_news':newslist,
         'has_news':(newslist != []),
         "pages": 1,
         "queryy":quer
        }
    else:
        frontend = {
            "search_news": [],
            "has_search": False
        }
    return render(request,'news/news.html',frontend)




# api.get_sources()
