from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    balance = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='patient/images/', blank=True, null=True)
    mobile_no = models.CharField(max_length = 11)
    


