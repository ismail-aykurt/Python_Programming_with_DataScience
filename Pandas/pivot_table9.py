# Pivot table

import pandas as pd
import seaborn as sbs

pd.set_option("display.max_columns", None)
df = sbs.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked")
# Burda ilk değer values yani hangi değeri hesaplayayım mantıgı ikincisi satırda ne göstereyim der 3. ise sütun
# değerini alır ve bize bir daat frame döndürür

df.pivot_table("survived", ["sex", "class"], "embarked")