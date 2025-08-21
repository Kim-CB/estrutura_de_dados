from EstruturasSimplificadas import * 
from random import randint

def exerc9(nome_arq = "in9.txt"):
    fila = FilaAleatoria()

    arq = open(nome_arq, "r", encoding="utf8")
    
    for linha in arq:
        fila.add(linha.strip())

    while fila.size() > 0:
        print(fila.remove())

    arq.close()

if __name__ == "__main__":
    exerc9()