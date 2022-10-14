from orcamento import Orcamento, Item
from impostos import ICMS, ISS, IPI, IOF, Template_de_imposto_condicional
from calculador_de_impostos import Calculador_de_impostos

orcamento = Orcamento()
orcamento.adiciona_item(Item('ITEM - 1', 50))
orcamento.adiciona_item(Item('ITEM - 2', 200))
orcamento.adiciona_item(Item('ITEM - 3', 250))

print('VALOR E TOTAL DE ITENS')
print(orcamento.valor)
print(orcamento.total_itens)

calculador_de_impostos = Calculador_de_impostos()

print('ISS e ICMS com IPVX50 (mais R$ 50,00)')
calculador_de_impostos.realiza_calculo(orcamento, ISS())
calculador_de_impostos.realiza_calculo(orcamento, ICMS())

print('ISS com ICMS (ambos com IPVX50)')
calculador_de_impostos.realiza_calculo(orcamento, ISS(ICMS()))

print('IPI IOF')
calculador_de_impostos.realiza_calculo(orcamento, IPI())
calculador_de_impostos.realiza_calculo(orcamento, IOF())

print('IPI com IOF')
calculador_de_impostos.realiza_calculo(orcamento, IPI(IOF()))
