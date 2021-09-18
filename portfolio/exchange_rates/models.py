from django.db import models


class Currency(models.Model):
    cur_id = models.IntegerField()
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return '{} {}'.format(self.abbreviation, self.previousexchangerate_set.order_by('-update_date')[0])


class PreviousExchangeRate(models.Model):
    price = models.FloatField()
    count = models.IntegerField()
    update_date = models.DateTimeField(auto_now_add=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return 'price - {} for {}\nupdate date - {}'.format(self.price, self.count, self.update_date)