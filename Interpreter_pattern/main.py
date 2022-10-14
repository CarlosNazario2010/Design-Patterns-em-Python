from numero import Numero
from soma import Soma
from subtracao import Substracao

# RESULTADO RECEBE O METODO avalia() DA CLASSE SOMA
expressao_esquerda = Substracao(Numero(10), Numero(5))
expressao_direita = Soma(Numero(2), Numero(10))
expressao_conta = Soma(expressao_esquerda, expressao_direita)

resultado = expressao_conta.avalia()
print(resultado)
