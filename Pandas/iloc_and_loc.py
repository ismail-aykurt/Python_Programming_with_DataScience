# Loc and ILOC yapısı

import pandas as pd
import seaborn as sbs

pd.set_option("display.max_columns", None)
df = sbs.load_dataset("titanic")

# iLog ile konum tabanlı seçimi yapabiliriz

df.iloc[0: 3]  # Burada diyoruz iki 0 ile 3 e kadar bana gözlem birimlerini getir arada : var
df.iloc[0, 0]  # Bura da da 0. satır 0. sütüundaki değeri getir dedik arada da virgül var dikkat
# Şimdi burda mesela biz 0:3 dedik bize 0,1,2 olan değerleri getirdi ancak şimdi yapacağım loc işlemi etiket neyse
# o değerleri döndürecek

df.loc[0:3]  # Burda demek istediğim bize 0,1,2,3  3 de dahil ne varsa onları getirecek

# Şimdi bir aralık ve de değişken almak istersek de iloc kullanmayız da loc kullanırız. iloc kullanarak hata alalım

df.iloc[0:3, "age"]  # Evet bu tarz bir kullanım yaparsak hata alırız
df.iloc[0:3, 0:3]  # Ancak bu şekilde deriz ki 3. satır ile 3.sutunları al

df.loc[0:3, "age"]  # Bu şekilde kullanımı yaparak sadece değikeni alabiliriz

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]  # Bu tarz bir kullanım da yapılabilir
