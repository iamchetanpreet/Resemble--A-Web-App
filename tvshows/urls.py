from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.populartv, name='populartv'),
    path('search-tv/<pg>', views.searchtv, name='searchtv'),
    path('details-tv/<id>', views.detailstv, name='detailstv'),
    path('popular-tv/<pg>', views.populartv,name='populartv'),
    path('top-rated-tv/<pg>', views.topratedtv,name='topratedtv'),
    path('on-the-air-tv/<pg>', views.ontheairtv,name='ontheairtv'),
    path('airing-today-tv/<pg>', views.airingtodaytv,name='airingtodaytv'),
]
