############################FONKSİYONLAR GENEL YAPILARI NELERDİR##############################
# Belirli görevleri yerine getirmek için hazırlnmış kod blokları.

# FONKSİYON OKURYAZARLIĞI
# argüman ve parametre aynı değerlerdir aslında. Parametre fonksiyonu oluştururken verilen değerler olurken
# argüman ise fonksiyonu çağırırken verilen değerlere denir
print("a", "b")
print("a", "b", sep="__")


# FONKSİYON TANIMLAMA

def iki_carp(sayi1=int(0),

             sayi2=int(1)):

    carpma = sayi1 * sayi2
    print(carpma)


iki_carp(8, 5)

def summer(arg1,
           arg2):
    """
    toplama

    :param arg1: int , float
    :param arg2: int , float
    :return: arg1 + arg2
    """


    print(arg1 + arg2)


summer(12,8)
summer(15, 8)
