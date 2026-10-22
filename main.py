import numpy as np
import pandas as pd

df = pd.read_csv("sales.csv", encoding="latin1")

print("-------------- Basic Information --------------")
print(df.head())
print(df.tail())
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Index:", df.index)
print(df.dtypes)
df.info()
print(df.describe())

print("-------------- Series and DataFrame --------------")
sales_series = df["Sales"]
print(sales_series.head())

small_df = df[["Region", "Category", "Sales", "Profit"]]
print(small_df.head())

print("-------------- Selecting Rows --------------")
print(df.iloc[0])
print(df.loc[0:4, ["Region", "Sales"]])

print("-------------- Data Cleaning --------------")
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

df["Order Date"] = pd.to_datetime(df["Order Date"])
print(df["Order Date"].dtype)

print("-------------- New Columns --------------")
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Profit Margin %"] = np.round(df["Profit"] / df["Sales"] * 100, 2)
print(df[["Year", "Month", "Profit Margin %"]].head())

print("-------------- NumPy --------------")
sales = df["Sales"].to_numpy()
profit = df["Profit"].to_numpy()

print("Total Sales :", np.round(np.sum(sales), 2))
print("Total Profit:", np.round(np.sum(profit), 2))
print("Average     :", np.round(np.mean(sales), 2))
print("Median      :", np.round(np.median(sales), 2))
print("Std Dev     :", np.round(np.std(sales), 2))
print("Max         :", np.max(sales))
print("Min         :", np.min(sales))
print("Loss orders :", np.sum(profit < 0))

print("-------------- Filtering --------------")
print("Sales above 1000:", df[df["Sales"] > 1000].shape[0])
print("Loss-making orders:", df[df["Profit"] < 0].shape[0])
print("West and Technology:", df[(df["Region"] == "West") & (df["Category"] == "Technology")].shape[0])

print("-------------- Sorting --------------")
print(df.sort_values("Profit", ascending=False)[["State", "Sub-Category", "Profit"]].head(5))
print(df.sort_values("Profit")[["State", "Sub-Category", "Profit"]].head(5))

print("-------------- Group By --------------")
print(df.groupby("Region")["Sales"].sum())
print(df.groupby("Category")["Profit"].sum())
print(df.groupby("Sub-Category")["Profit"].sum().sort_values())
print(df.groupby("Year")["Sales"].sum())
print(df["Segment"].value_counts())

print("-------------- Insights --------------")
print("Best region     :", df.groupby("Region")["Sales"].sum().idxmax())
print("Best category   :", df.groupby("Category")["Profit"].sum().idxmax())
print("Worst sub-category:", df.groupby("Sub-Category")["Profit"].sum().idxmin())

df.groupby("Region")[["Sales", "Profit"]].sum().to_csv("region_summary.csv")
print("Saved region_summary.csv")