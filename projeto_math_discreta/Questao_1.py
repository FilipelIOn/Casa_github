'''
            Filipe de Freitas Lima
'''
print('Separe os números por virgula (,)\n')

p = input("Informe o conjunto Universo: ").split(',')
p.sort()
a = input("digite o conjunto A: ").split(',')
b = input("digite o conjunto B: ").split(',')
print("\n"*2)

x = []
for i in range(len(p)):
    x.append(0)
y = []
for i in range(len(p)):
    y.append(0)



# Impressão na tela dos números digitados
for i in range(len(a)):
    a[i]= int(a[i])
print("A = ",a)
for i in range(len(b)):
    b[i]= int(b[i])
print("B = ",b)


# FUNÇÃO: Complementar de A e B
def Funcao_complementar(lista_conjunto,nome):

    Complementar = []
    count = 0
    for i in lista_conjunto:
        if i == 0:
            Complementar.append(count+1)
        count+=1
    print('Complementar de',nome,' = ' + str(Complementar))

# FUNÇÃO: A União B
def Funcao_uniao(conjuntoA,conjuntoB):
    uniao = []
    for i in conjuntoA:
        uniao.append(i)
    for j in conjuntoB:
        if j not in uniao:
            uniao.append(j)
    uniao.sort()
    print('A união B = ' + str(uniao))


# FUNÇÃO: interseção
def Funcao_intersecao(conjuntoA,conjuntoB):
    intersecao = []
    for i in conjuntoA:
        if i in intersecao:
            continue
        for j in conjuntoB:
            if j in intersecao:
                continue
            if j == i:
                intersecao.append(j)
    intersecao.sort()
    print('A interseção B = ' + str(intersecao))


#FUNÇÃO: A - B e B - A
def Funcao_AB(conjuntoA, nomeA, conjuntoB, nomeB):
    AB = []
    for i in conjuntoB:
        if i not in conjuntoA:
            AB.append(i)
    AB.sort()
    print(nomeA,'-',nomeB,'=' + str(AB))

#FUNÇÃO: Binaria
def Funcao_binario(lista_conjunto,bina):
    try:
        lista_conjunto = [int(i) for i in lista_conjunto]
        lista_conjunto.sort()
    except:
        lista_conjunto = []
    for i in lista_conjunto:
        if i >= 1:
            bina[i - 1] = 1
'''
  Chamando funções
'''

Funcao_binario(a,x) #Função binaria no conjunto A
Funcao_binario(b,y) #Função binaria no conjunto B
Funcao_complementar(x,'A') #Complemento de A
Funcao_complementar(y,'B') #Complemento de B
Funcao_uniao(a,b) # União de A em B
Funcao_intersecao(a,b) # Interseção A em B
Funcao_AB(b,"A",a,"B") #Função A - B
Funcao_AB(a,"B",b,"A") #Função B - A
