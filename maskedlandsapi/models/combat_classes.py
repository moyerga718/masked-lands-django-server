from django.db import models

class CombatClass(models.Model):
    """model for character classes (calling it combat class because Class is a keyword in python)

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    description = models.TextField()
    primary_attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    image_url = models.TextField()
