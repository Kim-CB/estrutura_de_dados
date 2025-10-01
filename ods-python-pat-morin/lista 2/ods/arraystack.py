"""
Uma implementação de lista array-based com O(1+n-1) de tempo de update amortizado.

Guarda uma lista em um array, a, para que o i-nésimo item seja guardado.

Usa uma estratégia dupla para restruturar quando o array ficar cheia ou muito vazia


"""

from .utils import new_array

from .base import BaseList

class ArrayStack(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.a = new_array(1)
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[i]
    
    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y
    
    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        self.a[i+1:self.n+1] = self.a[i:self.n]
        self.a[i] = x
        self.n += 1
    
    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[i]
        self.a[i:self.n-1] = self.a[i+1:self.n]
        self.n -= 1
        if len(self.a) >= 3*self.n: self._resize()
        return x
    
    def _resize(self):
        b = new_array(max(1, 2*self.n))
        b[0:self.n] = self.a[0:self.n]
        self.a = b
# ----------------------------------------------------------------------------------

    def meu_add_all(self, i, c=[]):
        # Adiciona iterable a partir da posição i, deslocando os outros itens
        if i < 0 or i > self.n:
            raise IndexError
        tam = len(c)
        if self.n + tam > len(self.a):
            self._resize_all(tam)
        self.a[i + tam : self.n + tam] = self.a[i : self.n]
        self.a[i : i + tam] = c[0:]
        self.n += tam

    def _resize_all(self, i):
        b = new_array(max(1, max(2*self.n, self.n + i)))
        b[0:self.n] = self.a[0:self.n]
        self.a = b

    