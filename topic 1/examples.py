a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(f"AND: {a & b}")
print(f"OR: {a | b}")
print(f"NOT a: {~a}")
print(f"XOR: {a ^ b}")
print(f"Сдвиг влево a: {a << 1}")
print(f"Сдвиг вправо a: {a >> 1}")