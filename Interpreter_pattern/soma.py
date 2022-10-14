class Soma(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda 
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia() + \
            self.__expressao_direita.avalia())

