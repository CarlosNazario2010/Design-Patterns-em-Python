from orcamento import Orcamento
from calculador_de_impostos import Calculador_de_impostos
from impostos import ICMS, ISS

orcamento = Orcamento(500.0)
calculador_de_impostos = Calculador_de_impostos()
        
print('ISS E ICMS')
calculador_de_impostos.realiza_calculo(orcamento, ISS())
calculador_de_impostos.realiza_calculo(orcamento, ICMS())