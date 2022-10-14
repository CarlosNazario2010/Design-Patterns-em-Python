from impressora import Impressora
from soma import Soma
from subtracao import Subtracao
from numeros import Numero


expressao_esquerda = Subtracao(Numero(10), Numero(5))
expressao_direita = Soma(Numero(2), Numero(10))
expressao_conta = Soma(expressao_esquerda, expressao_direita)

visitor = Impressora()
expressao_conta.aceita(visitor)
