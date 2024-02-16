# SEABORN
import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt

df = sbs.load_dataset("tips")
df.head()
df["sex"].value_counts()
sbs.countplot(x=df["sex"], data=df)  # evet burada daha gelişmiş bir şekilde aldı değerleri bir de matplotlibden yap

df["sex"].value_counts().plot(kind="bar")  # Evet burda da daha sade bir grafik oldu


# SAYISAL DEĞİŞKEN GÖRSELLEŞTİRME

sbs.boxplot(x=df["total_bill"])
plt.show()

sbs.histplot(x=df["total_bill"])
plt.show()

