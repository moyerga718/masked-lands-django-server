from django.db import models 

class God(models.Model):
    """GOD MODEL

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    short_name = models.TextField()
    description = models.TextField()
    alignment = models.TextField()
    rgb = models.TextField()
    icon_url = models.TextField()
    image_url = models.TextField()