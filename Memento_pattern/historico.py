class Historico(object):                            

    def __init__(self):
        self.__estados_salvos = []

    def obtem_estado(self, indice):                 
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado):               
        self.__estados_salvos.append(estado)