from django.urls import path
from . import views
# from django.views.generic import TemplateView

# Define the application namespace as 'cats'. This is useful when you have multiple apps in a project
# and need to differentiate between URLs with the same name in different apps.
app_name = 'cats'

# Define the URL patterns for the 'cats' app. This list maps URLs to views in your Django application.
urlpatterns = [
    # Map the root URL (e.g., 'cats/') to the `MainView` view.
    # `views.MainView.as_view()` is a class-based view that will handle requests to this URL.
    # The name 'all' is used to refer to this URL pattern in templates or code.
    path('', views.MainView.as_view(), name='all'),

    # Map the URL 'main/create/' to the `CatCreate` view.
    # This view is used to create a new Cat instance.
    # The name 'cat_create' is used to refer to this URL pattern in templates or code.
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),

    # Map the URL 'main/<int:pk>/update/' to the `CatUpdate` view.
    # This view is used to update an existing Cat instance.
    # `<int:pk>` is a path converter that captures an integer primary key (pk) from the URL.
    # The name 'cat_update' is used to refer to this URL pattern in templates or code.
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),

    # Map the URL 'main/<int:pk>/delete/' to the `CatDelete` view.
    # This view is used to delete an existing Cat instance.
    # `<int:pk>` captures the primary key of the Cat to be deleted.
    # The name 'cat_delete' is used to refer to this URL pattern in templates or code.
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),

    # Map the URL 'lookup/' to the `BreedView` view.
    # This view is used to display a list of Breed instances.
    # The name 'breed_list' is used to refer to this URL pattern in templates or code.
    path('lookup/', views.BreedView.as_view(), name='breed_list'),

    # Map the URL 'lookup/create/' to the `BreedCreate` view.
    # This view is used to create a new Breed instance.
    # The name 'breed_create' is used to refer to this URL pattern in templates or code.
    path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),

    # Map the URL 'lookup/<int:pk>/update/' to the `BreedUpdate` view.
    # This view is used to update an existing Breed instance.
    # `<int:pk>` captures the primary key of the Breed to be updated.
    # The name 'breed_update' is used to refer to this URL pattern in templates or code.
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),

    # Map the URL 'lookup/<int:pk>/delete/' to the `BreedDelete` view.
    # This view is used to delete an existing Breed instance.
    # `<int:pk>` captures the primary key of the Breed to be deleted.
    # The name 'breed_delete' is used to refer to this URL pattern in templates or code.
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]