from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.topheadlines, name='topheadlines'),
    path('top-headlines/<pg>', views.topheadlines, name='topheadlines'),
    path('top-headlines2/<con>/<cat>/<pg>', views.topheadlines2, name='topheadlines2'),
    path('search-news/<sort>/<pg>',views.searchnews,name='searchnews')
]
