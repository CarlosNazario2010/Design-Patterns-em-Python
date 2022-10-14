from datetime import date

from contratos import Contrato
from estado import Estado
from historico import Historico


historico = Historico()
contrato = Contrato(data=date.today(), cliente='Flávio Almeida')
print(contrato.cliente, contrato.tipo, contrato.data)
print('')

contrato.avanca()
historico.adiciona_estado(contrato.salva_estado())
print(contrato.cliente, contrato.tipo)
print('')

contrato.avanca()
contrato.cliente = 'Joao Ribeiro'
historico.adiciona_estado(contrato.salva_estado())
print(contrato.cliente, contrato.tipo)
print('')

contrato.avanca()
historico.adiciona_estado(contrato.salva_estado())
print(contrato.cliente, contrato.tipo)
print('')

contrato.restaura_estado(historico.obtem_estado(0))
print(f'Tipo do contrato restaurado {contrato.tipo}')
print(f'NOME DO CLIENTE: {contrato.cliente}')
print('')

contrato.restaura_estado(historico.obtem_estado(1))
print(f'Tipo do contrato restaurado {contrato.tipo}')
print(f'NOME DO CLIENTE: {contrato.cliente}')
print('')

contrato.restaura_estado(historico.obtem_estado(2))
print(f'Tipo do contrato restaurado {contrato.tipo}')
print(f'NOME DO CLIENTE: {contrato.cliente}')
