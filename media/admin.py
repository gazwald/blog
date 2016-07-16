from django.contrib import admin

from .models import UploadedFile


class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_add')

admin.site.register(UploadedFile, UploadedFileAdmin)
