# KOŞULLU SEÇİM İŞLEMLERİ

import pandas as pd
import seaborn as sbs

pd.set_option("display.max_columns", None)
df = sbs.load_dataset("titanic")
df.head()

# Şimdi de şartlı bir seçim yapmak isteyelim

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()  # Burada yaşı 50 den büyük olan toplam kişi sayısını aldık

# şimdi de bir koşul ve o koşulu sağlayan sütunu alalım

df.loc[df["age"] > 50, "class"].head()

df.loc[df["age"] > 50, ["age", "class"]].head()  # Burda da yaş değeri 50 den büyük olan yaş ce class değişkenleri aldık

df.loc[df["who"] == "man", "who"].head()  # Burda da who değiikeninden man olan ilk beş who değişkeni aldık

# Eğer birden fazla koşul vermek istersek de bunları parantez içine almamız gerekiyor

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class", "sex"]].head()
# Yukarıda yaşı 50 den buyuk ve cinsiyeti erkek olan değişkenleri aldık aslında bunu SQL de daha rahat yapabiliriz
# oraya da sıra gelecek

col_names = ["alive", "alone", "age", "class", "sex", "embark_town"]

df.loc[(df["sex"] == "female") & (df["age"] < 50), col_names].head(10)

# Şimdi de 3 adet koşul ekleme işlemi yapalım
df.loc[(df["sex"] == "female") &
       (df["age"] < 50) &
       (df["embark_town"] == "Cherbourg"), col_names].head(10)
# Burda sadece kodun okunabilirliğini artttırdım


# Mesela şimdi de koşulu daha da karıştıralım. Bu sefer de embark_town a yada ekleyelim
df["embark_town"]

df.loc[(df["sex"] == "female") &
       (df["age"] < 50) &
       ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")), col_names].head(10)
