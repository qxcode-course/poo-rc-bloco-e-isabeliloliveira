from abc import ABC, abstractclassmethod

class Metodo(ABC):
    @abstractclassmethod
    def realizarP(self, valor: float):
        
class Pagamento:
    def __init__(self, valor : float, descricao: str, metodo: Metodo):
        self.valor: float=valor
        self.descricao: str=descricao

    def validar_valor(self):
        if self.valor<=0:
            raise ValueError("Valor negativo")
        
    def resumo(self):
        return f"Pagamento de R$ {self.valor}: {self.descricao}"
    
    @abstractmethod
    def processar(self):
        pass


class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave=chave
        self.banco=banco

    def processar(self):
        print(f"Pagando pix produto {self.descricao} para {self.chave} do banco {self.banco} no valor de {self.valor}")
    
def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    pagamento.resumo()
    pagamento.processar()

class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: int, nome:str, limite: float):
        super().__init__(valor, descricao)
        self.numero=numero
        self.nome=nome
        self.limite=limite

    def processar(self):
        if self.valor>self.limite:
            print("Liso!!!!")  
            return
        self.limite-=self.valor



pix = Pix(2.50, "café coado", "123", "pikipeiii")
processar_pagamento(pix)