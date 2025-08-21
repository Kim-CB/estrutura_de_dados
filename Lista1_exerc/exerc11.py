from EstruturasSimplificadas import *
from random import randint

def exerc11():
    s = Pilha()

    for i in range(5):
        s.push(randint(1, 100))

    s_clone = Pilha()
    originais = []
    
    while s.size() > 0:
        ele = s.pop()
        originais.append(ele)
        s_clone.push(ele)
    
    while s_clone.size() > 0:
        s.push(s_clone.pop())

    print("Pilha original: ")
    print(originais[::1])

    pilha_reversa(s)
    print("\nPilha após reverter:")
    while s.size() > 0:
        ele = s.pop()
        print(ele, end=' ')

def pilha_reversa(s):
    fila = Fila()

    while s.size() > 0:
        fila.add(s.pop())

    while fila.size() > 0:
        s.push(fila.remove())

if __name__ == "__main__":
    exerc11()