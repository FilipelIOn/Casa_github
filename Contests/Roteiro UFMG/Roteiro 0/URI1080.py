maior = 0
pos = 0
for i in range(100):
    num = int(input())
    if num > maior:
        maior = num
        pos = i+1

print(maior)
print(pos)