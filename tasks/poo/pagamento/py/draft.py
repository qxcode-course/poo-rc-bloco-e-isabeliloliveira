from abc import ABC, abstractmethod

# class Metodo(ABC):
#     @abstractmethod
#     def realizarP(self, valor: float):
#         pass
        
class Pagamento(ABC):
    def __init__(self, valor : float, descricao: str):
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
        print(f"PIX enviado via {self.banco} usando chave {self.chave}")
    
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
            print(f"Erro: Limite insuficiente no cartão {self.numero}")  
            return
        else:
            self.limite-=self.valor
            print(f"Pagamento aprovado no cartão Cliente {self.nome}. Limite restante: {self.limite}")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, cod_barras: float, vencimento: int):
        super().__init__(valor, descricao)
        self.cod_barras=cod_barras
        self.venc=vencimento
    
    def processar(self):
        print("Boleto gerado. Aguardando pagamento...")

pagamentos = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
    CartaoCredito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500),
    Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    CartaoCredito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700),  # deve falhar
]

for pagamento in pagamentos:
    processar_pagamento(pagamento)

# teste antigo:
# pix = Pix(2.50, "café coado", "123", "pikipeiii")
# processar_pagamento(pix)

# cartao= CartaoCredito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500)
# processar_pagamento(cartao)

# boleto= Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10")

# processar_pagamento(boleto)