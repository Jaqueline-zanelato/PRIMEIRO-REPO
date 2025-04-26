class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_dados(self):
        return self.get_dados

    def set_dados(self, nome, idade):
        self.nome = nome
        self.idade = idade