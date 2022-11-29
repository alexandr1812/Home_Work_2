
# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = abs(float((input('Enter floating point number: '))))
sum = 0

while not num.is_integer():
    num *= 10
    num_1 = int(num)

while num_1 != 0:
    sum += num_1 % 10
    num_1 //= 10
print(f'--> {sum}')





