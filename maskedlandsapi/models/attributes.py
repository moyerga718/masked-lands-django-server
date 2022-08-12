from django.db import models

class Attribute(models.Model):
    """model for Attribute names

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
