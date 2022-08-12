from django.db import models

class Spell(models.Model):
    """spell model

    Args:
        models (_type_): _description_
    """

    name = models.TextField()
    god = models.ForeignKey("God", on_delete=models.CASCADE)
    devotion_level = models.IntegerField()
    short_description = models.TextField()
    full_description = models.TextField()
    action_type = models.ForeignKey("ActionType", on_delete=models.CASCADE)
    will_cost = models.TextField()
    attack_range = models.IntegerField()
    