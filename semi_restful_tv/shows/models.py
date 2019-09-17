from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime


#This is the Vaildation
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 2:
            errors["title"] = "Title must be at least 2 characters."
        if len(postData["network"]) < 3:
            errors["network"] = "Network must be at least 3 characters."
        if len(postData["desc"]) < 10:
            errors["desc"] = "Description must be at least 10 characters."
        if len(postData["relase_date"]) > 0 and datetime.strptime(postData["relase_date"], '%Y-%M-%d') > datetime.today() :
            errors["relase_date"] = "Invalid release date."
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    relase_date=models.DateField()
    desc=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()