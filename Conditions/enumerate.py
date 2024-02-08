# enumerate fonksiyonu, bir iterable nesne üzerinde dolaşırken hem indeksi
# hem de değeri kullanmanız gereken birçok durumda kullanışlıdır

names = ["ismail", "mustafa", "ali", "tezcan"]
A = []
B = []

for index, name in enumerate(names):
    if index % 2 == 0:
        A.append(name)
        print(A)
    else:
        B.append(name)
        print(B)


