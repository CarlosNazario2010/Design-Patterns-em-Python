from abc import ABCMeta, abstractmethod

from orcamento import Orcamento, Item
from impostos import ICMS, ISS, IPI, IOF
from calculador_de_impostos import Calculador_de_impostos

orcamento = Orcamento()
orcamento.adiciona_item(Item('ITEM - 1', 50))
orcamento.adiciona_item(Item('ITEM - 2', 200))
orcamento.adiciona_item(Item('ITEM - 3', 250))

print('VALOR E TOTAL DE ITENS')
print(orcamento.valor)
print(orcamento.total_itens)
print('')

calculador_de_impostos = Calculador_de_impostos()

print('ISS ICMS')
calculador_de_impostos.realiza_calculo(orcamento, ISS())
calculador_de_impostos.realiza_calculo(orcamento, ICMS())
print('')

print('IPI IOF')
calculador_de_impostos.realiza_calculo(orcamento, IPI())
calculador_de_impostos.realiza_calculo(orcamento, IOF())