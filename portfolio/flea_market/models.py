from django.db import models
from django.utils.timezone import now


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
    title = models.CharField(max_length=100)
    type_ad = models.CharField(max_length=15)
    description = models.TextField()
    # photo = models.ImageField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_up = models.DateTimeField(default=now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(Region, on_delete=models.CASCADE)
    # user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title}'

