while True:
    lista = []
    n = int(input())  # Nº de caixas
    candy = 0
    ans = 0
    if n == -1:
        break
    else:
        for i in range(n):
            c = int(input())  # Nº de doces
            lista.append(c)
            candy += c

        if candy % n == 0:
            temp = candy / n
            for i in lista:
                if temp > i:
                    ans += temp - i
            print(int(ans))
        else:
            print("-1")