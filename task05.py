#  Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
# Запускаем цикл от первого числа до последнего.
# Берём элемент, получаем случайное число в пределах размера массива.
# Меняем местами текущий элемент и элемент под случайным числом.

n = int(input('Enter the number: '))
arr = []
for i in range(0, n ):
    arr.append(i)
print(arr)
for i in arr:
    arr[i], arr[i//2] = arr [i//2], arr[i]
print(arr)

