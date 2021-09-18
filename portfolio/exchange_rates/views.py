from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template import loader
from exchange_rates.models import *
from django.core import serializers
import json

# Create your views here.
def index(request):
    rates = {}
    for cur in Currency.objects.all():
        rates[cur.abbreviation] = {
            'rates': [i.price for i in PreviousExchangeRate.objects.filter(currency=cur).order_by('-update_date')[:30]],
            'count': PreviousExchangeRate.objects.filter(currency=cur)[0].count
        }

    currencies = {
        'currencies': Currency.objects.all(),
        'rates': json.dumps(rates),
    }
    return render(request, 'exchange_rates/index.html', context=currencies)