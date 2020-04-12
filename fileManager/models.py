from django.db import models
from folderManager.models import SolyFolder
from instanceManager.models import Instance


class SolyFile(Instance):
    url = models.CharField(max_length=200, blank=False, null=False)


class SuggestedFile(models.Model):
    file = models.FileField(upload_to='suggested_files/', blank=True)
    description = models.CharField(max_length=1000, blank=False, null=False, default='[]')
    author_name = models.CharField(max_length=50, blank=True, default='')
    author_email = models.CharField(max_length=50, blank=True, default='')
