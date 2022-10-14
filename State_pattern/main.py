from estado_orcamento import Estado_de_um_orcamento, \
    Em_aprovacao, Aprovado, Reprovado, Finalizado
from orcamento import Orcamento
from itens import Item


orcamento = Orcamento()
orcamento.adiciona_item(Item('ITEM - 1', 100))
orcamento.adiciona_item(Item('ITEM - 2', 50))
orcamento.adiciona_item(Item('ITEM - 3', 400))

print(orcamento.estado_atual)
print(orcamento.valor)

orcamento.aprova()
print(orcamento.estado_atual)

orcamento.finaliza()
print(orcamento.estado_atual)
