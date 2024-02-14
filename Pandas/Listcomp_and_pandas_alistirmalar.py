# Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric(sayısal) değişkenlerin isimlerini büyük
# harfe çeviriniz ve başına NUM ekleyiniz.
import pandas as pd
import seaborn as sbs

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 500)
df = sbs.load_dataset("car_crashes")
df.columns
df.info()

comp_df = ["NUM_" + col.upper() if df[col].dtype != "0" else col.upper() for col in df.columns]

# Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
# değişkenlerin isimlerinin sonuna "FLAG" yazınız.
# Tüm değişkenlerin isimleri büyük harf olmalı.
# Tek bir list comprehension yapısı ile yapılmalı

df1_comp = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


# Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# og_list = ["abbrev", "no_previous"]
# Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()






