from src.services.pedido_service import PedidoService
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.models.pedidos import Pedido

if __name__ == "__main__":
    service = PedidoService()

    """Criando pedidos e aplicando desconto"""


    pedido1 = Pedido("Leonardo", DescontoVIP())
    pedido1.setValor = 100

    pedido2 = Pedido("Marcão", DescontoNormal())
    pedido2.setValor = 200

    pedido3 = Pedido("Rian", DescontoPremium())
    pedido3.setValor = 300
   

service.adicionar_pedido(pedido1)
service.adicionar_pedido(pedido2)
service.adicionar_pedido(pedido3)

service.processar_pedidos()