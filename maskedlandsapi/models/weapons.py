from django.db import models

class Weapon(models.Model): 
    """Weapon model

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    weapon_type = models.ForeignKey("WeaponType", on_delete=models.CASCADE)
    attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    damage_die = models.IntegerField()
    number_of_damage_die = models.IntegerField()
    image_url = models.TextField()
    