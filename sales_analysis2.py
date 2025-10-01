import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ojisd_water.csv")

print("Summary of monthly revenue and bottles sold:")
print(df.describe())


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,8))

# Line chart
ax1.plot(df["Month"], df["Revenue"], marker="o", color="blue")
ax1.set_title("Monthly Revenue")
ax1.set_ylabel("Revenue ($)")
ax1.grid(True)

# Bar chart
ax2.bar(df["Month"], df["Bottles_Sold"], color="turquoise")
ax2.set_title("Bottles Sold Each Month")
ax2.set_ylabel("Bottles Sold")

plt.tight_layout()
plt.show()
