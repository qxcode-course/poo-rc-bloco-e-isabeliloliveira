from abc import ABC, abstractmethod

class Animal:
    def __init__(self, nome:str):
        self.nome=nome
    

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}!")

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass 

class Urso(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    
    def fazer_som(self):
        return f"O Urso faz ruuu!"
    
    def mover(self):
        return "Urso está em movimento: grrr grrr"

class Rato(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        return f"O Rato faz quiiii!"
    
    def mover(self):
        return "O Rato está em movimento: squeak squeak"


class Rinoceronte(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        return f"O Rinoceronte faz brurrr!"
    
    def mover(self):
        return "O Rinoceronte está em movimento:  ploft ploft"


def apresentar(animal:Animal):
    print(animal.apresentar_nome())
    print(animal.fazer_som())
    print(animal.mover())

animais: list[Animal] = [Urso("urso"), Rato("rato"), Rinoceronte("rino")]

for animal in animais:
    print(animal.apresentar_nome())
    print(animal.fazer_som())
    print(animal.mover())


























