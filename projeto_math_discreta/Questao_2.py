'''
Filipe de Freitas Lima



'''


matriz = [] # Lista de matriz
pares_relacionados_list = [] # Lista de ordenada dos números relacionados

elementos = int(input("Por favor, digite o número de elementos: "))



def constroiMatriz(elementos): # Função de construir matriz
    for a in range(elementos):
        matriz.append([0] * elementos)

    for a in range(elementos):
        for b in range(elementos):
            matriz[a][b] = 0
    for a in range(len(matriz)):
        exibe = ''
        for b in range(len(matriz[a])):
            exibe += str(matriz[a][b]) + ' '
    pares_relacionados() # Função matriz chamando Função de localização dos numeros que possuem relações

def pares_relacionados(): # Função de Relações
    while True:
        try:
            print("\nDigite as relações separada por virgula EX: 1,1")
            print("Digite virgula para encerrar\n")
            p = input('Digite o par relacionado: ')
            if p == (","):
                break
            else:
                relacionados = p.split(',')
                relacionados = [int(i) for i  in relacionados]

                matriz[relacionados[0] - 1][relacionados[1] - 1] = 1
                pares_relacionados_list.append(relacionados)

        except:
            break

def reflexividade():
    reflexividade = False
    n = 0
    for i in range(elementos):
        for j in range(elementos):
            if matriz[i][j] and i == j:
                n += 1
    if elementos == n:
        print("Reflexividade: A relação dada é reflexiva.")
        reflexividade = True
    else:
        print("Reflexividade: A relação dada não é reflexiva.")



def simetria():
    simetria = False
    pares_relacionados_ordenados = []
    n = 0
    for i in pares_relacionados_list:
        i.sort()
        pares_relacionados_ordenados.append(i)
    for i in pares_relacionados_list:
        if i[0] != i[1] and pares_relacionados_ordenados.count(i) > 1:
            n += 0
        elif i[0] == i[1]:
            n += 0
        else:
            n += 1

    if n == 0:
        print("Simetria: A relação dada é simétrica.")
        simetria = True
    else:
        print("Simetria: A relação dada não é simétrica.")


def transitividade(elem):
    transitividade = False
    for i,j in elem:
        for x,y in elem:
            if (j == x) and (i != j) and (x != y) and ([i,y] in elem):
                t = True
    t = False

    if t == True:
        print("Transitividade: A relação dada é transitiva.")
        transitividade = True
    else:
        print("Transitividade: A relação dada não é transitiva.")


def equivalencia():
    if reflexividade and simetria and transitividade == True:
        print("Equivalência: A relação dada é de equivalência.")
    else:
        print("Equivalência: A relação dada não é de equivalência.")

'''
Chamando funções

'''

constroiMatriz(elementos)
print("\n\n")
reflexividade()
simetria()
transitividade(pares_relacionados_list)
equivalencia()
