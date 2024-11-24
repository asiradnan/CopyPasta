from django.db import models

class MainModel(models.Model):
    key = models.CharField(max_length=20, default="", unique=True)
    data = models.TextField(blank=True, null =True)
    file = models.FileField(null=True, blank=True)
