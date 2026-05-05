from src.models.pedidos import Pedido


class PedidoRepository :
    """Classe de repositório para gerar e armazenar pedidos"""

    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)
    
    def listar_pedidos(self):
        return self.pedidos
        