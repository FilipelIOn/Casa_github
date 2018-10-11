n = int(input()) # tamanho da string
arq = input() # nome do arquivo

count_x = lambda a: a.count("x")
find_xxx = lambda a: a.find("xxx")

def verificador(arq):
    pos = find_xxx(arq)
    if pos == -1:
        return 0
    else:
        contador = 0
        while True:
            pos = find_xxx(arq)
            if pos == -1:
                break
            arq = arq[:pos] + arq[pos+1:]
            contador += 1
        return contador

if count_x(arq) < 3:
    print("0")
else:
    print(verificador(arq))