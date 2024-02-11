# Amaç key değerini string value değerini de bir liste olan sözlük oluşşturmak
# sadece sayısal değişkenler için yapmak istiyoruz


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
# Yani biz yukarıda sayısal değişkenleri aldık eğer iki eşittir alsaydık bu sefer de kategorik
# değişkenleri almış olurduk


agg_list = ["mean", "min", "max", "sum"]
soz = {}
for col in num_cols:
    soz[col] = agg_list

# şimdi de bir dicktionary comprehension ile bu adımların aynısını yapalım

dic_comp = {col: agg_list for col in num_cols}

