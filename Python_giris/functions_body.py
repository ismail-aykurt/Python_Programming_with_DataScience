"""
BUrada da fonksiyonların nasıl yazıldığı bir fonksiyon gövdesi nasıl olmalıdır
ona bakacağız
"""
def say_hi():
    """
    Burada sadece argüman veya parametre almayan bir fonksiyon yazdık
    :return: print()
    """
    print("merhaba")
    print("ben ismail")
    print("nasıl gidiyor")


say_hi()

def say_hi1(string):
    print(string)
    print("ismail")
    print("nasıl gidiyor")


say_hi1("tamamdır ekledim!!!")



#GİİRLEN HER HANGİ İKİ SAYININ ÇARPIMINI LİSTEYE EKLEME

list_store=[]

def add_element(a,b):
    """
    herhangi iki sayının çarpımını listeye ekleme
    :param a: int(a)
    :param b: int(b)
    :return: a * b and  append list_store[] ------>print(list_store)
    """
    c = a * b
    list_store.append(c)
    print(list_store)



add_element(5,4)
add_element(7,8)

############################# ÖN TANIMLI ARGÜMANLAR ########################
#Diyelim ki bir fonksiyon yazdık ve parametrelerini de verdik ancak parametre sayımız fazla biz istesek bu parametrelerde default değerleri verebiliriz

def devide(a=1, b=1):
    c=a / b
    print(c)


devide(4)
devide(5,6)


"""
NEDEN FONKSİYON TANIMLARIZ?
Sürekli aynı işlemleri tek tek yazmak yerine önceden hazır olan bir modül üzerinden kodlarımızı daha düzenli ve zamandan da tasarruf ederek
hemde kod sayımızı kod okunabilirliğimizi de arttırmak için yazarız
warm=ılık     moisture=nem    charge=şarj
"""
def calculate(varm , moisture, charge):
    conclusion=(varm + moisture) / charge
    print("girilen değerlere göre şehir sıcaklığ:",conclusion)


calculate(14 , 5 , 8)
#bu fonksiyonu her seferinde tek tek yazma yerine bir seferlik yaz ve kullan. DON'T REPEAT YOURSELF!!!!!




