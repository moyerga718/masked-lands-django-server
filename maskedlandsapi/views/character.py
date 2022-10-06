from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import Character
from maskedlandsapi.models import Player
from maskedlandsapi.models import Species
from maskedlandsapi.models import Background
from maskedlandsapi.models import CombatClass
from maskedlandsapi.models import Subclass
from maskedlandsapi.models import Weapon
from maskedlandsapi.models import Armor
from maskedlandsapi.serializers import CharacterCardSerializer


class CharacterView(ViewSet): 

    def retrieve(self, request, pk):
        """get details for one character by id

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """

        try:
            #GET ONE CHARACTER OBJECT THAT MATCHES ID YOU GIVE IT
            character = Character.objects.get(pk=pk)
            #PASS THAT INTO THE CHARACTER SERIALIZER WHICH CONVERTS DB DATA INTO JSON
            serializer = CharacterSerializer(character)
            #RETURN SERIALIZED JSON DATA TO CLIENT
            return Response(serializer.data)
        except Character.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """get all characters

        Args:
            request (_type_): _description_
        """

        characters = Character.objects.all()
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
