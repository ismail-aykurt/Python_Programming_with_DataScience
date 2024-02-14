# Toplulaştırma ve Gruplama (Aggregation and Groups)
# count()
# first()
# last()   # BU metodları kullanarak veri setimizdeki değişkenlerden birini veya herhangi bir kaçını istediğimiz şekilde
# mean()   # gruplama ve de toplulaştırma işlemleri yapabiliriz
# median()
# min()
# max()
# std()
# sum()

import pandas as pd
import seaborn as sbs

pd.set_option("display.max_columns", None)
df = sbs.load_dataset("titanic")
df.head()

# Örneğin yaş değişkeninin ortalamasını almak isteyelim
df["age"].mean()  # Burda sadece yaş değişkeninin ortalamasını aldık tamam da ben cinsiyet sınıfından kadın ve erkek
                  # ayrı ayrı yaş değişkenlerinin ortalamasını nasıl alabiliirm. Bunun için de groupby() fon kllncaz
df.groupby("sex")["age"].mean()
# Evet önce fonksiyonu aldık ve neyin değerini alalım dedi bende cinsiyet dedim neye göre yaşa göre dedik

# Şimdi de cinsiyete göre yaş ortalaması ve de toplamını alalım burda aggregation kullanacaz sürekli bunu alışkanlık
# haline getirmek işimizi daha da rahatlatacak

df.groupby("sex").agg({"age": ["mean", "sum", "count"]})
# Evet yukarıdaki kullanım her zaman daha avantajlı bu şekilde bir gruplama yapabiliriz

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})


# Şimdi de cinsiyetten başka bişey daha ekleyelim ve kırılım miktarını arttıralim

df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"],
                                        "survived": "mean"})


df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "count"],
                                        "survived": "mean"})

# Bu kodu çalıştırdıktan sonra şu şekilde okuyabiliriz mesela cinsiyeti kadın olan Cherbourg dan binen 1. sınıf yaş
# ortalaması 36.0522 olan 38 kişinin hayatta kalma ortalaması 0.9767..  şeklinde ilk kişiyi okudum
# Bu şekilde verileri gruplama yaparak daha iyi bir şekilde analiz edebiliriz
# survived değişeni sayısal bir değişken ve sadece 1 ve 0 dan oluşur. 1 se hayattasın 0 ise öldün. Mesela biz burda
# survived değişkenini kullandık ve ortalamalarını aldık eğer bire yakınsa demekki hayatta kalması daha garanti


# Şİmdi de kendim bir tane gruplama yapayım

df.groupby(["sex", "who"]).agg({"age": ["max", "min", "count"],
                                "survived": "mean"})
