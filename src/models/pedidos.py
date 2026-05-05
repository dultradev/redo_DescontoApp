from src.models.desconto import IDesconto

from abc import ABC, abstractmethod

# Interface (Strategy)
class IDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class Pedido:
    def __init__(self, cliente, desconto: IDesconto):
        self.cliente = cliente
        self.desconto = desconto
        self._valor = 0.0

    @property
    def getValor(self):
        return self._valor

    # ESTE NOME DEVE SER IGUAL AO CHAMADO NO SERVICE
    def valor_final(self, valor) -> float:
        self._valor = valor
        return self._valor - self.desconto.calcular(self._valor)

    
    @getValor.setter
    def setValor(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("O valor do pedido não pode ser negativo.")
        self._valor= novo_valor