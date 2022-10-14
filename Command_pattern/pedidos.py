from datetime import date


class Pedido(object):

    def __init__(self, cliente, valor):                                                
        self.__cliente = cliente                     
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'
        print(f'{self.__cliente} PEDIDO FINALIZADO.')

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao