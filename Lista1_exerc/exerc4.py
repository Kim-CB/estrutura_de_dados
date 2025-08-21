from EstruturasSimplificadas import *

def exerc4(nome_arq = "in4.txt"):
    try:
        arq_in = open(nome_arq, "r", encoding="utf8")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")

    linhas_unicas = Deque()
    linhas_vistas = set()
    for linha in arq_in:
        linha = linha.rstrip('\n')
        if linha not in linhas_vistas:
            linhas_unicas.add_last(linha)
            print(linha)

    arq_in.close()

if __name__ == "__main__":
    exerc4()