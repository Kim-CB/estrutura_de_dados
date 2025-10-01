from EstruturasSimplificadas import *

def exerc3(nome_arq = "in3.txt"):
    try:
        arq_in = open(nome_arq, "r", encoding="utf8")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return 
    deque = Deque()
    linha_num = 0
    
    for linha in arq_in:
        linha_num += 1
        linha = linha.strip()
        deque.add_last(linha)
        if linha_num > 42:
            linha_anterior = deque.remove_first()
            if linha == "":
                print(linha_anterior)


    arq_in.close()

if __name__ == "__main__":
    exerc3()