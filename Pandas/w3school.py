import pandas as pd

df2 = pd.read_csv("DataSets/data.csv")

df2.info()

df2.isnull().values.any()

df2.isnull().sum()

df3 = df2.dropna()
df3.isnull().values.any()


mean1 = df3["Calories"].mean()

df2["Calories"].fillna(mean1, inplace=True)

df2.to_string()