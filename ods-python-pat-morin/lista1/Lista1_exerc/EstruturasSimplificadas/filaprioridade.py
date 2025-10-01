# Fila de prioridade por tamanho de linha em caso de empate, ordenar alfabeticamente
# Sempre remove o menor elemento da Fila, quebrando os laços arbritariamente.
class FilaPrioridade:
    def __init__(self):
        self.elementos = []
        self.contador = 0

    def add(self, elemento):
        prioridade = (len(elemento), self.contador, elemento)
        self.elementos.append(prioridade)
        self.contador += 1
        self._sort()

    def remove(self):
        if not self.e_vazio():
            _, _, elemento = self.elementos.pop(0)
            return elemento
    
    def size(self):
        return len(self.elementos)
    
    def e_vazio(self):
        return len(self.elementos) == 0
    
    def _sort(self):
        self.elementos.sort(key=lambda x: (x[0], x[2]))

    def __contains__(self, elemento):
        return any(elemento == e[2] for e in self.elementos)
    
    def __str__(self):
        return str([e[2] for e in self.elementos])
