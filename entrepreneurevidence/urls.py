from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('root.urls')),
    path('urlparser/',include('urlparser.urls')),
    path('enterpreneurs/',include('enterpreneur.urls')),

]
