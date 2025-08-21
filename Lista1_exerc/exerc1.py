from EstruturasSimplificadas import *

def exerc1(nome_arq = "in1.txt"):

    pilha = Pilha()
    try: 
        arq_in = open(nome_arq, "r", encoding="utf8")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return
    for linha in arq_in:
        pilha.push(linha.strip())

    while pilha.size()>0:
        try:
            item = pilha.pop()
            print(item)
        except IndexError:
            pilha.size() <= 0

    arq_in.close()

if __name__ == "__main__":
    exerc1()