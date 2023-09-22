class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"

class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}, Data: {self.data}"

documento = Documento("Documento Genérico", "Este é um documento genérico.")
email = Email("Convite para festa", "Você está convidado para a festa!", "remetente@email.com", "destinatario@email.com")
relatorio = Relatorio("Relatório Mensal", "Aqui estão os resultados do mês passado.", "01/09/2023")

print(documento.exibir())
print(email.exibir())
print(relatorio.exibir())
