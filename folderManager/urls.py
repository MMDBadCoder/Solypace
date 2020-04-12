from django.urls import path

from folderManager import views

urlpatterns = [
    path('<int:folder_id>/', views.folder_page, name='folder_page')
]