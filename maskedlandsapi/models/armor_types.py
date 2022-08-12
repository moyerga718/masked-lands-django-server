from django.db import models

class ArmorType(models.Model):
    """model for armor type

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    