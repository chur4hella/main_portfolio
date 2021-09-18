from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return 'name - {}, email - {}'.format(self.name, self.email)


class Message(models.Model):
    subject = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)

    def __str__(self):
        return 'subject - {}\ntext - {}\ndate - {}'.format(self.subject, self.text, self.date)