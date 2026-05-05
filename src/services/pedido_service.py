from src.models.pedidos import Pedido

class PedidoService:
    """Classe de serviço para processar pedidos e aplicar descontos."""

    def __init__(self, repository):
        # Mude de self.pedidos para self.repository para bater com os métodos abaixo
        self.repository = repository 

    def adicionar_pedido(self, pedido: Pedido):
        self.repository.adicionar_pedido(pedido)

    def processar_pedidos(self):
        pedidos = self.repository.listar_pedidos()
        for pedido in pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor Final: {pedido.valor_final(pedido.getValor)}")

