from django.db import models
from django.db.models.functions import Now


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=35)
    document_id_type = models.IntegerField()
    document_id = models.CharField(max_length=15, blank=False, primary_key=True)
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=250)
    user_role = models.IntegerField(default=1)
    email = models.EmailField(null=True, blank=True)
    mobile_number = models.CharField(max_length=12, default='Not number provided')
    registration_date = models.DateTimeField(db_default=Now())


class Blog(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    document_id = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE, null=True)
    blog_image = models.CharField(max_length=300)
    creation_date = models.DateTimeField(db_default=Now())
    blog_content = models.CharField(max_length=4500)

