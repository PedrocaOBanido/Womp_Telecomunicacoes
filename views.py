from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import Cliente, Carrinho, Pedido, ItemPedido
from django.utils import timezone

def finalizar_compra(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    
    # 1. Criar um novo pedido
    novo_pedido = Pedido.objects.create(cliente=cliente, data_hora_compra=timezone.now())

    # 2. Recuperar itens do carrinho do cliente
    itens_carrinho = Carrinho.objects.filter(cliente=cliente)

    # 3. Para cada item no carrinho:
    for item_carrinho in itens_carrinho:
         # 3.1. Inserir um novo registro na tabela ItemPedido
         ItemPedido.objects.create(
            pedido=novo_pedido,
            produto=item_carrinho.produto,
            quantidade=item_carrinho.quantidade,
            preco_unitario=item_carrinho.produto.preco
         )
        # 3.2. Remover item do carrinho (opcional)
        item_carrinho.delete()


    # 4. Retornar o ID do pedido finalizado (Pode redirecionar para a página de pedidos ou de confirmação)
    return HttpResponse(f'Pedido {novo_pedido.id} finalizado com sucesso!')