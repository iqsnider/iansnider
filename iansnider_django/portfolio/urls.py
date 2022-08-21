from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='porfolio-home'),
    path('about/', views.about, name='porfolio-about'),
]