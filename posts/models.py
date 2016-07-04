from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_add = models.DateTimeField('Date added', auto_now=True)
    date_pub = models.DateTimeField('Date published', null=True, blank=True)

    def __str__(self):
        return self.title
