num = int(input("Введите число:"))
sum = 0
while num > 0:
    num1 = num % 10
    sum = sum + num1
    num = num // 10

print(sum)