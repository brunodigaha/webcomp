from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from core.views import HomeClass
from core.views import SobreClass, ContatoClass

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webcomp.views.home', name='home'),
    # url(r'^webcomp/', include('webcomp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',HomeClass.as_view(), name='home'),
    url(r'^sobre$',SobreClass.as_view(), name='sobre'),
    url(r'^contato$',ContatoClass.as_view(), name='contato'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)