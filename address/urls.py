from django.conf.urls import url
from address import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^candidatos$', views.apply),
    url(r'^empresas$', views.companies),
    url(r'^sobre$', views.about)
]
