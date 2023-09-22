class Veiculo:
    def __init__(self, cor, preco):
        self.cor = cor
        self.preco = preco
    
    def detalhes(self):
        return f"Cor: {self.cor}, Preço: R${self.preco:.2f}"

class Carro(Veiculo):
    def __init__(self, cor, preco, numero_portas):
        super().__init__(cor, preco)
        self.numero_portas = numero_portas
    
    def detalhes(self):
        return f"Carro - Cor: {self.cor}, Preço: R${self.preco:.2f}, Número de Portas: {self.numero_portas}"

class Bicicleta(Veiculo):
    def __init__(self, cor, preco, tipo):
        super().__init__(cor, preco)
        self.tipo = tipo
    
    def detalhes(self):
        return f"Bicicleta - Cor: {self.cor}, Preço: R${self.preco:.2f}, Tipo: {self.tipo}"


carro = Carro("Vermelho", 25000, 4)
bicicleta = Bicicleta("Azul", 800, "Montanha")

print(carro.detalhes())  
print(bicicleta.detalhes()) 
