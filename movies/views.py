from django.shortcuts import render
import tmdbsimple as tmdb
import os

tmdb.API_KEY = '964010ea624101379783b97697354c3a'
quer = None

class Movie():
    def __init__(self,id,title,poster_path):
        self.id = id
        self.title = title
        self.poster_path = poster_path

# Create your views here.
def popularmovies(request, pg=1):
    movie1 = tmdb.Movies()
    pop = movie1.popular(page=pg)
    mylist = pop['results']
    movielist= []
    for i in mylist:
        m = Movie(i['id'],i['title'],i['poster_path'])
        movielist.append(m)
    frontend = {
     'popular_movies':movielist,
     'pages15':list(range(1,16)),
     'pages30':list(range(16,31)),
    }
    return render(request,'movies/mov.html',frontend)

def topratedmovies(request, pg=1):
    movie1 = tmdb.Movies()
    top = movie1.top_rated(page=pg)
    mylist1 = top['results']
    movielist= []

    for i in mylist1:
        m = Movie(i['id'],i['title'],i['poster_path'])
        movielist.append(m)
    frontend = {
         'top_rated_movies':movielist,
         'pages15':list(range(1,16)),
         'pages30':list(range(16,31)),
        }
    return render(request,'movies/mov.html',frontend)

def upcomingmovies(request, pg=1):
    movie1 = tmdb.Movies()
    up = movie1.upcoming(page=pg)
    mylist = up['results']
    movielist= []
    for i in mylist:
        m = Movie(i['id'],i['title'],i['poster_path'])
        movielist.append(m)
    frontend = {
         'upcoming_movies':movielist,
         'pages15':list(range(1,16)),
         'pages30':list(range(16,31)),
        }
    return render(request,'movies/mov.html',frontend)

def nowplayingmovies(request, pg=1):
    movie1 = tmdb.Movies()
    np = movie1.now_playing(page=pg)
    mylist = np['results']
    movielist= []
    for i in mylist:
        m = Movie(i['id'],i['title'],i['poster_path'])
        movielist.append(m)
    frontend = {
         'nowplaying_movies':movielist,
         'pages15':list(range(1,16)),
         'pages30':list(range(16,31)),
        }
    return render(request,'movies/mov.html',frontend)


def details(request, id=None):

    movie = tmdb.Movies(id)
    trailers = list(filter(lambda v: v['type'] == 'Trailer', movie.videos()['results']))
    teasers = list(filter(lambda v: v['type'] == 'Teaser', movie.videos()['results']))
    keywords = movie.keywords()['keywords']
    slist = movie.similar_movies()['results']
    simlist = []
    for i in slist:
        m = Movie(i['id'],i['title'],i['poster_path'])
        simlist.append(m)
    rlist = movie.recommendations()['results']
    reclist = []
    for i in rlist:
        m = Movie(i['id'],i['title'],i['poster_path'])
        reclist.append(m)
    frontend = {
        "info": movie.info(),
        "year": movie.info()['release_date'][:4],
        "date": movie.info()['release_date'],
        "cast": movie.credits()['cast'][:15],
        "crew": movie.credits()['crew'][:15],
        "photos":movie.images()['backdrops'],
        "recommend":reclist,
        "similar":simlist,
        "trailers": trailers,
        "teasers": teasers,
        "keywords": keywords,
        "reviews": movie.reviews()['results'],
        "alt": movie.alternative_titles()['titles']
    }
    return render(request, "movies/details.html", frontend)

def searchmovies(request,pg=1):

    query = str(request.GET.get('query', ''))
    global quer
    if query != '':
        quer = query
        search_r = tmdb.Search().movie(query=query,page=pg)
        search_result = search_r['results']
        if search_r['total_pages'] <=10:
            totalpage = list(range(1,search_r['total_pages']+1))
        elif search_r['total_pages'] <=15:
            totalpage = list(range(1,16))
        else:
            pass
        frontend = {
            "search_result": sorted(search_result, key=lambda x: x['popularity'], reverse=True),
            "has_result": (search_result != []),
            "pages": totalpage,
            "queryy":quer
        }
    else:
        frontend = {
            "search_result": [],
            "has_result": False
        }
    return render(request,'movies/mov.html', frontend)

def person(request, id=None):

    per = tmdb.People(id)
    frontend = {
        "info": per.info(),
        "movie": per.movie_credits()['cast'][:15],
        "tv": per.tv_credits()['cast'][:15],
        "photos":per.images()['profiles'],
    }
    return render(request, "movies/person.html", frontend)
