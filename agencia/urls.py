from django.conf.urls import url, include
from django.contrib import admin
from cars import urls as carsUrls
from django.views.static import serve
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(carsUrls)),
    url(
    	regex=r'^media/(?P<path>.*)/$',
    	view=serve,
    	kwargs={"document_root":settings.MEDIA_ROOT}
    	),
]