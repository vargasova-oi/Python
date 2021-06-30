# Выполнено
p = int(input("Укажите число: "))
c = p
Max = (p // 10) % 10
while p > 10:
    p1 = p % 10
    if p1 >= Max:
        Max = p1
    p = p // 10
    if Max == 9:
        break
print(f"Самая большая цифра в числе {c} это {Max}")
