from django.urls import path

from . import views


urlpatterns= [
    path('', views.add_home, name='add'),
    path('add', views.add, name='result'),

]