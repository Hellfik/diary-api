from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('client/', views.client_page, name='client'),
]