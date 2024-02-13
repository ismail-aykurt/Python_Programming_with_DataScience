import numpy as np


arr1 = np.random.randint(10, size=8)

arr1[0]
arr1[0:5]

arr1[0] = 999

arr2 = np.random.randint(10, size=(3, 5))
# burada 3 satırlık 5 sutunluk bir matris oluşturduk. Mesela ilk satırın ilk elemanına nasıl erişebiliriz

arr2[0, 0]
arr2[1, 3]
# Burada herhangi bir satıra eleman ekleme işlemi yapalım
arr2[2, 1] = 999

# mesela herhangi bir satırına bir float değeri eklemeye çalışalım

arr2[2, 2] = 2.757
# burada numpy nümerik oldugu için yani sadece aynı veri tiplerindeki sayıları aldıgı için float olan
# bir değeri dizimiz hangi veri tipinde ise ona göre ekleme yapacaktır. Yani 2.75 i 2 olarak ekledi

arr2[:, 0]

arr2[0:2, 0:3]


# peki buz bu indexlere her zaman tek tek yazarak mı erişmeye çalışcaz. İşte burda da (fancy index) kavramı devreyegirer

liste = [0, 1, 2]
arr2[liste]



