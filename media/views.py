from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import UploadedFile
from .forms import UploadedFileForm


@login_required
def media_list(request):
    file_list = UploadedFile.objects.order_by('-date_add')
    paginator = Paginator(file_list, 5)

    page = request.GET.get('page')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    context = {'files': files}
    return render(request, 'media/list.html', context)


@login_required
def media_view(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)
    context = {'file': file}
    return render(request, 'media/view.html', context)


@login_required
def meida_add(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media:media_list')
    else:
        form = UploadedFileForm()

    context = {'form': form}
    return render(request, 'media/add.html', context)


@login_required
def media_del(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)
    file.delete()
    context = {'file': file}
    return redirect('media:media_list')
