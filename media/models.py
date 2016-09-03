from django.db import models
from django.contrib.auth.models import User


class UploadedFile(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    image = models.ImageField()
    date_add = models.DateTimeField('Date added', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_add', )
