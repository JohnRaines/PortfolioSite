from django.conf.urls import url, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
	url('^$', views.index, name='aboutpage'),
]