from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("sermons/", views.sermons, name="sermons"),
    path("ministries/", views.ministries, name="ministries"),
    path("gallery/", views.gallery, name="gallery"),
]
