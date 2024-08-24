import uuid

from django.db import models
from django.db.models.functions import Now


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=35)
    document_id = models.CharField(max_length=15, blank=False)
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=250)
    role_type = models.IntegerField(default=1)
    email = models.EmailField(null=True, blank=True)
    mobile_number = models.CharField(max_length=12, default='Not number provided')
    registration_date = models.DateTimeField(db_default=Now(), editable=False)
    last_updated = models.DateTimeField(db_default=Now())
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    psid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


class Blog(models.Model):
    title = models.CharField(max_length=40)
    blog_image = models.CharField(max_length=300)
    creation_date = models.DateTimeField(db_default=Now(), editable=False)
    last_updated = models.DateTimeField(db_default=Now())
    blog_content = models.CharField(max_length=4500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs', to_field='psid')


class Workshop(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=280)
    workshop_image = models.CharField(max_length=300)
    creation_date = models.DateTimeField(default=Now(),editable=False)
    last_updated = models.DateTimeField(default=Now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workshops', to_field='psid')


class Profile(models.Model):
    bio = models.CharField(max_length=300)
    age = models.IntegerField()
    facebook = models.CharField(max_length=300)
    instagram = models.CharField(max_length=300)
    tiktok = models.CharField(max_length=300)
    profile_picture = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile', to_field='psid')


class Role(models.Model):
    name = models.CharField(max_length=50)
