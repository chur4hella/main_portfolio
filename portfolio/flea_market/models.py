from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=150)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Category: {self.title}'


class Region(models.Model):
    title = models.CharField(max_length=50)
    parent_region = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'City: {self.title}'


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    choices = [
        ('sell', 'Продам'),
        ('buy', 'Куплю'),
        ('exchange', 'Обмен'),
        ('service', 'Услуга'),
        ('rent', 'Аренда'),
    ]
    type_ad = models.CharField(choices=choices, max_length=15, verbose_name='Тип объявления', default=choices[0])
    short_description = models.TextField(verbose_name='Короткое описание (200 символов)', max_length=200)
    description = models.TextField(verbose_name='Описание объявления', max_length=500)
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    bargain = models.BooleanField(verbose_name='Торг', default=False)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='')
    date_update = models.DateTimeField(auto_now=True, verbose_name='')
    date_up = models.DateTimeField(default=now, verbose_name='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    city = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Город')
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title}'

class Image(models.Model):
    photo = models.ImageField(null=True, blank=True, verbose_name='Фото', upload_to='flea_market/uploads/%Y/%m/%d/')
    order_display = models.PositiveIntegerField(default=0)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, blank=True, null=True)


class Bookmark(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)