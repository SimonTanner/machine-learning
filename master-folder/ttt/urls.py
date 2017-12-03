from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newgame/', views.play_game, name = 'play_game'),
]
