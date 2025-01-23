# DjangoForEverybody

Michigan University's Django for Everybody (Insanely commented LOL)

SqLite3 superuser credencials are:


**username:** admin

**password:** admin


Where did those come from?

Easy:

After creating the migrations (to create the necessary files in the database) do:

```
$ python manage.py createsuperuser
```

And to launch the server:

```
% python manage.py runserver                  # Default localhost:8000
% python manage.py runserver 8080             # Custom port
% python manage.py runserver 0.0.0.0:8000     # Allow external access  
```

Django administration console is at: [http://127.0.0.1:8000/admin](https://)

Apps are created with:

% python manage.py startapp <app_name>  # <app_name> is the name of the app

and the apps themselves to mysites/settings.py

and the localization of the apps to mysite/urls.py

In that file you will find:

```
urlpatterns = [
    # The line below defines the default page for the site
    # The exact page is defined in the home app in mysite/home/urls.py
    path('', include('home.urls')),
    . . .
]
```


therefore, theHome screen is:

mysite/home/templates/home/main.html

as defined in the home app in mysite/home/urls.py:


```language
urlpatterns = [
    # The page is defined in the home app in mysite/home/views.py
    # by the HomeView class
    path('', views.HomeView.as_view()),
]
```


Cadorna / V4ffancul0

The login page is defined in the home app in mysite/home/templates/home/main.html

mysite/home/templates/registration/login_social.html
