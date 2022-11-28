from django.urls import path
from . import views
app_name = "cliente"
urlpatterns = [
    path("", view=views.index, name="index"),
    path("lista",views.lista , name="lista"),
    path("lista/<int:id>/",views.detalhe),
    path("contatos/",views.contato)
]
