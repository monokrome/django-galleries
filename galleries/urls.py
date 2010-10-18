from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'boundless.django.galleries.views.index', name='gallery_list'),
    url(r'^gallery/(?P<identifier>[\d]+)/$', 'boundless.django.galleries.views.gallery', name='gallery_detail'),
    url(r'^gallery/(?P<identifier>[^/]+)/$', 'boundless.django.galleries.views.gallery', {'slugified': True}, name='gallery_detail'),
    url(r'^photo/(?P<identifier>[\d]+)/$', 'boundless.django.galleries.views.photo', name='photo_detail'),
    url(r'^photo/(?P<identifier>[^/]+)/$', 'boundless.django.galleries.views.photo', {'slugified': True}, name='photo_detail'),
)

