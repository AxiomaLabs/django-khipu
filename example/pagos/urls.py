from django.conf.urls import url, include
from .views import carro


urlpatterns = [
    url(r'^carro/$', carro, name='carro'),
    url(r'^khipu/', include('khipu.urls')),
]
