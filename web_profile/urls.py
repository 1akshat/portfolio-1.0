from django.conf.urls import url, include
from django.conf import settings
from django.views.generic.base import TemplateView

from .views import sendmail, home

urlpatterns = [
	url(r'^$', home),
	url(r'^send/$', sendmail, name='mail'),
	url(r'^blog/', include('blog.urls'), name='blog'),
]
