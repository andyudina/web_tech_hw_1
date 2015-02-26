from django.conf.urls import include, url
from django.contrib import admin
from helloworld.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
]
