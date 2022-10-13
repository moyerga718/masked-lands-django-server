from django.db import models

class Subclass(models.Model):
    """Subclass model

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    combat_class = models.ForeignKey("CombatClass", on_delete=models.CASCADE, related_name="subclasses")
    hit_die = models.IntegerField()
    life = models.IntegerField()
    will = models.IntegerField()
    will_per_level = models.IntegerField()
    stamina = models.IntegerField()
    stamina_per_level = models.IntegerField()
    devotion_points = models.IntegerField()
    image_url= models.TextField()
    description = models.TextField()
    weapon_proficiencies = models.ManyToManyField("WeaponType", related_name="subclasses")
    armor_proficiencies = models.ManyToManyField("ArmorType", related_name="subclasses")