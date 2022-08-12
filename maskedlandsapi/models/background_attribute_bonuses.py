from django.db import models

class BackgroundAttributeBonus(models.Model):
    """model for bonuses to attributes based on background

    Args:
        models (_type_): _description_
    """

    background = models.ForeignKey("Background", on_delete=models.CASCADE)
    attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    bonus = models.IntegerField()
    