"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
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
