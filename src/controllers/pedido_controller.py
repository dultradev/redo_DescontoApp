from src.models.pedidos import Pedido
from src.services.pedido_service import PedidoService

class PedidoController:
    """Classe de controlador para gerenciar a lógica de negócio"""

    def __init__(self, service: PedidoService):
        self.service = service

    def adicionar_pedido(self, pedido: Pedido):
        self.service.adicionar_pedido(pedido)

    def processar_pedidos(self):
        self.service.processar_pedidos()