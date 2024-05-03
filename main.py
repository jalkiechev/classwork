#задача1
import numpy as np
M = 3
np.random.seed(0)
B = np.random.randint(-10, 10, (M, M))
print("Матрица B:")
print(B)
positive_product = 1
for i in range(M):
    for j in range(M):
        if B[i, j] > 0:
            positive_product *= B[i, j]
print("Произведение положительных элементов матрицы B:", positive_product)
#задача2
import numpy as np
M = 5
B = np.random.randint(0, 100, size=(M, M))
print("Матрица B:")
print(B)
minf = np.min(B)
minf_kek = np.unravel_index(np.argmin(B), B.shape)
print("\nМинимальный элемент матрицы B:", minf)
print("Его координаты:", minf_kek)
#задача3
import numpy as np
M = 3
N = 4
D = np.random.randint(0, 100, size=(M, N))
print("Матрица D:")
print(D)
min_ = np.unravel_index(np.argmin(D), D.shape)
max_ = np.unravel_index(np.argmax(D), D.shape)
D[min_], D[max_] = D[max_], D[min_]
print("\nМатрица D после замены минимального и максимального элементов:")
print(D)
#задача4
import numpy as np
M = 5
P = np.random.randint(1, 10, size=(M, M))
print("Матрица P:")
print(P)
cl = np.prod(P, axis=0)
print("\nПроизведения элементов каждого столбца:")
print(cl)
#задача5
import numpy as np
M = 5
P = np.random.randint(-10, 10, size=(M, M))
print("Матрица P:")
print(P)
net = np.sum(P < 0, axis=1)
print("\nКоличество отрицательных элементов в каждой строке:")
print(net)
