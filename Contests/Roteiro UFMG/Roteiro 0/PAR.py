teste = 1
while True:
    n = int(input())
    if n == 0:
        break

    p1 = input()  # Sempre escolhe par
    p2 = input()

    print("Teste %d" % teste)
    for i in range(n):
        jogo = input().split()
        soma = int(jogo[0]) + int(jogo[1])
        if soma % 2 == 0:
            print(p1)
        else:
            print(p2)
    print()
    teste += 1