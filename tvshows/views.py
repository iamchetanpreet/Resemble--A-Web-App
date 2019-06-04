from django.shortcuts import render
import tmdbsimple as tmdb
import os

tmdb.API_KEY = '964010ea624101379783b97697354c3a'
quer = None

class Tv():
    def __init__(self,id,title,poster_path):
        self.id = id
        self.title = title
        self.poster_path = poster_path

# Create your views here.
def ontheairtv(request, pg=1):
    tv1 = tmdb.TV()
    pop = tv1.on_the_air(page=pg)
    mylist = pop['results']
    tvlist= []
    for i in mylist:
        m = Tv(i['id'],i['name'],i['poster_path'])
        tvlist.append(m)
    frontend = {
     'on_the_air_tv':tvlist,
     'pages15':list(range(1,16)),
     'pages30':list(range(16,31)),
    }
    return render(request,'tvshows/tv.html',frontend)

def airingtodaytv(request, pg=1):
    tv1 = tmdb.TV()
    pop = tv1.airing_today(page=pg)
    mylist = pop['results']
    tvlist= []
    for i in mylist:
        m = Tv(i['id'],i['name'],i['poster_path'])
        tvlist.append(m)
    frontend = {
     'airing_today_tv':tvlist,
     'pages15':list(range(1,16)),
     'pages30':list(range(16,31)),
    }
    return render(request,'tvshows/tv.html',frontend)

def topratedtv(request, pg=1):
    tv1 = tmdb.TV()
    pop = tv1.top_rated(page=pg)
    mylist = pop['results']
    tvlist= []
    for i in mylist:
        m = Tv(i['id'],i['name'],i['poster_path'])
        tvlist.append(m)
    frontend = {
     'top_rated_tv':tvlist,
     'pages15':list(range(1,16)),
     'pages30':list(range(16,31)),
    }
    return render(request,'tvshows/tv.html',frontend)

def populartv(request, pg=1):
    tv1 = tmdb.TV()
    pop = tv1.popular(page=pg)
    mylist = pop['results']
    tvlist= []
    for i in mylist:
        m = Tv(i['id'],i['name'],i['poster_path'])
        tvlist.append(m)
    frontend = {
     'popular_tv':tvlist,
     'pages15':list(range(1,16)),
     'pages30':list(range(16,31)),
    }
    return render(request,'tvshows/tv.html',frontend)

def detailstv(request, id=None):

    tv = tmdb.TV(id)
    trailers = list(filter(lambda v: v['type'] == 'Trailer', tv.videos()['results']))
    teasers = list(filter(lambda v: v['type'] == 'Teaser', tv.videos()['results']))
    slist = tv.similar()['results']
    simlist = []
    for i in slist:
        t = Tv(i['id'],i['name'],i['poster_path'])
        simlist.append(t)
    rlist = tv.recommendations()['results']
    reclist = []
    for i in rlist:
        t = Tv(i['id'],i['name'],i['poster_path'])
        reclist.append(t)
    frontend = {
        "info": tv.info(),
        "year": tv.info()['first_air_date'][:4],
        "date": tv.info()['first_air_date'],
        "cast": tv.credits()['cast'][:15],
        "crew": tv.credits()['crew'][:15],
        "photos":tv.images()['backdrops'],
        "recommendtv":reclist,
        "similartv":simlist,
        "trailers": trailers,
        "teasers": teasers,
        "season_number": tv.info()['last_episode_to_air']['season_number']
        # "reviews": tv.reviews()['results'],
    }
    return render(request, "tvshows/detailstv.html", frontend)

def searchtv(request,pg=1):

    query = str(request.GET.get('query', ''))
    global quer
    if query != '':
        quer = query
        search_r = tmdb.Search().tv(query=query,page=pg)
        search_result = search_r['results']
        if search_r['total_pages'] <=10:
            totalpage = list(range(1,search_r['total_pages']+1))
        elif search_r['total_pages'] <=15:
            totalpage = list(range(1,16))
        else:
            pass
        frontend = {
            "search_tv": sorted(search_result, key=lambda x: x['popularity'], reverse=True),
            "has_tv": (search_result != []),
            "pages": totalpage,
            "queryy":quer
        }
    else:
        frontend = {
            "search_tv": [],
            "has_tv": False
        }
    return render(request,'tvshows/tv.html', frontend)
