from django.urls import path
from . import views

urlpatterns = [
    path('urlparser/', views.urlparser, name='urlparser'),
]
