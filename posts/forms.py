from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'date_add']


    def save(self):
        instance = super(PostForm, self).save(commit=False)
        slugger = ' '.join(instance.id, instance.title)
        instance.slug = slugify(slugger)
        instance.save()
        return instance
