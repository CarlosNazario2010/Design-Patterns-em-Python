from abc import ABCMeta, abstractmethod

from pedidos import Pedido

class Comando(Pedido):

    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass


class Conclui_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()
  

class Paga_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    @property
    def pedido(self):
        return self.__pedido

    def executa(self):
        self.__pedido.paga()
        print(f'PAGANDO PEDIDO...{self.pedido.cliente} - \
            R$ {self.pedido.valor}')
