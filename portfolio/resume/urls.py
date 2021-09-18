from django.urls import path

from . import views


app_name = 'resume'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('works', views.works, name='works'),
    path('contact', views.contact, name='contact'),
]