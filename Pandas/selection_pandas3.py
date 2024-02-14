# ######## PANDASTA SEÇİM İŞLEMLERİ (SELECTION IN  PANDAS)###########

import pandas as pd
import seaborn as sbs
df = sbs.load_dataset("titanic")
df.head()

df.index

df[0:13]

df.drop(0, axis=0).head()  # burda sıfırıncı indexte olan elan-manı silme işlemi gerçekleşti sadece ekrana
                                 # yazdırmak için head() metodunu çağırdık görmek için

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)  # burada istrersek silmek istediğimiz bir listeyi de ekleyerek silebiliriz
# burada axis demek sadece satırlar üzerinde işlemlerin yapılmması gerektiğini ifade ediyor

df.drop(14, axis=0, inplace=True)

# #################  DEĞİŞKENİ İNDEXE ÇEVİRME#################

df["age"].head()
df.age.head()  # bu iki kullanım da aynı şekilde gerçekleşir

# şimdi de değişken olan age yi index halle çevirelim
df.index

df.index = df["age"]  # burada age değişkenini index haline getirdik şimdi bunu silelim değişkenlerden
df.drop("age", axis=1).head()  # evet burda axis değerini 1 dedik çünkü artık satırlardan değil de sütundan sildik
df.drop("age", axis=1, inplace=True)  # evet burda da kalıcı olarak silme işlemini gerçekleştirdik
df.head()

# ########### İNDEXİ DEĞİŞKENE ÇEVİRME#############

df.index  # burada de eğer indeks değerindeki herhangi bir indeksi değişken olarak atamak isterrseniz bu işlemleri yapcz

df["age"]  # mesela bunu çağırdıgımıda bir hata alırız çünkü yularıda bunu tamamen silmiştik
df["age"] = df.index
df.head()  # evet yukarıda  yaptıgımız atama işleminden sonra age indeksindeki değerleri age değişkeni oluşturarark
          # atama işlemleri gerçekleştirdik. Bu birinci yoldu şimmdi tekrardan yaş değişkenini silerek ikinci bir yoldan
          # tekrardan ekleme işlemini gerçekleştirelim

df.drop("age", axis=1, inplace=True)
df.head()  # evet bu işlemleri yaptık ve age değişkenini kaldırma işlemini gerçekleştirdik. Şimdi de tekrar ekleyelim

df.reset_index().head()
df1 = df.reset_index()
df1.head()
df1["age"] 









