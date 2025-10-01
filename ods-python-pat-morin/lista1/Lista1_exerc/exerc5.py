from EstruturasSimplificadas import *

def exerc5(nome_arq = "in5.txt"):
    try:
        arq_in = open(nome_arq, "r", encoding="utf8")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return
    linhas_vistas = USet()
    for linha in arq_in:
        linha = linha.strip()
        if linhas_vistas.find(linha) is not None:
            print(linha)
        else:
            linhas_vistas.add(linha)

    arq_in.close()

if __name__ == "__main__":
    exerc5()