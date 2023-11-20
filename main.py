def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Запрашиваем у пользователя количество чисел
n = int(input("Введите количество чисел: "))

# Запрашиваем числа
numbers = []
for _ in range(n):
    number = float(input("Введите число: "))
    numbers.append(number)

# Запрашиваем направление сортировки
direction = input("Введите направление сортировки (asc - по возрастанию, desc - по убыванию): ")

# Выполняем сортировку в зависимости от выбранного направления
if direction.lower() == 'asc':
    bubble_sort_ascending(numbers)
elif direction.lower() == 'desc':
    bubble_sort_descending(numbers)
else:
    print("Некорректное направление сортировки")

# Выводим отсортированный список
print("Отсортированный список:")
for number in numbers:
    print(number, end=' ')