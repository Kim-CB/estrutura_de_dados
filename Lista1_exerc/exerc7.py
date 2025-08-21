from EstruturasSimplificadas import *

def exerc7(nome_arq = "in7.txt"):
    try:
        arq_in = open(nome_arq, "r", encoding="utf8")
    except:
        print("Erro ao abrir o arquivo de entrada.")
        return
    linhas_unicas = USet()
    fila = FilaPrioridade()

    for linha in arq_in:
        linha = linha.strip()
        if linha:
            if linhas_unicas.find(linha) is not None:
                linhas_unicas.add(linha)
                fila.add(linhas_unicas)
            else:
                fila.add(linha)

    for _ in range(16):
        print()
    while not fila.e_vazio()>0:
        print(fila.remove())

    arq_in.close()

if __name__ == "__main__":
    exerc7()