from orcamento import Orcamento, Item
from descontos import Desconto_por_cinco_itens, Desconto_por_mais_quinhentos_reais, Sem_desconto

class Calculador_de_decontos(object):

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_quinhentos_reais(
                Sem_desconto())).calcula(orcamento)
        
        return desconto
