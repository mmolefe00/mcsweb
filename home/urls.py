from django.urls import path
from . import views

# URLConf
urlpatterns = [

    path('', views.index),
    path('about/', views.about),
    path('philosophy/', views.philosophy),
    path('services/', views.services),
    path('contact/', views.contact),

    path('blog/', views.blog_index),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]