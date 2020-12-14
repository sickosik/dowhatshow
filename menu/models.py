from django.conf import settings
from django.db import models


# 전체 메뉴 테이블

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True) #PK(메뉴PK)
    menu_name = models.CharField(max_length=30) #메뉴 이름
    category = models.CharField(max_length=15) #카테고리 분류
    price = models.IntegerField(blank=True, null=True) #가격
    description = models.CharField(max_length=300, blank=True, null=True) #설명
    
    class Meta:
        db_table = 'MENU_TB'

    def __str__(self):
        return self.name