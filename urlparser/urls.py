from django.urls import path
from .views import (
	GetData
)

urlpatterns = [
    path('urlparser/', GetData.as_view(), name='urlparser')
]
