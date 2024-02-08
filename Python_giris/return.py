#fonksiyonların çıktışarını girdi olarak kullnamak demektir

"""def topla(a, b):
    print(a+b)

topla(5,4) * 5
Mesela buradaki fonksiyona biz isteiğimiz bir değeri çarparsak hata alırız çünkü en başta değerimizin tipi NoneType oluyor """

def topla(a, b):
    return a+b

d=topla(5,7)
toplama=d * 8
print(toplama)

def calculate(varm , moisture , charge):
    varm*=2
    moisture*=2
    charge*=2
    sonuc=(varm + moisture) / charge
    return varm, moisture, charge , sonuc

varm , moisture , charge , sonuc=calculate(5,32,51)


#LOCAL & GLOBAL  DEĞİŞKENLER




