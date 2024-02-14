import pandas as pd
import seaborn as sbs

df = sbs.load_dataset("tips")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df.loc[(df["size"] < 30) & (df["total_bill"] > 10)].mean