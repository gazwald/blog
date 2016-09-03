from django.forms import ModelForm
from .models import Post
from django.utils.text import slugify
from random import randint


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'date_add']


    def save(self):
        instance = super(PostForm, self).save(commit=False)
        slugger = ' '.join([instance.title, str(randint(0,99))])
        instance.slug = slugify(slugger)
        instance.save()
        return instance
