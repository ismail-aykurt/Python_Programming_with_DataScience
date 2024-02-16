# MATPLOTLIB and SEABORN
"""
Matplotlib:
-----------
Düşük seviyeli, esnek, geniş kontrol sağlar.
Temel grafik kütüphanesidir.
Özelleştirme için daha fazla çaba gerektirebilir.
Varsayılan temalar ve renk paletleri sade olabilir.
Genel grafik oluşturmak için kullanılır.

Seaborn:
--------
Matplotlib üzerine inşa edilmiş, yüksek seviyeli, kullanımı kolay.
Modern ve çekici varsayılan temalar sunar.
İstatistiksel grafiklere odaklanır.
Daha az kodla çekici grafikler oluşturmayı destekler.
Hızlı başlangıç için idealdir."""

# Eğer eldeki veri kategorik = sutun grafik   countplot and bar
# Eğer değişken sayısal ise = histogram(hist) and boxplot

# Kategorik değiken görselleştirme

import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sbs.load_dataset("titanic")
df.head()
df["sex"].value_counts().plot(kind="bar")
plt.show()
