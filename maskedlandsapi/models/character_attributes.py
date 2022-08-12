from django.db import models

class CharacterAttribute(models.Model):
    """model for object that stores value for a single character attribute (character "bob" has a strength value of 14...)

    Args:
        models (_type_): _description_
    """

    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    value = models.IntegerField()