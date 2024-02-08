# divide students adında bir fonksiyon yazılacak
# burda çift indekste olanlar bir listeye
# tek indekste olanlar başka bir listeye atılacak
# en sonunda da tek listede olacakk şekilde çıktı verilecek

students = ["İsmail", "Ahmet", "Mustafa", "Melih", "Fatih", "Mehmet Ali"]


def divide_students(students):
    """
    Bir fonksiyon tanımladık burada girilen bir listede tek ve çift indekslerde bulunan her bir elemanı tek olanı başka bir listeye
    çift olanı da başka listeye atıyoruz ve kullanıcıya tek bir liste halinde veriyoruz
    :param students: list[]
    :return: groups[[A][B]]
    """
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)

        else:
            groups[1].append(student)
    print(groups)


divide_students(students)

#Burada girilen bir listedeki elemanların indekslerini enamurate ile bularak onları tek ve çift indekslerine
#göre bir listeye atadık ve çıktıyı da iki listeyi birleştirerek verdik

