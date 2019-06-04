from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.popularmovies, name='popularmovies'),
    path('search-movies/<pg>', views.searchmovies, name='searchmovies'),
    path('details/<id>', views.details, name='details'),
    path('person/<id>', views.person, name='person'),
    path('popular-movies/<pg>', views.popularmovies,name='popularmovies'),
    path('top-rated-movies/<pg>', views.topratedmovies,name='topratedmovies'),
    path('upcoming-movies/<pg>', views.upcomingmovies,name='upcomingmovies'),
    path('now-playing-movies/<pg>', views.nowplayingmovies,name='nowplayingmovies'),
]
