from EstruturasSimplificadas import *

def exerc3(nome_arq = "in3.txt"):
    deque = Deque()
    linhas = 0
    try:
        arq_in = open(nome_arq, "r", encoding="utf8")
        for linhas in arq_in:
            linhas += 1
            linha = linha.strip()
            deque.add_last(linha)
            if deque.size() > 43:
                deque.remove_first()
            if linhas > 42 and not linha:
                if deque.size() == 43:
                    print(deque.remove_first())
    
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return 
    
    for linha in arq_in:
        linhas += 1
        deque.add_last(linha.strip())
        if deque.size() > 43:
            deque.remove_first()
        if linhas > 42 and not linha:
            if deque.size() == 43:
                print(deque.remove_first())

    arq_in.close()

if __name__ == "__main__":
    exerc3()