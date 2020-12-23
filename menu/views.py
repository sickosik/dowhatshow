from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django.db.models import Q
from .models import Menu
from .serializers import MenuSerializer
from django.http import HttpResponse, JsonResponse

# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")


# Menu Viewset
class ListMenu(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class DetailMenu(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Category in Menu
@api_view(['GET'])
def MainMenu(request):
    # value = request.GET.get('keyword')
    queryset = Menu.objects.filter(category='메인')
    serializer = MenuSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def SideMenu(request):
    # value = request.GET.get('keyword')
    queryset = Menu.objects.filter(category='사이드')
    serializer = MenuSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BeverageMenu(request):
    # value = request.GET.get('keyword')
    queryset = Menu.objects.filter(category='음료')
    serializer = MenuSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AdditionalMenu(request):
    # value = request.GET.get('keyword')
    queryset = Menu.objects.filter(category='추가')
    serializer = MenuSerializer(queryset, many=True)
    return Response(serializer.data)


# Recommand
# @api_view(['GET'])
# def RecommandMenu(request):
#     dummy_data = {
#     }
#     return JsonResponse(dummy_data)