#!/usr/bin/python

print('Type Your Numbers - First List:')
A = input().split()
print('Type Your Numbers - Second List:')
B = input().split()

# A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("given lists are")
print(A)
print(B)

C = list(set(A).intersection(B))
print("the result list with common elements and no duplicates is below:")
print(C)
# [1, 2, 3, 5, 8, 13]
