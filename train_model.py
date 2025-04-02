# train_model.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
df = pd.read_csv("ufc_fights_sample.csv")

# Define efficiency functions
def compute_efficiency(row, prefix):
    strike_eff = (row[f"{prefix}_SLpM"] - row[f"{prefix}_SApM"]) / row[f"{prefix}_SLpM"] if row[f"{prefix}_SLpM"] != 0 else 0
    td_eff = row[f"{prefix}_TDAtt"] * row[f"{prefix}_TDAcc"] / 100
    return strike_eff, td_eff

# Prepare features and labels
X = []
y = []

for _, row in df.iterrows():
    A_strike_eff, A_td_eff = compute_efficiency(row, "A")
    B_strike_eff, B_td_eff = compute_efficiency(row, "B")

    features_A = [
        row["A_SLpM"], row["A_SApM"], row["A_StrAcc"], row["A_StrDef"],
        row["A_TDAcc"], row["A_TDDef"], row["A_SubAtt"], row["A_TDAtt"],
        row["A_Time"], row["A_Age"], A_strike_eff, A_td_eff
    ]
    
    features_B = [
        row["B_SLpM"], row["B_SApM"], row["B_StrAcc"], row["B_StrDef"],
        row["B_TDAcc"], row["B_TDDef"], row["B_SubAtt"], row["B_TDAtt"],
        row["B_Time"], row["B_Age"], B_strike_eff, B_td_eff
    ]
    
    X.append(np.array(features_A) - np.array(features_B))
    y.append(1 if row["Winner"] == "A" else 0)

X = np.array(X)
y = np.array(y)

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model/ufc_model.pkl")
print("✅ Model trained and saved to model/ufc_model.pkl")