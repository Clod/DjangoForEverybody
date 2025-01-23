from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Defines a namespace for the app
app_name = 'home'

urlpatterns = [
    # The page is defined in the home app in mysite/home/views.py
    # by the HomeView class
    # The name is used by the {% url %} template tag to generate the URL
    # for the page within the namespace defined in the app_name
    path('', views.HomeView.as_view(), name='home'),
]
