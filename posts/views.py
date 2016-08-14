from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    return render(request, 'posts/view.html', context)


def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/view.html', context)


@login_required
def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm(initial={'date_pub': timezone.now()})

    context = {'form': form}
    return render(request, 'posts/add.html', context)
