from register import views
from django.conf.urls import url


urlpatterns = [
    url('cadastro', views.index),
    url('register', views.register),
    url('login', views.login),
    url('success', views.success)
]
