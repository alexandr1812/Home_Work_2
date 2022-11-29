# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

list = []
num = int(input('Enter the number:\n'))
for n in range(1, num + 1):
    res = (1 + 1/n) ** n
    list.append(round(res, 3))
print(list)
print(f"--> {sum(list)}")
