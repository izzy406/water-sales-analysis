import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ojisd_water.csv")

print("Summary of monthly revenue and bottles sold:")
print(df.describe())

# Total outstanding credit for the year
df["Outstanding"] = df["Revenue"] - df["Cash_Collected"]
print("Total still owed:", df["Outstanding"].sum())

# Months with outstanding credit
print("Months with outstanding credit:")
df[df["Cash_Collected"] < df["Revenue"]]


# Plot cash vs revenue
plt.plot(df["Month"], df["Revenue"], marker="o", label="Revenue (Billed)")
plt.plot(df["Month"], df["Cash_Collected"], marker="o", label="Cash Collected")
plt.title("OJISD Water: Revenue vs Cash")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.show()
