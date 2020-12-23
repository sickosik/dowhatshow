from django.urls import path, include
from .views import helloAPI
from . import views

urlpatterns = [
  path("hello/", helloAPI),

  # Menu
  path("menu/", views.ListMenu.as_view()),
  path("menu/<int:pk>", views.DetailMenu.as_view()),

  # Category in Menu
  path('menu/main', views.MainMenu),
  path('menu/side', views.SideMenu),
  path('menu/beverage', views.BeverageMenu),
  path('menu/add', views.AdditionalMenu),
  
  # Recommand Menu
  # path('menu/recommand', views.RecommandMenu)
]