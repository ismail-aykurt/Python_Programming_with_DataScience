# ############# VERİ OKUMA##########

import pandas as pd

df = pd.read_csv("DataSets/ornek.csv")

df.head(5)
df.size
df.ndim

# Burada  farklı formatlarda verileri okumak istersek de ctrl tuşuna basılı tutup pandas kütüphanesine gireceğiz
# orada ctfl+ F yaparak read_ yazıp gerekeli olan tüm bilgiler karşımıza çıkacaktır zaten

df1 = pd.read_csv("DataSets/data.csv")
df1.head()
df1.info()
df1.dtypes
df1.size

# Mesela burada verileri okuduktan sonra verilerde hata var mı yokmu varsa da bunşarı nasıl halledebiliriz

df2 = pd.read_csv("DataSets/data.csv")
df2.info()
df2.isnull().values.any()  # bu komut ile dosyada hatalı veri var mı yok mu diye sorgulayalım önce. Bu komut çalıştıktan
# sonra True değeri dönecektir demekk ki hatalı bir veri var. Şimdi de hangi sütunda kaçar tane hata var bakalım
df2.isnull().sum()
# Yukarıdaki komut çalıştıktan sonra bize hangi kolonda kaçar tane hata oldugunu söyledi. Şimdi de bu hataları
# temizleyelim
df3 = df2.dropna()
df3.info()
# Yukarıda temizlnmiş bir şekilde df3 e atama yaptık ve info() diyerek bilgileini aldıktan sonra en başta 169 satır olan
# cvs dosyamız hatalı olan satırları çıkardıktan sonra satır sayısında düşüş oldugunu gözlemleyebiliriz
