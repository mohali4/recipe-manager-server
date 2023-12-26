from rest_framework import serializers
from .models import material, recipe

class materialSerializer(serializers.ModelSerializer):
    class Meta:
        model = material
        fields = ['id','name']
class recipeSerilizer(serializers.ModelSerializer):
    # materials = materialSerializer(many=True)    
    class Meta:
        model = recipe
        fields = ['id','name','review','describtion','enerjy','materials']

    # def create(self, validated_data):
    #     materials_data = validated_data.pop('materials')
    #     recipe_instance = recipe.objects.create(**validated_data)
    #     recipe_instance.materials.set(materials_data)
    #     # for material_data in materials_data:
    #     #     material_instance = material.objects.create(**material_data)
    #     #     recipe_instance.materials.add(material_instance)

    #     return recipe_instance