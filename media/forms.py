from django.forms import ModelForm
from .models import UploadedFile


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['date_add']
