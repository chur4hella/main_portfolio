from django.shortcuts import render
from .models import Category



def index(request):
    six_categories = [i.category_set.first().category_set.first() for i in Category.objects.filter(parent_category=None).order_by('id')[: 8]]
    data = {
        'classifier': Category.objects.filter(parent_category=None).order_by('id'),
        'six_categories': six_categories,
    }
    return render(request, 'flea_market/index.html', context=data)

def ads(request):
    pass

def ad(request):
    pass

def my_ads(request):
    pass

def ads_participate(request):
    pass

def add_ad(request):
    pass

def login_registration(request):
    pass
