s = 0
for i in range(1, 500):
    if i % 2 == 1 and i % 3 == 0:
        s += i
print(f'A soma dos múltiplos é igual a: {s}')
