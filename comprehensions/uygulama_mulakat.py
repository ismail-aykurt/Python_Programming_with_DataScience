###########################
# UYGULAMA- MÜLAKAT SORUSU
###########################

# AMAÇ: Çift sayıların karesi alınarak bir sözlüğe eklemek
# key'ler orijinal değerler value'ler ise değişen değerler olacak

numbers = range(10)

new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
# Şimdi de bunu comprehensions kullanarak tam bir mülakat sorusu cevabı verelim

new_dict1 = {n: n ** 2 for n in numbers if n % 2 == 0}
# Şimdi bak bakalım 4 satırlık bir kodu nasıl tek satırda yazabildik






