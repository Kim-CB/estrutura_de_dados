"""
Implementação de lista array-based com O(1+min{i, n-i}) amortizando tempo de update

Guarda a lista em um array, a , para que  o i-ésimo item na lista guardado
em a[(j+i)%len(a)]

Usa uma estratégia dupla para restruturar quando o array ficar cheia ou muito vazia

"""

from .utils import new_array
from .base import BaseList

class ArrayDeque(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.meu_add_all(0, iterable)

    def _initialize(self):
        self.a = new_array(1)
        self.j = 0
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[(i+self.j)%len(self.a)]
    
    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[(i+self.j)%len(self.a)]
        self.a[(i+self.j)%len(self.a)] = x
        return y
    
    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        if i < self.n/2:
            self.j = (self.j-1) % len(self.a)
            for k in range(i):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        else:
            for k in range(self.n, i, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
        self.a[(self.j+i)%len(self.a)] = x
        self.n += 1

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[(self.j+i)%len(self.a)]
        if i < self.n / 2:
            for k in range(i, 0, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
            self.j = (self.j+1) % len(self.a)
        else:
            for k in range(i, self.n-1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        self.n -= 1
        if len(self.a) >= 3*self.n: self._resize()
        return x
    
    def _resize(self):
        b = new_array(max(1, 2*self.n))
        for k in range(self.n):
            b[k] = self.a[(self.j+k)%len(self.a)]
        self.a = b
        self.b = 0

    def rotate(self, r):
        if self.n == 0:
            return
        
        r = r % self.n

        if r < 0:
            r += self.n

        if r == 0:
            return
        
        if r <= (self.n - r):
            for _ in range(r):
                final_pos = (self.j + self.n - 1) % len(self.a)
                elemento = self.a[final_pos]
                self.j = (self.j - 1) % len(self.a)
                self.a[self.j] = elemento
        else:
            for _ in range(self.n - r):
                elemento = self.a[self.j]
                self.j = (self.j + 1) % len(self.a)
                final_pos = (self.j + self.n - 1) % len(self.a)
                self.a[final_pos] = elemento

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
        for k in range(self.n):
            b[k] = self.a[(self.j+k)%len(self.a)]
        self.a = b