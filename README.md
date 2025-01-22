# DjangoForEverybody

Michigan University's Django for Everybody (Insanely commented LOL)

SqLite3 superuser credencials are:

```
username: admin
password: admin
```

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


Each app path mut be added to mysite/urls.py

and the apps themselves to mysites/settings.py


Home screen is:

mysite/home/templates/home/main.html