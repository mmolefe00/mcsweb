from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('philosophy/', views.philosophy),
    path('services/', views.services),
    path('contact/', views.contact)
]