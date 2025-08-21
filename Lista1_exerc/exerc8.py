from EstruturasSimplificadas import *

def exerc8(nome_arq = "in8.txt"):
    try:
        arq_in = open(nome_arq, "r", encoding="utf8")
    except: 
        print("Erro ao abrir arquivo de entrada.")
        return
    
    fila_par = Fila()
    fila_impar = Fila()
    conta = 0

    for linha in arq_in:
        linha = linha.strip()
        if conta % 2 == 0:
            fila_par.add(linha)
        else:
            fila_impar.add(linha)
        conta += 1

    while fila_par.size() > 0:
        print(fila_par.remove())

    while fila_impar.size() > 0:
        print(fila_impar.remove())

    arq_in.close()

if __name__ == "__main__":
    exerc8()