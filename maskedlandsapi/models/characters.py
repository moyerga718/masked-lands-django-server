from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    """class for a single character

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    xp = models.IntegerField()
    bio = models.TextField()
    image_url = models.TextField()
    species = models.ForeignKey("Species", on_delete=models.CASCADE)
    background = models.ForeignKey("Background", on_delete=models.CASCADE)
    combat_class = models.ForeignKey("CombatClass", on_delete=models.CASCADE)
    subclass = models.ForeignKey("Subclass", on_delete=models.CASCADE)
    weapon = models.ForeignKey("Weapon", on_delete=models.CASCADE)
    armor = models.ForeignKey("Armor", on_delete=models.CASCADE)
