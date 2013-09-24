from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
# /portfolio/
    # /
    url(r'^$', views.index, name='portfolio'),
    # /page-slug/
    url(r'^(?P<pageslug>[-\w]+)/$', views.page, name='page'),
    # /page-slug/section-slug
    url(r'^(?P<pageslug>[-\w]+)/(?P<sectionslug>[-\w]+)/$', views.section, name='section'),
    # /page-slug/section-slug/item-slug
    url(r'^(?P<pageslug>[-\w]+)/(?P<sectionslug>[-\w]+)/(?P<itemslug>[-\w]+)/$', views.item, name='item'),
    # /download/page-slug/section-slug/item-slug
    url(r'^download/(?P<pageslug>[-\w]+)/(?P<sectionslug>[-\w]+)/(?P<itemslug>[-\w]+)/(?P<versionid>\d+)/$', views.download, name='download'),
)