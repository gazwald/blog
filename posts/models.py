from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Post(models.Model):
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category, blank=True, null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date_add = models.DateTimeField('Date added', auto_now=True)
    date_pub = models.DateTimeField('Date published', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_add', )
