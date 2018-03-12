#!/usr/bin/python

N = int(input("N value: "))


def chislo(N):
    L = []
    while N > 1:
        for i in range(9, 1, -1):
            if N % i == 0:
                L.append(i)
                N /= i
                break
        else:
            return '-1'

    return ''.join(map(str, reversed(L)))


print("smallest value for N is:")
print(chislo(N))
