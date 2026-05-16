from newsrc.app.frameworks.database.memory_database import MemoryDatabase
from newsrc.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from newsrc.app.use_cases.criar_pedido import CriarPedido
from newsrc.app.adapters.controllers.pedido_controller import PedidoController
from newsrc.app.presenters.pedido_presenter import PedidoPresenter

def main() -> None:
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    presenter = PedidoPresenter()

    controller = PedidoController(
    criar_pedido_use_case=criar_pedido_use_case,
    presenter=presenter
    )
    # Criar os pedidos

    pedido4 = controller.criar_pedido("Cliente A", 100.0, "normal")
    pedido5 = controller.criar_pedido("Cliente B", 200.0, "vip")
    pedido6 = controller.criar_pedido("Cliente C", 300.0, "premium")

    print("Pedidos criados:")
    print(pedido4)
    print(pedido5)
    print(pedido6)

    print("\nPedidos salvos:")
    for pedido in controller.listar_pedidos():
        print (pedido)

if __name__ == "__main__":
    main()





