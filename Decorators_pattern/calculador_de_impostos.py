from orcamento import Orcamento
from impostos import ICMS, ISS, IPI, IOF, Template_de_imposto_condicional

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print(valor)