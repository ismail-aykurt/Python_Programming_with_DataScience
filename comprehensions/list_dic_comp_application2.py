# Şimdi de içinde INS geçen kelimelerin başına FLAG diğerleerinin başına NO_FLAG koyalım

import seaborn as sb
df = sb.load_dataset("car_crashes")
df.columns

df_columns = [col.upper() for col in df.columns]

df_columns1 = ["FLAG_" + col if "INS" in col else "NO_FLAG" + col for col in df_columns]




