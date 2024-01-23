from datetime import datetime
import numpy as np


def grades(num):
    if num >= 0.9:
        res = 5
    elif num >= 0.7:
        res = 4
    elif num >= 0.5:
        res = 3
    elif num >= 0.3:
        res = 2
    elif num >= 0:
        res = 1

    return res


# Task1
# write to a file
f = open("lab1.txt", "a")
f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


# case A
arrayA = np.random.rand(4, 5, 7)

f.write("\nA:\n")
f.write(str(arrayA))


# case B
arrayB = np.around(arrayA)
arrayB = arrayB.astype(int)

f.write("\nB:\n")
f.write(str(arrayB))

# case C
arrayC = np.empty((4, 5, 7))

for a in range(4):
  for b in range(5):
      for c in range(7):
          arrayC[a][b][c] = grades(arrayA[a][b][c])

arrayC = arrayC.astype(int)
f.write("\nC:\n")
f.write(str(arrayC))

f.close()

# Task2
# according to the task ¯\_(ツ)_/¯
w1 = [1, 0, 0, 0]
w2 = [1, 0, 0, 0, 0]
w3 = [1, 0, 0, 0, 0, 0, 0]


def sum_with_coefs(array, w1, w2, w3):
    sum = 0
    for i in range(4):
        for j in range(5):
            for k in range(7):
                sum += w1[i] * w2[j] * w3[k] * array[i][j][k]
    return sum


# case A
a = sum_with_coefs(arrayA, w1, w2, w3)
print("Grade A:", a)

# case B
b = sum_with_coefs(arrayB, w1, w2, w3)
print("Grade B:", b)


# case C
def stuff(array):
    # generate random priorities, but they sum up to 1
    wz = np.random.dirichlet(np.ones(140), size=1)
    a_flat = array.ravel()

    sum = 0
    for j in range(140):
        sum += wz[0][j] * a_flat[j]
    return sum/140


print("Grade C (with priorities):", stuff(arrayA))

c = np.sum(arrayC)/140
print("Grade C (w/o priorities):", c)

# Task 3
print("331:", arrayA[2][2][0], arrayB[2][2][0], arrayC[2][2][0])
print("453:", arrayA[3][4][2], arrayB[3][4][2], arrayC[3][4][2])
print("452:", arrayA[3][4][1], arrayB[3][4][1], arrayC[3][4][1])
print("114:", arrayA[0][0][3], arrayB[0][0][3], arrayC[0][0][3])
print("141:", arrayA[0][3][0], arrayB[0][3][0], arrayC[0][3][0])


# Task 5
def smol(array, N):
    idx = array.ravel().argsort()[:N]
    return np.stack(np.unravel_index(idx, array.shape)).T


print("Smallest values:")
for a in smol(arrayA, 5):
    print(arrayA[a[0]][a[1]][a[2]], " - ", a)
