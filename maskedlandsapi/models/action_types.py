from django.db import models 

class ActionType(models.Model):
    """Action types model (reaction, standard action, bonus action, passive ability, etc....)

    Args:
        models (_type_): _description_
    """

    name = models.TextField()