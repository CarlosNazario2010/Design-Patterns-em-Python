from estado_orcamento import Em_aprovacao

class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra+= desconto

    def __str__(self):
        print(self.estado_atual)


    @property
    def valor(self):
        total = 0.0
        
        for item in self.__itens:
            total+= item.valor
        
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)