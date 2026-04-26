import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df_clean = pd.read_csv("temp_clean.csv")

X = df_clean.drop("PFS_status", axis=1)
y = df_clean["PFS_status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

print("Model trained successfully!")

import joblib
joblib.dump(model, "temp_model.pkl")
joblib.dump((X_train, X_test, y_train, y_test), "temp_data.pkl")