from django.urls import path

from . import views


app_name = 'flea_market'
urlpatterns = [
    path('', views.index, name='index'),
]