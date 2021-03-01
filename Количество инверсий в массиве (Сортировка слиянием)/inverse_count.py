'''
Первая строка содержит число 1 <= n <= 10^5,
вторая — массив A[1...n], содержащий натуральные числа, не превосходящие 10^9.

Необходимо посчитать число пар индексов 1 <= i <= j <= n,
для которых A[i]>A[j].

(Такая пара элементов называется инверсией массива.
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
'''


def merge(arr, left, right):
    i = 0
    j = 0
    count = 0

    while i < len(left) or j < len(right):
        if i == len(left):
            arr[i+j] = right[j]
            j += 1
        elif j == len(right):
            arr[i+j] = left[i]
            i += 1
        elif left[i] <= right[j]:
            arr[i+j] = left[i]
            i += 1
        else:
            arr[i+j] = right[j]
            count += len(left)-i
            j += 1


    return count




def get_inverse_count(arr):
    if len(arr) < 2:
        return 0

    center = len(arr) // 2
    left_part = arr[:center]
    right_part = arr[center:]

    return get_inverse_count(left_part) + get_inverse_count(right_part) + merge(arr, left_part, right_part)


n = int(input())
array = list(map(int, input().split()))
print(get_inverse_count(array))