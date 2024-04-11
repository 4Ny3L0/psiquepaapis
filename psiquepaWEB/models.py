from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    document_id_type = models.IntegerField()
    document_id = models.CharField(max_length=15)
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    user_role = models.IntegerField(default=1)
