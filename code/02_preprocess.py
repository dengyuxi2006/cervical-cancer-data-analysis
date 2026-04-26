import pandas as pd

df = pd.read_csv("temp_df.csv")

df["total_dose"] = df["dose1"] + df["dose2"] + df["dose3"] + df["dose4"] + df["dose5"] + df["dose6"] + df["dose7"]

features = ["age", "path", "diff", "stage", "total_dose", "meand", "SCC", "CCRT", "PFS_status"]
df_clean = df[features].dropna()

print("Preprocessing done")
print("Clean samples:", df_clean.shape[0])

df_clean.to_csv("temp_clean.csv", index=False, encoding="utf-8-sig")