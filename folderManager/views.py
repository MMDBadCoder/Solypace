from django.http import Http404
from django.shortcuts import render

# Create your views here.
from fileManager.models import SolyFile
from folderManager.models import SolyFolder


def folder_page(request, folder_id):
    folder = SolyFolder.objects.filter(id=folder_id)
    if not folder.exists():
        raise Http404
    children = SolyFolder.objects.filter(parent=folder)
    files = SolyFile.objects.filter(parent=folder)
    return render(request, 'folder-page.html', {'folder': folder, 'children': children, 'files': files})


def init(request):
    SolyFolder.objects.all().delete()
    SolyFolder.objects.create(label='Home', description='', parent=None)


def home_page(request):
    root_folder = SolyFolder.objects.filter(parent=None)
    if not root_folder.exists():
        raise Http404
    return folder_page(request, root_folder.get().id)
