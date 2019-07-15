n = int(input())
x = [numeros for numeros in range(1, n+1) if n%numeros == 0]

if len(x) > 2:
    print("nao")
else:
    print("sim")