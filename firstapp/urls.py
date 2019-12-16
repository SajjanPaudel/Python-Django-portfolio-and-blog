from django.urls import path
from django.conf.urls import url
from .import views


app_name = 'firstapp'
urlpatterns= [
    path('',views.article_list ,name="list"),
    path('homepage/',views.homepage, name="home"),
    path('create/',views.article_create, name ="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail")
]
