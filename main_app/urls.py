from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.show),
    url(r'^post_url/$', views.post_plant, name='post_plant'),
    url(r'^generargrafico/([0-9]+)/$', views.generargrafico),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
