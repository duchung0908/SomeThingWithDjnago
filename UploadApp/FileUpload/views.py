from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from UploadApp.settings import MAX_FILE_SIZE
from .forms import FileUploadForm


def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FileUploadForm()
        else:
            return JsonResponse({'error': "File is invalid"})
    form = FileUploadForm()
    return render(request, 'uploadfile.html', {'form': form})