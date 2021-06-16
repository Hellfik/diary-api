from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_screen_view(request):
    return render(request, "content/home.html")


def client_page(response):
    return HttpResponse('<h1>Client page</h1>')
