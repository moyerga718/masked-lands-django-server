from django.db import models

class Background(models.Model):
    """Background model

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    species = models.ForeignKey("Species", on_delete=models.CASCADE, related_name="backgrounds")
    description = models.TextField()
    image_url = models.TextField()
    