from django.db import models 

class Armor(models.Model):
    """Armor model

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    armor_type = models.ForeignKey("ArmorType", on_delete=models.CASCADE)
    base_ac = models.IntegerField()
    dex_bonus = models.BooleanField()
    bonus_cap = models.IntegerField()
    strength_requirement = models.IntegerField()
    image_url = models.TextField()