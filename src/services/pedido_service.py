from src.models.pedidos import Pedido

class PedidoService:
    """Classe de serviço para processar pedidos e aplicar descontos."""

    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def processar_pedidos(self):
        for pedido in self.pedidos:
            # 1. Use o nome correto da property (getValor)
            # 2. Chame o método valor_final passando esse valor
            valor_bruto = pedido.getValor 
            valor_com_desconto = pedido.valor_final(valor_bruto)
            
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor Final: {valor_com_desconto}")

