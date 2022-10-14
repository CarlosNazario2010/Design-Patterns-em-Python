from fila_de_trabalho import Fila_de_trabalho
from comandos import Comando, Paga_pedido, Conclui_pedido
from pedidos import Pedido


pedido1 = Pedido('Flávio', 150)
pedido2 = Pedido('Almeida', 250)

fila_de_trabalho = Fila_de_trabalho()

fila_de_trabalho.adiciona(Paga_pedido(pedido1))
fila_de_trabalho.adiciona(Paga_pedido(pedido2))
fila_de_trabalho.adiciona(Conclui_pedido(pedido1))
fila_de_trabalho.adiciona(Conclui_pedido(pedido2))

fila_de_trabalho.processa()
