from django.urls import path
from . import views

urlpatterns = [
    path('', views.enterpreneurs, name='enterpreneurs'),
]
