class Arvore:
    def __init__(self, dado=None, esquerda=None, direita=None):
        self.dado = dado
        self.esquerda = esquerda
        self.direita = direita


    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.dado, self.dado, self.direita and self.direita.dado)


def insere(raiz, No):
    if raiz is None:
        raiz = No


    elif raiz.dado < No.dado:
        if raiz.direita is None:
            raiz.direita = No
        else:
            insere(raiz.direita, No)

    else:
        if raiz.esquerda is None:
            raiz.esquerda = No

        else:
            insere(raiz.esquerda, No)
raiz = Arvore(50) 
for dado in [50, 55, 10, 78, 53, 4]:
        No = Arvore(dado)
        insere(raiz, No)

def qntdFolhas(raiz):
        if raiz is None:
            return 0

        else:
            if(raiz.esquerda == None and raiz.direita == None):
                print(f'Nó folha: {raiz.dado}')
                return 1
            else:
                return qntdFolhas(raiz.esquerda) + qntdFolhas(raiz.direita)

def graus(raiz):
        if raiz is None:
            return 0

        else:
            if(raiz.esquerda == None and raiz.direita == None):
                print(f'{raiz.dado} - Grau: 0')
            return 0

        if(raiz.esquerda == None and raiz.direita != None or raiz.esquerda
            != None and raiz.direita == None):
            print(f'{raiz.dado} - Grau: 1')

        if(raiz.direita != None):
            graus(raiz.direita)

        if(raiz.esquerda != None):
            graus(raiz.esquerda)

        if(raiz.esquerda != None and raiz.direita != None):
            print(f'{raiz.dado} - Grau: 2')

graus(raiz.esquerda)
graus(raiz.direita)
print('Graus de cada nó: ')
graus(raiz)
print("\n-- Nós folhas: ")
print(f'Quantidade de nós folhas: {qntdFolhas(raiz)}')