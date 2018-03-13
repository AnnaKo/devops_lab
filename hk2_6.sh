# !/usr/bin/python
"""python script"""
# pylint: disable=invalid-name

exp = str(input("Add Your Expression Here: "))
"""adding expression from input"""
li = ['+', '-', '*', '/']
"""setting the list"""

for i in range(len(li)):
    if exp[1:].find(li[i]) >= 0:
        A = exp[1:].index(li[i])+1
        break

try:
    Q = exp.index('=')
    X, Y, Z = int(exp[0:A]), int(exp[A + 1:Q]), int(exp[Q + 1:])
    if exp[A] == '+' and X + Y == Z:
        print('YES')
    elif exp[A] == '-' and X - Y == Z:
        print('YES')
    elif exp[A] == '*' and X * Y == Z:
        print('YES')
    elif exp[A] == '/' and X / Y == Z:
        print('YES')
    else:
        print('NO')

except Exception:
    print('ERROR')
