from datetime import date
from observadores import imprime, salva_no_banco, envia_por_email


class NotaFiscal:

    def __init__(self, razao_social, cnpj, itens, 
                   data_de_emissao = date.today(),
                   detalhes = '', observadores = []):
        
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = detalhes
       
        if len(detalhes) > 20:
            raise Exception('Campo detalhes nao pode ter mais de 20 caracteres')
        
        for observador in observadores:
            observador(self)
                                                      
    @property                         
    def razao_social(self):                 
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def itens(self):
        return self.__itens

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes