# ############# DEĞİŞKENLER ÜZERİNDE İŞLEMLER##############
import pandas as pd
import seaborn as sbs

pd.set_option("display.max_columns", None)  # bu kod çağıracak dataframin tüm değerlerini çağırı mesela bunu kaldır ve
# çağır ... noklatar kalkacak yani tüm değişkenleri ekrana yanısatac
df = sbs.load_dataset("titanic")
df.head()

"age" in df  # kontol ettik age değişkeni bu data fremede var mı diye

type(df["age"])  # Evet burda tipini sorguladıktan sonra bize Series olarak dönüş yapıyor dikkat
# Eğer bir değişken alacaksak ve bu değişken DataFrame ise ancak siz az önce yukarıda da denediğimiz gibi tipini
# sorgulayınca Series olarak döner. peki bunu nasıl halledebiliriz. Çift parantez içine almamız gerekiyor

type(df[["age"]])  # Evet şimdi DataFrame oldugunu bize söyledi!!!!!!!!!!!!!!!1

df[["age", "alive"]]  # Birden fazla değiişken seçerken iki köşeli paranteze dikkat

df1 = ["age", "alive", "fare"]

type(df[df1])  # Birden fazla değişkeni de tek bir liste içine alarak sorgulama işlemi yapabiliriz
# BUrda dikkat etmen gereken normalde birden fazla değişken sorguşaması yaparken iki tane köşeli parantez kullanırdık
# ancak zaten bizim elimizdeki de bir liste oldugu için direkt parametre olarak verebililiriz

df[df1]  # Evet bakın tek bir liste içinde bir liste de ekleyerek çağırma işlemi yapabildik

# Mesela yeni bir değişken atama işlemini şöyle yapabiliriz

df["age2"] = df["age"] ** 2  # Mesela burada da age değişkeni yerine age2 değişkenini ekledik ve  değişkendeki her
df["age2"]  # bir gözlem biriminin karesini alarak yeni bir değişken oluşturfuk

df["age3"] = df["age"] / df["age2"]  # Burda da yeni  bir değişkene bazı işlemler yaptık
df.head()  # Evet bu komutu çalıştırınca age3 değişkeni eklenir veri setimize
df.index
df.info

# Şimdi de bu age3 değişkenini dataframeden geçici olarak silelim

df.drop("age3", axis=1).head()  # evet geçici olarak silme işlemini yaptık şimdi de kalıcı olarak silelim
df.info  # bak halen 17 kolon gösteriyor şimdi silelim

df.drop("age3", axis=1, inplace=True)
"age3" in df
df.head()

# Peki birden fazla değişkeni nasıl silebiliriz

col_names = ["who", "alone", "alive"]  # bu değişkenler datada olan değişkenler şimdi silelim

df.drop(col_names, axis=1, inplace=True)  # Evet burda da birden fazla değişkeni silme işlemini yaptık
df.info

df.loc[:, df.columns.str.contains("age")].head()  # BUrada da colonlarda age ile başlayan tüm değişkenleri al dedik
df.loc[:, ~df.columns.str.contains("age")].head()  # BUrada da colonlarda age ile başlamayan tüm değişkenleri al dedik
