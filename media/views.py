from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from .models import UploadedFile
from .forms import UploadedFileForm


@login_required
def media_list(request):
    file_list = cache.get_or_set('file_list', UploadedFile.objects.all())
    paginator = Paginator(file_list, 5)

    page = request.GET.get('page')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    context = {'files': files,
               'form': UploadedFileForm()}

    return render(request, 'media/view.html', context)


@login_required
def media_add(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_upload = form.save(commit=False)
            new_upload = request.user
            new_upload.save()

    return redirect('media:media_list')


@login_required
def media_del(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)
    file.delete()
    return redirect('media:media_list')
