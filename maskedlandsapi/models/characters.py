from django.db import models
from maskedlandsapi.models.background_attribute_bonuses import BackgroundAttributeBonus
from maskedlandsapi.models.armors import Armor
from maskedlandsapi.models.subclasses import Subclass
from math import floor
from math import ceil

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
    base_max_life = models.IntegerField(default=5)
    base_max_will= models.IntegerField(default=5)
    base_max_stamina = models.IntegerField(default=5)
    current_life = models.IntegerField(default=5)
    current_will = models.IntegerField(default=5)
    current_stamina = models.IntegerField(default=5)
    hit_die = models.IntegerField(default = 6)
    species = models.ForeignKey("Species", on_delete=models.CASCADE)
    background = models.ForeignKey("Background", on_delete=models.CASCADE)
    combat_class = models.ForeignKey("CombatClass", on_delete=models.CASCADE)
    subclass = models.ForeignKey("Subclass", on_delete=models.CASCADE)
    weapon = models.ForeignKey("Weapon", on_delete=models.CASCADE)
    armor = models.ForeignKey("Armor", on_delete=models.CASCADE)
    base_strength = models.IntegerField(default = 10)
    base_dexterity = models.IntegerField(default = 10)
    base_constitution = models.IntegerField(default = 10)
    base_intelligence = models.IntegerField(default = 10)
    base_attunement = models.IntegerField(default = 10)
    base_charisma = models.IntegerField(default = 10)
    sunface_pts = models.IntegerField(default = 0)
    moonface_pts = models.IntegerField(default = 0)
    escritorio_pts = models.IntegerField(default = 0)
    goge_pts = models.IntegerField(default = 0)
    faelina_pts = models.IntegerField(default = 0)
    garthank_pts = models.IntegerField(default = 0)

    def devotion_lvl(self, pts):
        """Function for calculating devotion level based on # of devotion pts"""

        if pts >= 21:
            lvl = 5
        elif pts >= 15:
            lvl = 4
        elif pts >= 9:
            lvl = 3
        elif pts >= 5:
            lvl = 2
        elif pts >= 2:
            lvl = 1
        else:
            lvl = 0
        
        return lvl

    def eff_att_calc(self, base_val, att_id):
        """function for calculating effective attribute value after background bonuses."""
        background = self.background
        
        try:
            background_att_bonus = BackgroundAttributeBonus.objects.get(background=background, attribute__id=att_id)
            bonus = background_att_bonus.bonus
            eff_val = base_val + bonus
        except:
            eff_val = base_val

        return eff_val

    def mod_calc(self, eff_val):
        """function for calculating attribute modifier from effective attribute value"""

        if eff_val > 10:
            mod = floor((eff_val - 10) / 2)
        else:
            mod = ceil((eff_val - 10) / 2)

        return mod

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

    @property
    def max_life(self):
        """calculates max life from base max life and con mod"""
        return self.base_max_life + self.con_mod

    @property
    def max_will(self):
        """calculates max will from base max will and att mod"""
        return self.base_max_will + self.att_mod

    @property
    def max_stamina(self):
        """calculates max stamina from base max stamina and con mod"""
        return self.base_max_stamina + self.con_mod

    # Properties to find effective attribute values

    @property
    def eff_strength(self):
        """property to calculate effective strength, incorporating bonuses from background"""
        return self.eff_att_calc(self.base_strength, 1)

    @property
    def eff_dexterity(self):
        """property to calculate effective strength, incorporating bonuses from background"""
        return self.eff_att_calc(self.base_dexterity, 2)

    @property
    def eff_constitution(self):
        """property to calculate effective constitution, incorporating bonuses from background"""
        return self.eff_att_calc(self.base_constitution, 3)

    @property
    def eff_intelligence(self):
        """property to calculate effective intelligence, incorporating bonuses from background"""
        return self.eff_att_calc(self.base_intelligence, 4)

    @property
    def eff_attunement(self):
        """property to calculate effective attunement, incorporating bonuses from background"""
        return self.eff_att_calc(self.base_attunement, 5)

    @property
    def eff_charisma(self):
        """property to calculate effective charisma, incorporating bonuses from background"""
        return self.eff_att_calc(self.base_charisma, 6)

    #Properties to calculate modifiers for effective attribute values

    @property
    def str_mod(self):
        """property to calculate strength modifier from effective strength value"""
        return self.mod_calc(self.eff_strength)

    @property
    def dex_mod(self):
        """property to calculate dexterity modifier from effective dexterity value"""
        return self.mod_calc(self.eff_dexterity)

    @property
    def con_mod(self):
        """property to calculate constitution modifier from effective constitution value"""
        return self.mod_calc(self.eff_constitution)

    @property
    def int_mod(self):
        """property to calculate intelligence modifier from effective intelligence value"""
        return self.mod_calc(self.eff_intelligence)

    @property
    def att_mod(self):
        """property to calculate attunement modifier from effective attunement value"""
        return self.mod_calc(self.eff_attunement)

    @property
    def cha_mod(self):
        """property to calculate charisma modifier from effective charisma value"""
        return self.mod_calc(self.eff_charisma)

    #Properties to calculate devotion level based off of devotion points for each god

    @property
    def sunface_lvl(self):
        """calculate characters sunface devotion lvl"""
        lvl = self.devotion_lvl(self.sunface_pts)
        return lvl

    @property
    def moonface_lvl(self):
        """calculate characters moonface devotion lvl"""
        lvl = self.devotion_lvl(self.moonface_pts)
        return lvl

    @property
    def escritorio_lvl(self):
        """calculate characters escritorio devotion lvl"""
        lvl = self.devotion_lvl(self.escritorio_pts)
        return lvl

    @property
    def goge_lvl(self):
        """calculate characters goge devotion lvl"""
        lvl = self.devotion_lvl(self.goge_pts)
        return lvl

    @property
    def faelina_lvl(self):
        """calculate characters faelina devotion lvl"""
        lvl = self.devotion_lvl(self.faelina_pts)
        return lvl

    @property
    def garthank_lvl(self):
        """calculate characters garthank devotion lvl"""
        lvl = self.devotion_lvl(self.garthank_pts)
        return lvl

    @property
    def ac(self):
        """Calculate characters effective AC"""
        
        #Get armor object
        armor_obj = Armor.objects.get(pk=self.armor.id)

        #If armor doesn't give character ac bonus from dex mod (heavy armor)...
        if armor_obj.dex_bonus is False:
            #AC is equal to armors base AC
            ac = armor_obj.base_ac
        #If armor does allow ac bonus from dex mod, but that bonus has a cap...
        elif armor_obj.dex_bonus is True and armor_obj.bonus_cap > 0:
            #Check to see if bonus cap is greater than characters current dex mod.
            if armor_obj.bonus_cap > self.dex_mod:
                #if bonus cap is greater than dex mod, add dex mod to armors base ac
                ac = armor_obj.base_ac + self.dex_mod
            else: 
                #if dex mod has exceeded bonus cap, just add bonus cap to armors base ac
                ac = armor_obj.base_ac + armor_obj.bonus_cap
        # if armor allows ac bonus from dex mod and there is no bonus cap, add full dex mod to base ac.
        else:
            ac = armor_obj.base_ac + self.dex_mod

        return ac