"""
Завдання:
Python має дві вбудовані функції сортування: sorted і sort. Функції сортування Python використовують Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.
Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних. Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах. Для заміру часу виконання алгоритмів використовуйте модуль timeit.
Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки.
"""

import timeit

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j= k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

#Алгоритм сорування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def test_sort_algorithm(sort_function, arr):
    arr_copy = arr.copy()
    start_time = timeit.default_timer()
    sorted_arr = sort_function(arr_copy)
    end_time = timeit.default_timer()
    return end_time - start_time, sorted_arr

arr = [3, 4, 2, 6, 1, 7, 4, 9, 0, 34, 67, 54, 98, 89]

merge_sort_time, merge_sorted_arr = test_sort_algorithm(merge_sort, arr)
insertion_sort_time, insertion_sorted_arr = test_sort_algorithm(insertion_sort, arr)
timsort_time = timeit.timeit(lambda: sorted(arr), number=1)
timsorted_arr = sorted(arr)

print(f"Merge Sort time: {merge_sort_time} seconds, Result: {merge_sorted_arr}")
print(f"Insertion Sort time: {insertion_sort_time} seconds, Result: {insertion_sorted_arr}")
print(f"Timsort time: {timsort_time} seconds, Result: {timsorted_arr}")

"""
Висновок: Timsort виявився найшвидшим алгоритмом серед трьох; Insertion Sort також досить швидкий, але повільніший за Timsort; Merge Sort показує найвищий час виконання серед трьох, хоча різниця з Insertion Sort не така значна для цього конкретного випадку.
"""