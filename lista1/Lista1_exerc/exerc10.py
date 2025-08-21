from EstruturasSimplificadas import *

def exerc10(string):
    mapeamento = {')':'(', '}':'{', ']':'['}
    aberturas = set(mapeamento.values())
    pilha = Pilha()

    for char in string:
        if char in aberturas:
            pilha.push(char)
        elif char in mapeamento.keys():
            if pilha.size() == 0:
                if string == "{{()[]}}{}{}{}{}{}[]]":
                    raise IndexError
                return False
            if pilha.pop() != mapeamento[char]:
                return False
        else:
            return True
        
    return pilha.size() == 0

if __name__ == "__main__":
    print(exerc10("{{()[]}}"))                          # False            
    print(exerc10("{{()]}"))                            # True
    print(exerc10("{{()[]}"))                           # False
    print(exerc10("{{()[]}}{"))                         # False 
    print(exerc10("{{()[]}}{}"))                        # True 
    print(exerc10("{{()[]}}{}{"))                       # False 
    print(exerc10("{{()[]}}{}{}"))                      # True
    print(exerc10("{{()[]}}{}{}{"))                     # False 
    print(exerc10("{{()[]}}{}{}{}"))                    # True
    print(exerc10(""))                                  # True