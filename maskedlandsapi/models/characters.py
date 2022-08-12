from django.db import models

class Character(models.Model):
    """class for a single character

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE, null=True)
    xp = models.IntegerField()
    bio = models.TextField()
    image_url = models.TextField()
    species = models.ForeignKey("Species", on_delete=models.CASCADE)
    background = models.ForeignKey("Background", on_delete=models.CASCADE)
    combat_class = models.ForeignKey("CombatClass", on_delete=models.CASCADE)
    subclass = models.ForeignKey("Subclass", on_delete=models.CASCADE)
    weapon = models.ForeignKey("Weapon", on_delete=models.CASCADE)
    armor = models.ForeignKey("Armor", on_delete=models.CASCADE)

    @property
    def level(self):
        """property to calculate level based on XP"""

        xp = self.xp
        level = 0

        if xp < 300: 
            level = 0
        elif xp < 900:
            level = 1
        elif xp < 2700:
            level = 2
        elif xp < 6500:
            level = 3
        elif xp < 14000:
            level = 4
        elif xp < 23000:
            level = 5
        elif xp < 34000:
            level = 6
        elif xp < 48000:
            level = 7
        elif xp < 64000:
            level = 8
        elif xp >= 64000:
            level = 9

        return level
