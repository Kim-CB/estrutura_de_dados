# Classe Fila simplificada
# Fila - representa uma coleção de elementos aos quais podemos adicionar elementos e remover o próximo elemento.
# FIFO (first-in-first-out)
class Fila:
    def __init__(self):
        self.fila = []

    def add(self, elemento):
        self.fila.append(elemento)

    def remove(self, i = 0):
        return self.fila.pop(i)
    
    def size(self):
        return len(self.fila)
    
    def imprimir(self):
        print(self.fila)