import abc
from newsrc.app.entities.pedido import Pedido

class IPedidoGateway(abc.ABC):
    @abc.abstractclassmethod
    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        pass
    @abc.abstractclassmethod
    def listar(self) -> list[Pedido]:
        pass