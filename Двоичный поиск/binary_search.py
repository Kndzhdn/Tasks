import sys

'''
В первой строке даны целое число 1 ≤ n ≤ 10^5 и массив A[1…n] из n различных натуральных чисел,
не превышающих 10^9 в порядке возрастания, 
во второй — целое число 1 ≤ k ≤ 10^5 и k натуральных чисел b_1, ..., b_k, не превышающих 10^9. 

Для каждого i от 1 до k необходимо вывести индекс 1 ≤ j ≤ n, 
для которого A[j]=b_i, или -1−1, если такого jj нет.
'''




'''
Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
'''

def binary_search(xs, query):
    left, right = 0, len(xs)-1
    while left <= right:
        middle = (left+right) // 2
        if query < xs[middle]:
            right = middle - 1
        elif query > xs[middle]:
            left = middle + 1
        else:
            return middle + 1
            
    return -1


reader = (map(int, line.split()) for line in sys.stdin)
n, *xs = next(reader)
k, *queries = next(reader)
for query in queries:
    print(binary_search(xs, query), end=" ")
