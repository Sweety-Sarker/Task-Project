from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customuserModel(AbstractUser):
    profile_picture=models.ImageField(upload_to='media/photo',null=True)
    bio=models.TextField(null=True)


class taskModel(models.Model):
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    due_date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    priority=models.CharField(max_length=100,null=True,choices=[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),

    ])
    status=models.CharField(max_length=100,null=True,choices=[
        ('pending','Pending'),
        ('inprogress','Inprogress'),
        ('completed','Completed'),
    ])

    user=models.ForeignKey(customuserModel,on_delete=models.CASCADE,null=True)