import pandas as pd

s = pd.Series([1, 2, 3], index=["row1", "row2", "row3"])

type(s)
s.size  # boyut bilgisini döndürür yani içinde kaç eleman var
s.ndim  # kaç boyyutlu oldugunu yazdırır
s.head(3)  # baştan ilk üç elemanı getir
s.tail(2)  # sondan ilk iki elamanı al gel
s.values  # burada dikkat etmen gereken şey eğer values olarak çağırırsan bize array tipinde elemanları döndürür
s.index
s.dtype




