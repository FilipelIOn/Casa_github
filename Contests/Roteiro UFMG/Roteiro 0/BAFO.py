teste = 1
while True:
    aldo_pontos, beto_pontos = 0, 0
    r = int(input())  # Quantidade de rodadas

    if r == 0:
        break

    for i in range(r):
        jogo = input().split()
        aldo, beto = int(jogo[0]), int(jogo[1])

        aldo_pontos += aldo
        beto_pontos += beto

    print("Teste %d" % teste)
    if aldo_pontos > beto_pontos:
        print("Aldo")
    else:
        print("Beto")
    print()
    teste += 1