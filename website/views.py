from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def sermons(request):
    return render(request, "sermons.html")

def ministries(request):
    return render(request, "ministries.html")

def gallery(request):
    return render(request, "gallery.html")

def event(request):
    return render(request, "event.html")
