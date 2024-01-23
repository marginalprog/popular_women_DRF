import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

"""class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content"""


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()  # не "cat",  а cat_id

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance


"""
#  Аналог работы get и post. +- такая же конструкция (код и декод) лежит в Response 
# с использованием класса сериализатора
def encode():
    model = WomenModel('Angelina Jolie', 'content: Angelina Jolie')
    model_serializer = WomenSerializer(model)
    print(model_serializer.data, type(model_serializer.data), sep='\n')
    json = JSONRenderer().render(model_serializer.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"content: Angelina Jolie"}')
    data = JSONParser().parse(stream)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.is_valid())
    print(serializer.validated_data)

"""
