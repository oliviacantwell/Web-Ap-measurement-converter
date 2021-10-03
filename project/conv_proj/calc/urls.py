from django.urls import path

from . import views

urlpatterns = [
    path('', views.convert, name='convert'),
    path('add', views.add, name='add')
]