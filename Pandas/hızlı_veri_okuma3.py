import pandas as pd
import seaborn as sbs



df = sbs.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.describe().T # burdaki metod ile verideki sayısal değerler için hızlı bir şekilde  veri analizi yapabildik. max, min

df.isnull().values.any()  # Burada verisetinde herhangi bir bozuk veri var mı yok mu öğreniyorz

df.isnull().sum()  # Burada ise bu eksikliklerin her bir değişken için kaçar adet eksik ooldugu bilgisi döner

df["sex"].value_counts()  # Burada da eldeki değişkenin kaçar adet gözlem birimleri oldugu bilgisi döndürüyor


data = {"ad": ["İsmail", "mehmet", "ali"],
        "şehir": ["Ankara", "İzmir", "Antalya"],
        "yaş": [20, 21, 23]}

my_data = pd.DataFrame(data)

my_data.shape
my_data.ndim
my_data.head()
my_data.tail()
my_data.dtypes
type(my_data)





