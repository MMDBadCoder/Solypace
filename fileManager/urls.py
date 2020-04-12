from django.conf.urls import url
from fileManager import views

urlpatterns = [
    url('add-new/', views.add_new_file, name='add-new-file')
]
