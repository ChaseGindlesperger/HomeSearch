from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index/', views.index, name='index'),
    path('index/search_results', views.search, name='SearchResults'),
    path('index/info/', views.info, name='info')
]
