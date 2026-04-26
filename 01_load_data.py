import pandas as pd

file_path = r"E:\智慧肿瘤-大模型\宫颈癌的近距离放疗的愈后分析\1-数据处理\data_clean_v2.xlsx"
df = pd.read_excel(file_path)

print("Data loaded successfully")
print("Shape:", df.shape)
print(df.head())

df.to_csv("temp_df.csv", index=False, encoding="utf-8-sig")