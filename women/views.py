from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all() так как здесь убран кверисет, то в url добавляем basename
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        # вывод части записей
        if not pk:
            return Women.objects.all()[:3]

        # вывод конкретной записи через url
        return Women.objects.filter(pk=pk)

    """    # вывод всех категорий
        @action(methods=['GET'], detail=False)
        def category(self, request):
            cats = Category.objects.all()
            return Response({'cats': [c.name for c in cats]})
    """
    # вывод конкретной категории
    @action(methods=['GET'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


'''class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

'''