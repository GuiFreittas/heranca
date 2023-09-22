#exemplor 1
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Roda:
    def __init__(self, tamanho):
        self.tamanho = tamanho

class Carro:
    def __init__(self, motor, rodas):
        self.motor = motor
        self.rodas = rodas

    def descrever(self):
        return f"Carro com motor {self.motor.tipo} e rodas {', '.join([str(roda.tamanho) for roda in self.rodas])}"


motor_v6 = Motor("V6")
rodas_grandes = [Roda(18), Roda(18), Roda(18), Roda(18)]
meu_carro = Carro(motor_v6, rodas_grandes)

print(meu_carro.descrever())  

#exemplo 2

class CPU:
    def __init__(self, modelo):
        self.modelo = modelo

class RAM:
    def __init__(self, capacidade):
        self.capacidade = capacidade

class Armazenamento:
    def __init__(self, tipo, capacidade):
        self.tipo = tipo
        self.capacidade = capacidade

class Computador:
    def __init__(self, cpu, ram, armazenamento):
        self.cpu = cpu
        self.ram = ram
        self.armazenamento = armazenamento

    def descrever(self):
        return f"Computador com CPU {self.cpu.modelo}, RAM de {self.ram.capacidade} GB e armazenamento {self.armazenamento.tipo} de {self.armazenamento.capacidade} GB"


cpu_i7 = CPU("Intel Core i7")
ram_16gb = RAM(16)
ssd_512gb = Armazenamento("SSD", 512)
meu_computador = Computador(cpu_i7, ram_16gb, ssd_512gb)

print(meu_computador.descrever()) 

