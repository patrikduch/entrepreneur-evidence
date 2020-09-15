from django.urls import path
from .views import (
	GetData,
	ParseURLAjax
)

urlpatterns = [
    path('urlparser/', GetData.as_view(), name='urlparser'),
    path('testik/', ParseURLAjax.as_view(), name = "ParseURLAjax")
]
