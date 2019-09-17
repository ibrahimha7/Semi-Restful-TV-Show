from django.db import models

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    relase_date=models.DateField()
    desc=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
