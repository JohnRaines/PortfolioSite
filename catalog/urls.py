from django.conf.urls import url
from . import views

urlpatterns = [
	url('^$', views.index, name="catalog"),
	url('details/(?P<id>\d+)/$', views.details, name="details"),
	url('trust/', views.catalog, name="catalog2")
]