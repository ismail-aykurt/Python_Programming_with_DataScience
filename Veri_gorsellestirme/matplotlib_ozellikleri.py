import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

# ########## plot ##########
# çizge grafikleri için kullanılır
x = np.array([1, 8, 10])
y = np.array([0, 150, 200])
plt.plot(x, y)  # Burada sadece çizgi bir grafik olarak aldık
plt.show()

plt.plot(x, y, "o")
plt.show()  # Burda da grafiği noktalar haline getirdik. İstediğimiz
# birden fazla nokta kullanalım

x = np.array([2, 4, 6, 8])
y = np.array([1, 3, 5, 9])
plt.plot(x, y)
plt.show()
# Şimdi de noktaları ekleyelim. Dikkat eğer grafiği çalıştırdıktan sonra kapatmadan başka bir grafik çalştırırsan
# çalışan grafik diğer grafiğin üstüne gelir

plt.plot(x, y, "o")
plt.show()

# ######### marker(işaretliyici özellik)  ############

y = np.array([1, 25, 11, 35])
plt.plot(y, marker="D")
plt.ylabel("y ekseni")
plt.show()
# Burada istediğimiz gibi bir işaretleme verebiliriz daha çok araştırma ismail git ve internetten bakkkk
# yaygın  ma
# markerler == [o, * . , s P D x + .....]


# Line

y = np.array([1, 5, 8, 12, 20])
plt.plot(y)
plt.show()
# Şimdi bu şekilde sade bir çizgi oldu bunu biraz daha özelleştirelim

plt.plot(y, linestyle="dashed")  # Burada kesikli hale getirdik
plt.plot(y, linestyle="dotted")  # Burada da noktalı hale aldık
plt.plot(y, linestyle="dashdot")  # hem noktalı hemde kesikli zaten bu uçu var

plt.plot(y, linestyle="dashed", color="r", marker="D", markersize=4)
# Burada daha da özelleştirdik ve markersize ile de işaretleyicimizin ne kadar vurgu yapmasının boyutunu girdik


# Multiple lines

x = np.array([1, 2, 50, 6, 70])
y = np.array([10, 5, 12, 36, 17])
plt.plot(x, linestyle="dashed", color="b", marker="P", markersize=6)
plt.plot(y, linestyle="dashdot", color="r", marker="D", markersize=8)
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.title("DATA MANIPULATION")
plt.show()
# Burada iki adet veriyi yazmak istersek üstüste yazabilmek için ayrı ayrı yazıp çağırmak gerekiyor


# ###### LABELS(ETİKETLER)########
# burda işimize en çok yarayacak olan kısım aslında tam olarak burası
x = np.array([8, 85, 9, 19, 10, 15, 11, 5, 12, 15])
y = np.array([24, 25, 20, 70, 80, 29, 30, 10, 32, 30])
plt.plot(x, linestyle="dashdot", color="r", marker="D", markersize=8)
plt.plot(y, linestyle="dashed", color="b", marker="P", markersize=7)
plt.title("DATA SCIENCE")
plt.xlabel("data x")
plt.ylabel("data y")
plt.grid()

# ####### Subplots #######
# Şimdi de birden fazla grafiği nasıl çizeceğimize bakalım

x = np.array([1, 2, 5, 7, 8, 12, 4])
y = np.array([4, 12, 5, 36, 31, 10, 12])
plt.subplot(1, 3, 1)  # Şimdi ben burada bana 1 e 3 lük bir grafik yap dedim ve 1 incisini aloyırum dedim
plt.plot(x, y,  color="r", marker="*", markersize=5)
plt.title("Grafik 1")
plt.xlabel("grf1 x")
plt.ylabel("grf1 y")
plt.grid()


# Şİmdi de ikincisini alalım
x = np.array([1, 20, 15, 7, 8, 12, 4])
y = np.array([4, 12, 15, 6, 31, 10, 12])
plt.subplot(1, 3, 2)  # Şimdi ben burada bana 1 e 3 lük bir grafik yap dedim ve 1 incisini aloyırum dedim
plt.plot(x, y,  color="b", marker="*", markersize=5)
plt.title("Grafik 2")
plt.xlabel("grf2 x")
plt.ylabel("grf2 y")
plt.grid()

# 3.grafiği alalım
x = np.array([10, 20, 5, 7, 8, 12, 4])
y = np.array([40, 12, 5, 36, 31, 10, 12])
plt.subplot(1, 3, 3)  # Şimdi ben burada bana 1 e 3 lük bir grafik yap dedim ve 1 incisini aloyırum dedim
plt.plot(x, y,  color="y", marker="D", markersize=5)
plt.title("Grafik 3")
plt.xlabel("grf3 x")
plt.ylabel("grf3 y")
plt.grid()
