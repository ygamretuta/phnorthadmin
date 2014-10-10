from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tastypie.api import Api
from members.api.resources import MemberResource

v1_api = Api(api_name='v1')
v1_api.register(MemberResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

