import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ojisd_water.csv")

print("Summary of monthly revenue and bottles sold:")
print(df.describe())

# 1. Profit calculation for each month
df["Profit"] = df["Revenue"] - (df["Cost_of_Goods"] + df["Expenses"])
print("Monthly Profit:")
print(df[["Month", "Profit"]])

# 2. Total yearly profit
print("Total Yearly Profit: $", df["Profit"].sum())

# 3. Outstanding credit (Revenue - Cash collected)
df["Outstanding"] = df["Revenue"] - df["Cash_Collected"]
print("Total Still Owed: $", df["Outstanding"].sum())


# 5. Plot Profit over the year
plt.figure(figsize=(8,4))
plt.plot(df["Month"], df["Profit"], marker="o", color="green")
plt.title("OJISD Water: Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit ($)")
plt.grid(True)
plt.show()


#5 Identify the best month
best = df.loc[df['Revenue'].idxmax()]
print(f"Best month: {best['Month']} with revenue of ${best['Revenue']} and {best['Bottles_Sold']} bottles sold.")







