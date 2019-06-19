from django.conf.urls import url
from address import views

urlpatterns = [
    url(r'^home', views.homepage),
    url(r'candidatos', views.apply),
    url(r'endereco', views.applyendereco),
    url(r'contato', views.applycontato),
    url(r'formacao', views.applyformacao),
    url(r'habilidade', views.applyhabilidade),
    #url(r'^listagem$', views.listagem),
    url(r'empresas', views.companies),
    url(r'sobre', views.about)
]
