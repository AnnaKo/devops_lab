#!/usr/bin/python

E = str(input())
L = ['+', '-', '*', '/']

for I in range(len(L)):
    if E[1:].find(L[I]) >= 0:
        A = E[1:].index(L[I])+1
        break
      
try:
    Q = E.index('=')
    X, Y, Z = int(E[0:A]), int(E[A + 1:Q]), int(E[Q + 1:])
    if E[A] == '+' and X + Y == Z:
      print('YES')
    elif E[A] == '-' and X - Y == Z:
      print('YES')
    elif E[A] == '*' and X * Y == Z:
      print('YES')
    elif E[A] == '/' and X / Y == Z:
      print('YES')
    else:
      print('NO')

except Exception:
  print ('ERROR')