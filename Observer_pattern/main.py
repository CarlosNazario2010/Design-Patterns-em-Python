from nota_fiscal import NotaFiscal
from itens import Item
from observadores import imprime, salva_no_banco, envia_por_email

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

nota_fiscal = NotaFiscal(
    'Ramarim Calcados LTDA',
    29979036000198,
    itens,
    observadores=[imprime, envia_por_email, salva_no_banco]
)

print('')

for item in itens:
    print(item.descricao, item.valor)

print(f'''
{nota_fiscal.razao_social},
{nota_fiscal.cnpj},                
{nota_fiscal.itens[0].descricao},
{nota_fiscal.itens[1].valor},
{nota_fiscal.data_de_emissao},
{nota_fiscal.detalhes}''')
