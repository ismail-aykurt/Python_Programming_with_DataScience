# ################ Why NumPy ##############
# NumPy, Python'da hızlı ve etkili bilimsel hesaplamalar yapmak için kullanılan bir kütüphanedir. Çok boyutlu dizilerle
# çalışma yeteneği, hızlı matematiksel işlemler, yaygın kullanılan veri yapılarını temsil etme ve diğer bilimsel
# kütüphanelerle uyum gibi avantajlarıyla öne çıkar. Python topluluğunda yaygın olarak kullanılır ve geniş bir fonksiyon
# yelpazesi sunar.


import numpy as np

# Mesela elimizde iki liste olsun buradaki her bir elemanı çarpalım bunu klasik pythonik yoldan yapalım

list1 = [1, 2, 3, 4]
list2 = [1, 3, 5, 6]

null_list = []

for i in range(0, len(list1)):
    null_list.append(list1[i] * list2[i])

# Burada da numpy kütüphanesini kullanarak işlemlerimizi daha hızlı ve daha az kod satırı yazarak gerçekleştrebildik
list1 = np.array([1, 2, 3, 4])
list2 = np.array([1, 3, 5, 6])
result = list1 * list2






