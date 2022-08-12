from django.db import models

class WeaponType(models.Model):
    """Model for weapon types

    Args:
        models (_type_): _description_
    """

    name = models.TextField()