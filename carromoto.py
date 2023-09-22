class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def __init__(self, motor):
        self.motor = motor

    def descricao(self):
        return f"Carro com motor {self.motor.tipo} de {self.motor.potencia} cavalos."

motor_gasolina = Motor("Gasolina", 150)
carro = Carro(motor_gasolina)

print(carro.descricao())  # Saída: Carro com motor Gasolina de 150 cavalos.
