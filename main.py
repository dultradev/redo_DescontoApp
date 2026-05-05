from src.repositories.pedido_repository import PedidoRepository
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.models.pedidos import Pedido
from src.services.pedido_service import PedidoService
from src.controllers.pedido_controller import PedidoController

if __name__ == "__main__":
    repo = PedidoRepository()
    service = PedidoService(repo)
    controller = PedidoController(service)

    """Criando pedidos e aplicando desconto"""

    pedido1 = Pedido(cliente="Leonardo", desconto=DescontoVIP())
    pedido1.setValor = 100

    pedido2 = Pedido(cliente="Marcão", desconto=DescontoNormal())
    pedido2.setValor = 200

    pedido3 = Pedido(cliente="Rian", desconto=DescontoPremium())
    pedido3.setValor = 300
   

controller.adicionar_pedido(pedido1)
controller.adicionar_pedido(pedido2)
controller.adicionar_pedido(pedido3)

controller.processar_pedidos()
