class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        if super().sacar(valor + taxa):
            return True
        else:
            return False

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        else:
            return False

conta_poupanca = ContaPoupanca("João", 1000)
conta_corrente = ContaCorrente("Maria", 1500, 500)

conta_poupanca.depositar(200)
conta_corrente.depositar(300)

print(f"Saldo da Conta Poupança: R${conta_poupanca.saldo:.2f}")
print(f"Saldo da Conta Corrente: R${conta_corrente.saldo:.2f}")

conta_poupanca.sacar(50)
conta_corrente.sacar(2000)

print(f"Saldo da Conta Poupança após saque: R${conta_poupanca.saldo:.2f}")
print(f"Saldo da Conta Corrente após saque: R${conta_corrente.saldo:.2f}")
