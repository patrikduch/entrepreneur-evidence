from django.urls import path
from .views import (
	GetData,
	ParseURLAjax,
	urlparser
)

urlpatterns = [
    path('getdata/', GetData.as_view(), name='get_data'),
    path('', urlparser, name = 'urlparser'),
    path('parseurlajax/', ParseURLAjax.as_view(), name = "parse_url_ajax")
]
