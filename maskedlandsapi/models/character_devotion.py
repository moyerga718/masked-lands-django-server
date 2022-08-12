from django.db import models

class CharacterDevotion(models.Model):
    """model for objects that keep track of character devotion to a specific god.

    Args:
        models (_type_): _description_
    """

    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    god = models.ForeignKey("God", on_delete=models.CASCADE)
    devotion_points = models.IntegerField()
    devotion_level = models.IntegerField()
