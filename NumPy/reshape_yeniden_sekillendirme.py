import numpy as np

arr = np.random.randint(10, size=9)

# Şimdi de elde ettiğimiz matrisin boyutunu değiştirelim yani reshape yapalım


arr.reshape(3, 3)
# burda dikkat edilmesi gereken kaç boyutlu yapacaksak boyut sayısı size değerinini bir katı olması gerekiyor


arr1 = np.random.randint(10, size=6)
arr1.reshape(2, 3)

arr3 = np.random.randint(10, size=8)
arr3.reshape(4, 2)






