import pandas as pd
import seaborn as sbs

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

#####################################################################################################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız
#####################################################################################################################
df = sbs.load_dataset("titanic")
df.head()
df.shape  # kaç satır kaç sutun oldugu bilgisi

#####################################################################################################################
# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#####################################################################################################################

df["sex"].value_counts()  # Burada kadın ve erkek sayılarını ayrı ayrı bulabiliyoruz
df["sex"].count()  # Burada da sadece kadın ve erkeklerin her ikisinin de yaşlarının toplamını buluyoruz

#####################################################################################################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#####################################################################################################################
df.nunique()  # Burada her bir değişken için yaptım.
df["who"].unique()  # Burda da sadece özel bir değişken aldım ve isimlerine baktım.

#####################################################################################################################
# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
#####################################################################################################################
df["pclass"].unique()

#####################################################################################################################
# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz
#####################################################################################################################
col_names = ["pclass", "parch"]
df[
    col_names].nunique()  # Ben burada iki şekilde seçme işlemi yaptım önce seçmek istediğim değişkenleri bir tane listeye
# aldım daha sonra bunlar üzerinden seçme işlemi yaptım.
df["pclass"].nunique()
df[["pclass", "parch"]].nunique()  # Şimdi burda da dikkat etmem gereken şey eğer birden fazla değişken alacaksak
# bunu iki parantez içinde almalıyız almazsak veri seti olarak Series olur ve hata alırız istersen dene


#####################################################################################################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
#####################################################################################################################
type(df[["embarked"]])
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype

#####################################################################################################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz
#####################################################################################################################
df[df["embarked"] == "C"].head(10)

#####################################################################################################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#####################################################################################################################
df[df["embarked"] != "S"].head(5)

#####################################################################################################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#####################################################################################################################
df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()
df[(df["age"] < 30) & (df["sex"] == "female")].head()  # Her iki kullanım da geçerli sayılır

#####################################################################################################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#####################################################################################################################
df.loc[(df["fare"] > 500) | (df["age"] > 70)].head()

#####################################################################################################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#####################################################################################################################

df.isnull()  # Burada bpş olan değişkenleri aldık True yada False değeri döndürür şimdi de toplam boş olan değerleri
# alalım
df.isnull().sum()
# Mesela bu data framede boş değer var mı yok mu sorgulayalım
df.isnull().values.any()  # Boş değer var mı yok mu baktık

#####################################################################################################################
# Görev 12: who değişkenini dataframe’den çıkarınız.
#####################################################################################################################
df.drop("who", axis=1, inplace=True)  # Burda tamamen silme işlemi yaptık ve de aşada var mı yok mu kontrol ettik
"who" in df

#####################################################################################################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#####################################################################################################################
type(df["deck"].mode())  # veri tipi Series oluyor dikkat
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

#####################################################################################################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
#####################################################################################################################

type(df["age"].median())
df["age"].fillna(df["age"].median(), inplace=True)
df["age"].isnull().sum()
df.isnull().sum()

# BUrada kenidim boş ola neğeri bulup onu bir değer ile doldurcam
df["embark_town"].isnull().sum()
df["embark_town"].fillna(df["embark_town"][0], inplace=True)
df.isnull().sum()

#####################################################################################################################
# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#####################################################################################################################

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]}).head()

df.groupby(["sex", "class"]).agg({"age": ["mean", "sum"],
                                  "survived": "mean"})


#####################################################################################################################
# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız
# fonksiyonu kullanarak titanik verisetinde age_flag adında bir değişken oluşturunuz . (apply ve lambda
# yapılarını kullanınız)
#####################################################################################################################
def age_30(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: age_30(x))
df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)


#####################################################################################################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız
#####################################################################################################################
df1 = sbs.load_dataset("tips")
df1.head()
df1.info()
df1.size
df1.shape

#####################################################################################################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve
# ortalamasını bulunuz.
#####################################################################################################################

df1.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]}).head()

#####################################################################################################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#####################################################################################################################

df1.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]}).head()

#####################################################################################################################
# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max
# ve ortalamasını bulunuz.
#####################################################################################################################

df1[(df1["time"] == "lunch") & (df1["sex"] == "female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"],
                                                                             "tip": ["sum", "min", "max", "mean"]})

#####################################################################################################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
#####################################################################################################################

df1.loc[(df1["size"] < 3) & (df1["total_bill"] > 10), "total_bill"].mean()
# Veya önce bir değişkene atama yaparım sonra da ortalamasını alırım

df2 = df1.loc[(df1["size"] < 3) & (df1["total_bill"] > 10)]
df2["total_bill"].mean()


##################################################################################################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve
# tip in toplamını versin.
##################################################################################################################
df1["total_bill_tip_sum"] = df1["total_bill"] + df1["tip"]
df1["total_bill_tip_sum"].sum()  # Burda toplamını bulduk

##################################################################################################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e
# atayınız.
##################################################################################################################

new_df = df1.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape
new_df.info()

