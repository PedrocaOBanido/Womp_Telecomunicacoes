from django.urls import path
from . import views

urlpatterns = [
    # outras rotas
    path('finalizar-compra/<int:cliente_id>/', views.finalizar_compra, name='finalizar_compra'),
]