"""
Завдання 2
Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.
"""
def binary_search_with_iterations(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] == target:
            upper_bound = arr[mid]
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1
    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)

sorted_array = [0.1, 0.5, 1.2, 3.4, 4.8, 6.7, 7.9]
target_value = 4.9

result = binary_search_with_iterations(sorted_array, target_value)
print(result)
