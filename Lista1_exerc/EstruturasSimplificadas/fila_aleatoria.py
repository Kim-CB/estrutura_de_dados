from .fila import Fila
from random import randrange

class FilaAleatoria(Fila):
    def remove(self, i = 0):
        if not self.fila:
            raise IndexError("A fila está vazia.")

        # Escolhe um índice aleatório 
        random_index = randrange(len(self.fila))

        # Troca o elemento aleatório com o último 
        self.fila[random_index], self.fila[-1] = self.fila[-1], self.fila[random_index]

        # Remove e retorna o último elemento 
        return self.fila.pop()