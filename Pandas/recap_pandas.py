# Burada pandasta elde ettikleriimizdernekstra olarak tekrarlarımızı yapacağız

import pandas as pd
import seaborn as sbs
from numpy import delete

pd.set_option("display.max_columns", None)
df = sbs.load_dataset("titanic")

df.head()
df.size
df.ndim
df.shape
df.info()  # BUrda da data üzerinde daha lkapsamlı biiglgi aldık
type(df)
df.columns
df.index
df.describe().T   # BUrda da direk tveri üüzerinde bir özet aldık

df.isnull().values.any()  # Bu veri d-setinde een aaz bir değerde gereksiz veri var mı?
df.isnull().sum()

df.isnull().mean()

df["age"].head()
df[["age", "sex"]].head()  # eğer iki değer verme istersek de bir tane daha parantez açman gerekecek

# ##################################################################################
# PANDASTA SELECTION OPERATİONS

df[0:3]
df.drop(0, axis=0).head()

delete_index = [1, 2, 3, 5]
df.drop(delete_index, axis=0).head()  #burda da istediiğimz herhanig satırlardan geçici silme işlem yaptık

# şimdi de işlmei kalıcı olaarak silelim

df.drop(delete_index, axis=0, inplace=True)  # evet kalıcı olarak silme işlemini de hallettik
df.head()
df.info

df.size
df.ndim
df.index
df.shape
df.columns
df["age2"] = df["age"] * 2
df.head()


df.info()

# şimdi de değişkenlere göre istediğimiz konumlardaki değişkenleri alalım. Yani veri seçimi ve indeksleme işlemlerinde
# işe yarıyorlar
df.iloc[0:2]
df.iloc[0:3, 2]
df.loc[0:8, "age"]

set_columns = ["age", "who", "fare"]
df.loc[0:6, set_columns]
