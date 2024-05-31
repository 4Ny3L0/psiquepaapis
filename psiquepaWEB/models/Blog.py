from django.db import models
from django.db.models.functions import Now


class Blog(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    blog_image = models.CharField(max_length=300)
    creation_date = models.DateTimeField(db_default=Now())
    blog_content = models.CharField(max_length=1000)