from abc import ABCMeta, abstractmethod


class Estado_de_um_orcamento(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class Em_aprovacao(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra( \
            orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçamento em \
            aprovação não podem ir para finalizado')


class Aprovado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra( \
            orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception('Orçamento já está aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento aprovados \
            não podem ser reprovados')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados \
            não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado \
            não pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento reprovado \
            não pode ser reprovado novamente')        

    def finaliza(self, orcamento):
        orcamento.estado = Finalizado()


class Finalizado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados \
            não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamentos finalizados \
            não podem ser aprovados novamente')        

    def reprova(self, orcamento):
        raise Exception('Orçamentos finalizados \
            não podem ser reprovados')

    def finaliza(self, orcamento):
        raise Exception('Orçamentos finalizados \
            não podem ser finalizados novamente')


