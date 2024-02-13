# ############# Creating numpy array#############

import numpy as np

np.array([1, 2, 3, 4])
type(np.array([1, 2, 3, 4]))
np.zeros(10, dtype=int)

np.random.random_integers(0, 10, size=10)

np.random.normal(10, 4, (3, 4))


# size -->  Topla eleman sayısını döndürür
# ndim--->  Dizinin boyut sayısını döndürür
# shape---> boyut bilgisi
# dtype---> arrayy veri tipi

a = np.random.randint(5, 10, size=5)
a.size
a.ndim
a.shape
a.dtype
