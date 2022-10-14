from estado import Estado


class Contrato(object):

    def __init__(self, data, cliente, tipo = "NOVO"):
        self.__data = data
        self.__cliente = cliente
        self.__tipo = tipo                       
                                    
    @property
    def data(self):                             
        return self.__data                         

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def cliente(self):                     
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def avanca(self):
        
        if self.__tipo == 'NOVO':                       
            self.__tipo = 'EM ANDAMENTO'                
        elif self.__tipo == 'EM ANDAMENTO':
            self.__tipo = 'ACERTADO'
        elif self.__tipo == 'ACERTADO': 
            self.__tipo = 'CONCLUIDO'

    def salva_estado(self):                             
        return Estado(Contrato(data = self.__data,       
                               cliente = self.__cliente, 
                               tipo = self.__tipo))

    def restaura_estado(self, estado):               
        self.__data = estado.contrato.data           
        self.__cliente = estado.contrato.cliente     
        self.__tipo = estado.contrato.tipo
