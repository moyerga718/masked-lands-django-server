from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)