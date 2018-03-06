#!/usr/bin/python

N = int(input("N value: "))

def chislo(N):
    L = []
    while N > 1:
        for I in range(9, 1, -1):
            if N % I == 0:
                L.append(I)
                N /= I
                break
        else:
            return '-1'

    return ''.join(map(str, reversed(L)))

print ("smallest value for N is:")
print (chislo(N))






  
