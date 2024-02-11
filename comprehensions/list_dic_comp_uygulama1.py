# Bir veri setindeki değişkenlerin isimlerini değiştirelim

# before:
# ["total", "spedding", "alcohol", "not_distracted", "no_previous", "ins_premium", "ins_losses", "abbrev"]

# after
# ["TOTAL", "SPEDDING", "ALCOHOL", "NOT_DISTRACTED", "NO_PREVIOUS", "INS_PREMIUM", "INS_LOSSES", "ABBREV"]

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df_columns = [col.upper() for col in df.columns]




