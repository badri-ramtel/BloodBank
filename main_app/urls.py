from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='mainapp-home'),
    path('add/', views.add, name='mainapp-add')
]