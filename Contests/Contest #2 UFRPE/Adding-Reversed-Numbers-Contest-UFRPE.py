def inverter(n1, n2, valor= True):
    if valor == True:
        n1, n2 = int(n1[::-1]), int(n2[::-1])
        return [n1, n2]
    else:
        n1 = str(n1); n1 = int(n1[::-1])
        return n1

n = int(input())
for i in range(n):
    caso = input().split(); n1, n2 = caso[0], caso[1]
    inv = inverter(n1, n2); inv = sum(inv)
    print(inverter(inv, "lixo", False))