from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # The page is defined in the home app in mysite/home/views.py
    # by the HomeView class
    path('', views.HomeView.as_view()),
]
