from django.urls import path

from . import views

app_name = "hello"

urlpatterns = [
    # Absurdly long name, but it help undestand it is arbitrary
    path("", views.myview, name='hello_app_home_page'),
    path("fun/", views.sessfun, name='fun'),
]