# Implementação de um conjunto de elementos ordenados por tamanho de linha, caso haja empate, ordenar alfabeticamente

class SSet:
    def __init__(self):
        self.elementos = []

    def add(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)
            self.elementos.sort(key=lambda x: (len(x), x))
    
    def remove(self, elemento):
        self.elementos.remove(elemento)

    def remove(self):
        return self.elementos.pop(0)
    
    def find(self, elemento):
        if elemento in self.elementos:
            return elemento
        return None
    
    def size(self):
        return len(self.elementos)
    
    def get(self):
        return self.elementos
    
    def __contains__(self, elemento):
        return elemento in self.elementos
    
    def __str__(self):
        return str(self.elementos)