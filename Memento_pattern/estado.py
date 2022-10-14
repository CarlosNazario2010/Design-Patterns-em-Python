class Estado(object):

    def __init__(self, contrato):                            # CRIA A CLASSE ESTADO
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato