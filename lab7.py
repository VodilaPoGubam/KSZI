import numpy as np
from random import uniform, randint
from scipy.optimize import linprog

# task 2
# n = size
def saati(n: int):
    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i, j] = 1
            elif matrix[i, j] == 0:
                matrix[i, j] = round(uniform(0.1, 9), 3)
                matrix[j, i] = round(1/matrix[i, j], 3)

    return matrix


# for task 3
def coefs(matrix, n):
    c_sum = []
    for r in range(n):
        c_sum.append(matrix[r].sum())

    total_sum = sum(c_sum)
    for i in range(len(c_sum)):
        c_sum[i] = round(c_sum[i]/total_sum, 3)

    return c_sum


# task 3 itself
n = 10                              # quantity of experts
m = saati(n)                        # saati matrix
c = coefs(m, n)
h = np.random.randint(10, 100, n)   # notional value of experts
H = 300                             # max price

res = linprog([-i for i in c], [h], H, method='highs', bounds=(0, 1))

final = []
for x in res.x:
    if x == 1:
        final.append(1)
    else:
        final.append(0)

authority = sum([c[i]*final[i] for i in range(9)])
authority_r = round(authority, 3)

price = sum([h[i]*final[i] for i in range(9)])

print(m)

print("Авторитетність експертів: ", c)
print("Вартість експертів: ", h)
print("Вибір експертів: ", final)

print("Авторитетність групи", authority)
print("Вартість групи", price)

if price > H:
    print("На жаль, вартість перевищує очікувану")
