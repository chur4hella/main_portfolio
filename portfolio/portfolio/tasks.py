from portfolio.celery import app
from exchange_rates.models import *
import requests

@app.task
def update_currencies_info():
  request = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0')
  if request.status_code == 200:
    for currency_db in Currency.objects.all():
      for cur_nb in request.json():
        if currency_db.cur_id == cur_nb['Cur_ID']:
          currency_db.previousexchangerate_set.create(price=cur_nb['Cur_OfficialRate'], count=cur_nb['Cur_Scale'], currency=currency_db)
