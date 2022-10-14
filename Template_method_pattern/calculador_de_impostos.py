from orcamento import Orcamento, Item
from impostos import Template_de_imposto_condicional, ICMS, ISS, IPI, IOF


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print(valor)
