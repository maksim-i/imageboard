from django.urls import path

from .views import IndexView, ImageboardView, PostView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imageboard_home/', ImageboardView.as_view(), name='imageboard'),
    path('<slug:slug>', PostView.as_view(), name='post'),
    path('imageboard_home/new_thread/', views.new_thread, name='new_thread'),
    path('imageboard_home/reply/', views.reply, name='reply'),
]
