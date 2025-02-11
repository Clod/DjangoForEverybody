from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    # http://127.0.0.1:8000/ads
    # Shows the list of ads (see class AdListView in ads/views.py)
    path('', views.AdListView.as_view(), name='all'),
    # http://127.0.0.1:8000/ads/ad/1 (1 is the number of the ad)
    # Shows the details of an ad (see class AdDetailView in ads/views.py)
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    # http://127.0.0.1:8000/ads/ad/create
    # Creates a new ad and is handled by the class AdCreateView in ads/views.py
    path('ad/create',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
    path('ad/<int:pk>/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    path('ad/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('ad/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_comment_delete'),
    path('ad/<int:pk>/favorite',
    # url to call the AddFavoriteView class in views.py
    views.AddFavoriteView.as_view(), name='ad_favorite'),
    # url to call the DeleteFavoriteView class in views.py
    path('ad/<int:pk>/unfavorite',
    views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]