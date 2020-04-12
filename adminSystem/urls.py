from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from adminSystem import views

urlpatterns = [
    path('super/', admin.site.urls, name='super-admin'),
    url('', views.admin_page, name='admin-page'),

]
