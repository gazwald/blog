from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def index(request):
    category = get_object_or_404(Category, category='post')
    posts = Post.objects.order_by('-date_pub').filter(category=category)[:5]
    context = {'posts': posts}
    return render(request, 'posts/view.html', context)


def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/view.html', context)
