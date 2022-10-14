from itens import Item
from criador_nota_fiscal import CriadorNotaFiscal

itens = [
           Item(
               'ITEM_A',
                100                   
            ),
           Item(
               'ITEM_B',
                200
            )
          ]

nota_fiscal = CriadorNotaFiscal()

for item in itens:
    print(item.descricao, item.valor)

nota_fiscal.com_razao_social('CALCADOS RAMARIM LTDA'),
nota_fiscal.com_cnpj(29979036000140),                
nota_fiscal.com_data_de_emissao('29/12/2021'),
nota_fiscal.com_itens(itens)
nota_fiscal.com_detahes('DETALHES DA NOTA FISCAL')

print(nota_fiscal.constroi_nota().razao_social)
print(nota_fiscal.constroi_nota().cnpj)
print(nota_fiscal.constroi_nota().data_de_emissao)
print(nota_fiscal.constroi_nota().itens[0].descricao)
print(nota_fiscal.constroi_nota().itens[1].valor)
print(nota_fiscal.constroi_nota().detalhes)