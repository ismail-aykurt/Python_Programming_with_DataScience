import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sbs.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()
# Veri görselleştirme işlemleri yapılacaksa bunlar da sayısal değişkenlerse en yaygın kullanımı istatistikte histon
# grafikleri ile kutu grafiğidir. Yok değişken kategorik bir değişken ise burda da sutun grafikk yeterli olur şuanlık
