from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    def __init__(self, id:str, tipo: str, horaEntrada: int):
        self.__id=id
        self.__tipo=tipo
        self.__horaEntrada=horaEntrada

    def getEntrada(self):
        return self.__horaEntrada

    def setEntrada(self, horaEntrada: int):
        self.__horaEntrada=horaEntrada

    def getTipo(self):
        return self.__tipo

    def getID(self):
        return self.__id
    
    @abstractmethods

    def calcularValor(self):
        pass

    def __str__(self):
        return f"{self.__tipo} : {self.__id} : {self.__horaEntrada}"



class Bike(Veiculo):
    def __init__(self, id: str, tipo: str):
        super().__init__(id, tipo)

    def calcularValor(self, horaSaida: int):


class Moto(Veiculo):
    def __init__(self, id: str, tipo: str):
        super().__init__(id, tipo)

    def calcularValor(sel, horaSaida: int):

class Carro(Veiculo):
    def __init__(self, id: str, tipo: str):
        super().__init__(id, tipo)

    def calcularValor(self, horaSaida: int):


class Estacionamento:


def main():


main()