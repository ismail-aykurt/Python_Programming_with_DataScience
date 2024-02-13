import numpy as np

a = np.array([1, -2, 3, 4])
np.add(a, 5)
np.subtract(a, 5)
np.power(a, 2)
np.abs(a)
np.zeros(10, dtype=int)
np.sum(5)
np.mean(a)  # bu metod da ortalama almaya yarıyor
np.min(a)
np.max(a)
np.var(a)

# ####### NumPy de iki bilinmeyen denklem çözme #######

# a = 0*x + 3*x = 4
# b = 2*x + 5*x1 =2

a = np.array([[0, 3], [2, 5]])
b = np.array([4, 2])
np.linalg.solve(a, b)


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1]