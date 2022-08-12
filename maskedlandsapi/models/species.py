from django.db import models

class Species(models.Model):
    """Species Model

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    description = models.TextField()
    primary_attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    speed = models.IntegerField()
    image_url = models.TextField()