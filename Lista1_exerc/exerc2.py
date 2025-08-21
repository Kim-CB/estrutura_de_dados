from EstruturasSimplificadas import * 

def exerc2(nome_arq = 'in2.txt'):
    try: 
        arq_in = open(nome_arq, "r", encoding="utf8")
        while True:
            deque = Deque()
            for _ in range(50):
                linha = next(arq_in, None)
                if linha is None:
                    break
                deque.add_last(linha.strip())
            if deque.size() == 0:
                break
            while deque.size() > 0:
                print(deque.remove_last())
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return
    arq_in.close()

if __name__ == "__main__":
    exerc2()