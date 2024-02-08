# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.

x = 8j + 15
type(x)

a = "hello"
type(a)

c = 12 < 15
type(c)
# ---------------------------------------------------------------------------------------------------------------

# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.

text = "the goal is to turn data into information, and into insight."
text.upper().replace(",", " ").replace(".", " ").split()

# ----------------------------------------------------------------------------------------------------------------

# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.
# Adım 1: Verilen listenin eleman sayısına bakınız.
# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım 4: Sekizinci indeksteki elemanı siliniz.
# Adım 5: Yeni bir eleman ekleyiniz.
# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

len(lst)  # adım1

lst[0]  # adım2
lst[10]

bos_lst = []  # Adım3
for i in lst:
    bos_lst.append(i)
    if bos_lst == ["D", "A", "T", "A"]:
        break

print(bos_lst)

# veya bu şekilde de yapabiliriz ancak biz burda sadece elemanların indeks numaralarını bildiğimiz için bu adımları yaptık
# bilmeseydik yukarıda yaptıgım gibi bir loop ile bu işlemi gerçekleştirebilirdik
new_lst = lst[0:4]

# ----------------------------------------------------------------------------------------------------------------
# Adım 4: Sekizinci indeksteki elemanı siliniz.

lst.pop(8)
lst.remove("N")
# burada remove ile herhangi bir değer silebilirken pop metodu ile de hangi indekste ise onu seçerek silmek gerekiyor
# eğer sadece pop dersek  bize listedeki son elemanı silecektir


# Adım 5: Yeni bir eleman ekleyiniz.

lst.append("S")

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(9, "C")
# ---------------------------------------------------------------------------------------------------------------

# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
# Adım 1: Key değerlerine erişiniz.
# Adım 2: Value'lara erişiniz.
# Adım 3: İsmail key'ine ait 18 değerini 19 olarak güncelleyiniz.
# Adım 4: Key değeri Selman value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Adım 5: Fatih'i dictionary'den siliniz.


dict = {"İsmail": ["Türkiye", 18],
        "Fatih": ["England", 20],
        "Mehmet Ali": ["Suriye", 21],
        "Ahmet Muhsin": ["Habeşistan", 25]}

dict.keys()  # Adım 1: Key değerlerine erişiniz.

dict.values()  # Adım 2: Value'lara erişiniz.

dict.update({"İsmail": ["Türkiye", 19]})  # Adım 3: İsmail key'ine ait 18 değerini 19 olarak güncelleyiniz.

dict.update(
    {"Selamn": ["Turkey", 24]})  # Adım 4: Key değeri Selman value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.pop("Fatih")  # Adım 5: Fatih'i dictionary'den siliniz.

# ---------------------------------------------------------------------------------------------------------------

# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız. Ben bunu bir kaç farklı yoldan yazcam
# 1. yol enamurate metodu ile yazmak

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def enamurate_with_ayirma(lst):
    lst1 = []
    lst2 = []
    for index, gezinme in enumerate(lst):
        if index % 2 == 0:
            lst1.append(gezinme)

        else:
            lst2.append(gezinme)

    return lst1, lst2


enamurate_with_ayirma(lst)

# 2. yol normal listeyi bir for döngüsü ile dolaşarak yazmak

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = []
lst2 = []
for i in lst:
    if i % 2 == 0:
        lst1.append(i)
    else:
        lst2.append(i)
print(lst1, lst2)

# 3. yol ise lambda ile olacak
ayirma_double = list(filter(lambda a: a%2==0, lst))
ayirma_single = list(filter(lambda x: x % 2 != 0, lst))
print(ayirma_double, ayirma_single)

# ---------------------------------------------------------------------------------------------------------------

# Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız

students = ["İsmail", "Mehmet Ali", "Fatih", "Zeynep", "Aslı", "Liva"]

for index, student in enumerate(students):
    if index < 3:
        index += 1
        print("Mühendislik Fakültesi", index, ". öğrenci :", student)

    else:
        print("Tıp Fakültesi", index, ". öğrenci :", student)

# -----------------------------------------------------------------------------------------------------------------

# Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
# almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişiliktir")

# ---------------------------------------------------------------------------------------------------------------
# Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data" ,"python"])
kume2 = set(["data", "function", "quit", "lambda", "python", "miuul"])

def kume(set1 , set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1, kume2)