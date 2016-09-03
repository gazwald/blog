from django.forms import ModelForm
from .models import UploadedFile


class UploadedFileForm(ModelForm):
    class Meta:
        model = UploadedFile
        exclude = ['owner', 'date_add']
