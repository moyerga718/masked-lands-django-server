from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action

from maskedlandsapi.models import Character
from maskedlandsapi.models import CharacterAttribute
from maskedlandsapi.models import Player
from maskedlandsapi.models import Species
from maskedlandsapi.models import Background
from maskedlandsapi.models import CombatClass
from maskedlandsapi.models import Subclass
from maskedlandsapi.models import Weapon
from maskedlandsapi.models import Armor
from maskedlandsapi.serializers import CharacterCardSerializer
from maskedlandsapi.serializers.character import CharacterSheetSerializer
from maskedlandsapi.serializers.character_attribute import CharacterAttributeSerializer


class CharacterView(ViewSet): 

    def retrieve(self, request, pk):
        """get details for one character by id

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """

        try:
            #Get character object
            character = Character.objects.get(pk=pk)

            #Get Character attributes
            char_attributes = CharacterAttribute.objects.filter(character__id = character.id)

            #Pass character obj into character sheet serializer. 
            char_serializer = CharacterSheetSerializer(character)
            attribute_serializer = CharacterAttributeSerializer(char_attributes, many=True)

            data = {
                "character": char_serializer.data,
                "attributes": attribute_serializer.data
            }
            #RETURN SERIALIZED JSON DATA TO CLIENT
            return Response(data)
        except Character.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """get all characters

        Args:
            request (_type_): _description_
        """

        name = request.query_params.get('name', None)
        species = request.query_params.get('species', None)
        background = request.query_params.get('background', None)
        combat_class = request.query_params.get('class', None)
        subclass = request.query_params.get('subclass', None)
        characters = Character.objects.all()

        if name is not None:
            characters = characters.filter(name__contains=name)
        if species is not None and species != "0":
            characters = characters.filter(species__id=int(species))
        if background is not None and background != "0":
            characters = characters.filter(background__id=int(background))
        if combat_class is not None and combat_class != "0":
            characters = characters.filter(combat_class__id=int(combat_class))
        if subclass is not None and subclass != "0":
            characters = characters.filter(subclass__id=int(subclass))

        serializer = CharacterCardSerializer(characters, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests for a new character entry.
        """

        player = Player.objects.get(user=request.auth.user)
        species = Species.objects.get(pk=request.data["species_id"])
        background = Background.objects.get(pk=request.data["background_id"])
        combat_class = CombatClass.objects.get(pk=request.data["combat_class_id"])
        subclass = Subclass.objects.get(pk=request.data["subclass_id"])
        weapon = Weapon.objects.get(pk=request.data["weapon_id"])
        armor = Armor.objects.get(pk=request.data["armor_id"])

        character = Character.objects.create(
            name=request.data["name"],
            xp=request.data["xp"],
            bio=request.data["bio"],
            image_url=request.data["image_url"],
            player=player,
            species=species,
            background=background,
            combat_class=combat_class,
            subclass=subclass,
            weapon=weapon,
            armor=armor
        )

        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def update(self, request, pk):
        """UPDATE A CHARACTER. Mostly will be used to update xp... 

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """
        character = Character.objects.get(pk=pk)
        character.name = request.data["name"]
        character.xp = request.data["xp"]
        character.bio = request.data["bio"]
        character.image_url = request.data["image_url"]

        species = Species.objects.get(pk=request.data["species_id"])
        background = Background.objects.get(pk=request.data["background_id"])
        combat_class = CombatClass.objects.get(pk=request.data["combat_class_id"])
        subclass = Subclass.objects.get(pk=request.data["subclass_id"])
        weapon = Weapon.objects.get(pk=request.data["weapon_id"])
        armor = Armor.objects.get(pk=request.data["armor_id"])

        character.species=species
        character.background=background
        character.combat_class=combat_class
        character.subclass=subclass
        character.weapon=weapon
        character.armor=armor

        character.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk): 
        """delete a character

        Returns:
            _type_: _description_
        """
        character = Character.objects.get(pk=pk)
        character.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ('id','name','player','xp','bio','image_url','species','background','combat_class','subclass','weapon','armor','level')
        depth = 2
