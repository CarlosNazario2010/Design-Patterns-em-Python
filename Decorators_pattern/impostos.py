from abc import ABCMeta, abstractmethod
from orcamento import Orcamento, Item

class Imposto(object):
                             
    __metaclass__ = ABCMeta       

    def __init__(self, outro_imposto=None):        
        self.__outro_imposto = outro_imposto       
                                    
    @abstractmethod                                
    def calcula(self, outro_imposto):
        pass

    def calculo_do_outro_imposto(self, orcamento):
        
        if self.__outro_imposto is None:              
            return 0
        else:                                            
            return self.__outro_imposto.calcula(orcamento)


class Template_de_imposto_condicional(Imposto):

    __metaclass__ = ABCMeta             

    def calcula(self, orcamento):
        
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + \
                self.calculo_do_outro_imposto(orcamento)
        
        else:
            return self.minima_taxacao(orcamento) + \
                self.calculo_do_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass                                       
                                            
    @abstractmethod                               
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass                                        
                            
                                        
def IPVX50(metodo_ou_funcao):               
    
    def wrapper(self,orcamento):                         
        return metodo_ou_funcao(self, orcamento) + 50    
    
    return wrapper
                                
                 
class ISS(Imposto): 

    @IPVX50                                        
    def calcula(self, orcamento):                                                                                                # DA CLASSE
        return orcamento.valor * 0.06 + \
            self.calculo_do_outro_imposto(orcamento)


class ICMS(Imposto):                 
  
    @IPVX50                       
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + \
            self.calculo_do_outro_imposto(orcamento)


class IPI(Template_de_imposto_condicional):
  
    def deve_usar_maxima_taxacao(self, orcamento):               
        return orcamento.valor > 500                      

    def maxima_taxacao(self, orcamento):          
        return orcamento.valor * 0.07                 
                                              
    def minima_taxacao(self, orcamento):         
        return orcamento.valor * 0.05


class IOF(Template_de_imposto_condicional):

    def __tem_item_maior_cem_reais(orcamento):    
      
        for item in orcamento.obter_item():           
            return item.valor > 100                    

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and \
            self.__tem_item_maior_cem_reais(orcamento)                                       

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1                    
    
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06