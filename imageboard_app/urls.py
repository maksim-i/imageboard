from django.urls import path

from .views import IndexView, PostView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>', PostView.as_view(), name='post'),
    path('new_thread/', views.new_thread, name='new_thread'),
    path('reply/', views.reply, name='reply'),
]
