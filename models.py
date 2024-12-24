from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    endereco = models.TextField()
    # Outros campos...

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    # Outros campos...

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    adicionado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Carrinho do cliente {self.cliente.nome} - {self.produto.nome}"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora_compra = models.DateTimeField(default=timezone.now)
    # Outros campos...

    def __str__(self):
        return f"Pedido #{self.id} - Cliente {self.cliente.nome}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item Pedido #{self.pedido.id} - {self.produto.nome}"