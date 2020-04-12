from django.shortcuts import render

from fileManager.models import SuggestedFile


def admin_page(request):
    suggested_docs = SuggestedFile.objects.all()
    return render(request, 'admin-page.html', {
        'suggested_docs': suggested_docs,
    })
