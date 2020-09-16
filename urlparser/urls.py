from django.urls import path
from .views import (
	GetData,
	ParseURLAjax,
	urlparser
)

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('getdata/', GetData.as_view(), name='get_data'),
    path('', urlparser, name = 'urlparser'),
    path('parseurlajax/', csrf_exempt(ParseURLAjax.as_view()), name = "parse_url_ajax")
]
