import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    # Скрыть поле "Пользователь", чтобы при добавлении записи она сразу вязалась с юзером
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = "__all__"


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
