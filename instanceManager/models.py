from django.db import models


# Create your models here.


class Instance(models.Model):
    parent = models.ForeignKey('Instance', on_delete=models.CASCADE, null=True, default=None)
    label = models.CharField(max_length=100, blank=False, null=False, default='No label yet')
    description = models.CharField(max_length=1000, blank=True, null=False, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
