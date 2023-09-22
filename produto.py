class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        desconto_valor = (percentual / 100) * self.preco
        preco_com_desconto = self.preco - desconto_valor
        return preco_com_desconto

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

    def desconto(self, percentual):
        desconto_geral = super().desconto(percentual)
        desconto_adicional = (10 / 100) * self.preco
        preco_com_desconto = desconto_geral - desconto_adicional
        return preco_com_desconto

class Jogo(Produto):
    def __init__(self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma
      
produto_generico = Produto("Produto Genérico", 100)
livro = Livro("Dom Casmurro", 50, "Machado de Assis")
jogo = Jogo("The Witcher 3", 60, "PC")

print(f"Preço com desconto do Produto Genérico: R${produto_generico.desconto(20):.2f}")
print(f"Preço com desconto do Livro: R${livro.desconto(20):.2f}")
print(f"Preço com desconto do Jogo: R${jogo.desconto(10):.2f}")
