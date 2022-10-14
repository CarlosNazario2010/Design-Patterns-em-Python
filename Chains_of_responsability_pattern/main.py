from calculador_de_descontos import Calculador_de_decontos
from orcamento import Orcamento, Item
from descontos import Desconto_por_cinco_itens, Desconto_por_mais_quinhentos_reais, Sem_desconto

orcamento = Orcamento()
orcamento.adiciona_item(Item('ITEM - 1', 100))
orcamento.adiciona_item(Item('ITEM - 2', 50))
orcamento.adiciona_item(Item('ITEM - 3', 400))

print('VALOR E TOTAL DE ITENS')
print(orcamento.valor)
print(orcamento.total_itens)

calculador = Calculador_de_decontos()            
desconto = calculador.calcula(orcamento)       

print('DESCONTO APLICADO')
print(f'{desconto:.2f}')