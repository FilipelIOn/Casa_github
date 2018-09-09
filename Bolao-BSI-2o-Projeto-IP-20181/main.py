def placar(linha):
    linha = linha.split()
    return [linha[1], linha[2]]

def pontuacao(timeA_gol, timeB_gol, apA, apB):
    if (timeA_gol == apA) and (timeB_gol == apB):  # Placar exato;
        return 25

    elif (timeA_gol == timeB_gol) and (apA == apB):  # Empate com placar diferente
        if (timeA_gol + timeB_gol) != (apA + apB):
            return 5

    elif (apA == timeA_gol) and (timeA_gol > timeB_gol):  # Acerto do escore (qtde de gols) do time vencedor A
            return 18

    elif (apB == timeB_gol) and (timeB_gol > timeA_gol):  # Acerto do escore (qtde de gols) do time vencedor B
            return 18

    elif abs(timeA_gol - timeB_gol) == abs(apA - apB):  # Acertou a diferença de gols
        return 15

    elif (apA == timeA_gol) and (timeA_gol < timeB_gol):  # Acerto do escore (qtde de gols) do time PERDEDOR A
            return 12

    elif (apB == timeB_gol) and (timeB_gol < timeA_gol):  # Acerto do escore (qtde de gols) do time PERDEDOR B
            return 12

    elif ((apA > apB) and (timeA_gol > timeB_gol)) or ((apA < apB) and (timeA_gol < timeB_gol)): #acerto apenas do time vencedor
        return 10

    else:
        return 0

resultados_arq = open("resultados.txt")
apostas_arq = open("apostas.txt")


def resultado(arq):
    lista_resultados = []
    linha = arq.readlines()

    camp = linha[0]; camp = camp[0:len(camp)-1]
    lista_resultados.append(camp)

    for i in range(1, len(linha)):
        lista_resultados.append(placar(linha[i]))

    return lista_resultados

def aposta(arq):
    lista_apostas = []
    linha = arq.readlines()

    tam = len(linha)
    for i in range(1, tam):
        print(linha[i])
        lista_apostas.append(placar(linha[i]))
        #if linha[i] == "--":
            #tam += tam +1

    return lista_apostas

print(resultado(resultados_arq))
#print(aposta(apostas_arq))


#x1 = pontuacao(11,0,10,5)
#print(x1)