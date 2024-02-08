"""
Lambda fonksiyonları, isimsiz (anonim) fonksiyonlardır ve lambda anahtar kelimesi ile tanımlanırlar.
Bu fonksiyonlar, kısa süreli kullanımlar veya tek bir satırda basit işlemler için uygundur.
Lambda fonksiyonlarını genellikle bir işlevin içinde veya bir fonksiyonun argümanı olarak kullanırız.
KULLLANIMI:
lambda arg1,arg2,...:ifade

"""
topla = lambda a, b: a + b

topla(4, 5)
# yani trek seferlik yaz kullan at mantığı


# ----------------------------------------------------------------------------------------------------------------------
# MAP()
"""
map() fonksiyonu, Python'da bir veya daha fazla iterable'ın (liste, demet, dize vb.) her
elemanına belirli bir işlemi uygulamak için kullanılan bir fonksiyondur. map() fonksiyonu,
orijinal iterable'ı değiştirmez, sadece belirtilen işlemi uygulayarak yeni bir iterable 
(genellikle liste) oluşturur.
iterable=liste, demet, setler...
KULLANIMI= iterable(map(fonksiyon, iterable1, iterable2))
"""

karesi = lambda x: x * x

number = [1, 2, 3, 6]

list(map(karesi, number))

list(map(lambda a: (a * 40 / 100) + a, number))

list(map(lambda a: a ** 2, number))

# ------------------------------------------------------------------
# Filter()
# Yani sadece istediğimiz bir iterabledeki elamanları filtrelemeye yarıyor
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list(filter(lambda x: x % 2 == 0, list_store))

# -------------------------------------------------------------------
# Reduce() ----->herhangi bir iterabledeki eelmanların tek bir değere indirgeme işlemi
#burda dikkat etmen gereken en önemli şey biz mesela map ve filter de bir iterable olarak döndürüuorduk ancak reducede tek
#değişkene indirgendiği için bir iterable olmuyor artık. yani hata alırız.

#KULLANIMI----> from functools import reduce ----> reduce(lambda arg1,arg2: ifade , iterable)

from functools import reduce

liste1 = [1, 2, 3, 4]

reduce(lambda x, y: x + y, liste1)
