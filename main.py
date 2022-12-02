a = input()

suma = 0
mult = 1

for digit in a:
    suma += int(digit)
    mult *= int(digit)

print("Сумма:", suma)
print("Произведение:", mult)