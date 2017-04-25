from django.conf.urls import url
from apps.core import views as core_views

urlpatterns = [
    url(r'^contact/$', core_views.contact, name='contact'),
    url(r'^send_contact/$', core_views.send_contact, name='send_contact'),
    url(r'^$', core_views.IndexView.as_view(), name='index')
]
