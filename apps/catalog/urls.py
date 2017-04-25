from django.conf.urls import url
from apps.catalog import views as catalog_views

urlpatterns = [
    url(r'^$', catalog_views.products, name='catalog')
]
