from orcamento import Orcamento
from impostos import ICMS, ISS

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print(valor)