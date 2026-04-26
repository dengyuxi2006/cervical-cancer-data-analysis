import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

df_clean = pd.read_csv("temp_clean.csv")

print(df_clean.describe().round(2))

plt.figure(figsize=(7,4))
sns.histplot(df_clean["age"], kde=True)
plt.title("Age Distribution")
plt.savefig("age_dist.png", dpi=300)
plt.close()

plt.figure(figsize=(6,4))
sns.countplot(x="stage", data=df_clean)
plt.title("Stage Distribution")
plt.savefig("stage_dist.png", dpi=300)
plt.close()

plt.figure(figsize=(10,8))
sns.heatmap(df_clean.corr(), cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("corr_heatmap.png", dpi=300)
plt.close()

print("Statistical images saved!")