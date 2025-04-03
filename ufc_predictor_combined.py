# ufc_predictor_combined.py

import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

class UFCFightModel:
    def __init__(self, model=None, scaler=None):
        self.model = model
        self.scaler = scaler

    def predict(self, fighter_A, fighter_B):
        def extract_features(f):
            return np.array([
                f['SLpM'], f['StrAcc'], f['SubAtt'],
                f['TDLanded'], f['TDAcc'], f['Age']
            ])
        A = extract_features(fighter_A)
        B = extract_features(fighter_B)
        diff = A - B
        scaled = self.scaler.transform([diff])
        prob = self.model.predict_proba(scaled)[0]
        return {
            "Winner": "Fighter A" if prob[1] > 0.5 else "Fighter B",
            "Win Probability": f"{max(prob) * 100:.1f}%",
            "Victory Method": "Decision" if max(prob) < 0.7 else "KO/Sub"
        }

def train_and_save_model():
    df = pd.read_csv("data/data.csv")
    df = df[df["Winner"].isin(["Red", "Blue"])].copy()

    features = [
        'R_avg_SIG_STR_landed', 'R_avg_SIG_STR_pct', 'R_avg_SUB_ATT',
        'R_avg_TD_landed', 'R_avg_TD_pct',
        'B_avg_SIG_STR_landed', 'B_avg_SIG_STR_pct', 'B_avg_SUB_ATT',
        'B_avg_TD_landed', 'B_avg_TD_pct',
        'R_age', 'B_age'
    ]
    df = df.dropna(subset=features)
    df['Winner'] = df['Winner'].map({'Red': 1, 'Blue': 0})

    X = []
    for _, row in df.iterrows():
        r = [row[f] for f in features[:6]]
        b = [row[f] for f in features[6:]]
        X.append(np.array(r) - np.array(b))

    X = np.array(X)
    y = df['Winner'].values

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    combined_model = UFCFightModel(model, scaler)
    joblib.dump(combined_model, "model/ufc_model_single.pkl")

def main():
    if not os.path.exists("model/ufc_model_single.pkl"):
        os.makedirs("model", exist_ok=True)
        print("Training model from data...")
        train_and_save_model()

    model = joblib.load("model/ufc_model_single.pkl")

    print("🥋 UFC Fight IQ Challenge
")
    print("Enter stats for each fighter below.
")

    def get_input(name):
        print(f"--- {name} ---")
        return {
            'SLpM': float(input("Strikes Landed per Minute: ")),
            'StrAcc': float(input("Striking Accuracy (%): ")),
            'SubAtt': float(input("Submission Attempts per Fight: ")),
            'TDLanded': float(input("Takedowns Landed per Fight: ")),
            'TDAcc': float(input("Takedown Accuracy (%): ")),
            'Age': float(input("Age: "))
        }

    fighter_A = get_input("Fighter A")
    print()
    fighter_B = get_input("Fighter B")

    result = model.predict(fighter_A, fighter_B)
    print("\n=== Prediction Result ===")
    print(f"Winner: {result['Winner']}")
    print(f"Win Probability: {result['Win Probability']}")
    print(f"Victory Method: {result['Victory Method']}")
    print("=========================")

# Create a ready-to-use model object so other scripts can import it
if __name__ != "__main__":
    if not os.path.exists("model/ufc_model_single.pkl"):
        os.makedirs("model", exist_ok=True)
        train_and_save_model()
    train_model = joblib.load("model/ufc_model_single.pkl")
