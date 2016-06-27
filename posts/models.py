from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_add = models.DateTimeField('Date added', auto_now=True)
    date_pub = models.DateTimeField('Date published', null=True, blank=True)
