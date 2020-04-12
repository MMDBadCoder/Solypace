import json

from django.shortcuts import render, redirect

from fileManager.forms import SuggestedFileForm


def add_new_file(request):
    success = False
    error_text = None
    if request.POST:
        post = request.POST.copy()
        description = ' '.join([post.get('tag' + str(i)) for i in range(3)])

        post['description'] = description

        form = SuggestedFileForm(post, request.FILES)
        if form.is_valid():
            form.save()
            success = True
        else:
            error_list = [str(error) for error in form.errors.get('__all__')]
            error_text = ''.join(error_list)

    return render(request, 'add-new-file.html', {'success': success, 'error': error_text})
