from django.db import models
from .forms import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', primary_key=True)

