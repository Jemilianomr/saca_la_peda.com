from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$', views.Home.as_view(), name="list"),
	url(r'^(?P<pk>\d+)/$', views.CarDetail.as_view(),name="detail"),
	url(r'^nuevo/$', views.CarCreation.as_view(), name="new"),
	url(r'^editar/(?P<pk>\d+)/$', views.CarUpdate.as_view(), name="update"),
    url(r'^borrar/(?P<pk>\d+)/$', views.CarDelete.as_view(), name="delete"),

]