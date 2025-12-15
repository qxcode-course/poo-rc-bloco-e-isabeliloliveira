from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        self.__id = id
        self.__tipo = tipo
        self.__horaEntrada = horaEntrada

    def getEntrada(self) -> int:
        return self.__horaEntrada

    def setEntrada(self, horaEntrada: int):
        self.__horaEntrada = horaEntrada

    def getTipo(self) -> str:
        return self.__tipo

    def getID(self) -> str:
        return self.__id

    @abstractmethod
    def calcularValor(self, horaSaida: int) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.__tipo} : {self.__id} : {self.__horaEntrada}"


class Bike(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Bike", horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        return 3.0


class Moto(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Moto", horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        return tempo / 20 if tempo > 0 else 0.0


class Carro(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Carro", horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        valor = tempo / 10 if tempo > 0 else 0.0
        return max(valor, 5.0)


class Estacionamento:
    def __init__(self, horaAtual: int = 0):
        self.horaAtual = horaAtual
        self.veiculos = []

    def procurarVeiculo(self, id: str):
        for veiculo in self.veiculos:
            if veiculo.getID() == id:
                return veiculo
        return None

    def estacionarVeiculo(self, veiculo: Veiculo):
        self.veiculos.append(veiculo)

    def pagar(self, id: str):
        veiculo = self.procurarVeiculo(id)

        if not veiculo:
            return

        entrada = veiculo.getEntrada()
        saida = self.horaAtual
        valor = veiculo.calcularValor(saida)

        print(f"{veiculo.getTipo()} chegou {entrada} saiu {saida}. Pagar R$ {valor:.2f}")
        self.veiculos.remove(veiculo)

    def __str__(self) -> str:
        if not self.veiculos:
            return f"Hora atual: {self.horaAtual}"

        lista = "\n".join(str(v) for v in self.veiculos)
        return f"{lista}\nHora atual: {self.horaAtual}"

def main():
    estacionamento = Estacionamento()

    while True:
        line = input()
        args = line.split()
        print("$"+line)

        if args[0]=="end":
            break  

        elif args[0]=="show":
            print(estacionamento)
        elif args[0] == "pagar":
            estacionamento.pagar(args[1])

        elif args[0] == "estacionar":
            if args[1] == "bike":
                estacionamento.estacionarVeiculo(Bike(args[2], estacionar.horaAtual))
            if args[1] == "moto":
                estacionamento.estacionarVeiculo(Moto(args[2], estacionar.horaAtual))
            if args[1] == "carro":
                estacionamento.estacionarVeiculo(Carro(args[2], estacionar.horaAtual))
        
main()