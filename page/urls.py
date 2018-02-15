from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^gallery/(?P<slug>[\w-]+)/(?P<id>[\w-]+)/$', views.post_detail, name='post_detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^success/$', views.success, name='success'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)