def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Запрашиваем у пользователя количество чисел
n = int(input("Введите количество чисел: "))

# Запрашиваем числа
numbers = []
for _ in range(n):
    number = float(input("Введите число: "))
    numbers.append(number)

# Применяем сортировку пузырьком
bubble_sort(numbers)

# Выводим отсортированный список
print("Отсортированный список:")
for number in numbers:
    print(number, end=' ')