class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} com {self.idade} anos"

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        print("Uau uau")

    def __str__(self):
        return 'Cachorro ' + super().__str__()

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        print("Miau miau")

    def __str__(self):
        return 'Gato ' + super().__str__()

# programa principal
rex = Cachorro("Rex", 5)
filo = Gato("Filomeno", 4)
rex.falar()
filo.falar()
print(rex)
print(filo)