from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('index',views.index,name="index"),

    path('form',views.form,name="form"),
    path('reg',views.reg,name='reg'),

    path('review',views.review,name="review"),
    path('rev',views.rev,name='rev'),


    path('reviews', views.reviews, name='reviews'),

path('index', views.index, name='index'),

]
