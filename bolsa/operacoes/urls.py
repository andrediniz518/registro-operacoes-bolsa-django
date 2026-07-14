from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('nova-operacao/', views.nova_operacao, name='nova_operacao'),
    path(
        "editar-operacao/<int:id>",
        views.editar_operacao,
        name="editar_operacao",
    ),
    path(
        "excluir-operacao/<int:id>",
        views.excluir_operacao,
        name="excluir_operacao",
    ),
]