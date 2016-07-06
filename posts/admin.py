from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_pub')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
