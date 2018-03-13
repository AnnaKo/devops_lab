# !/usr/bin/python
"""python script"""
# pylint: disable=invalid-name

N = int(input("N value: "))
"""enter N name"""

def chislo(N):
    """define chislo function"""
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
