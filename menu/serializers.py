from rest_framework import serializers
from .models import Menu

# Menu 기본정보
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'