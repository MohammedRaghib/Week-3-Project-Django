from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:postid>', views.like, name='like'),
    path('dislike/<int:postid>', views.dislike, name='dislike'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:profid>', views.profile, name='profile_id'),
    path('moreprofs/', views.moreprofs, name='moreprofs'),
    path('editprof/', views.editprof, name='editprof'),
]

urlpatterns += staticfiles_urlpatterns()