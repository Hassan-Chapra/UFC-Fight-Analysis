# ufc_event_demo.py

import joblib
import numpy as np

def predict_fight(fighter_A, fighter_B):
    data = joblib.load("ufc_model.pkl")
    model = data['model']
    scaler = data['scaler']

    def extract_features(f):
        return np.array([
            f['SLpM'], f['StrAcc'], f['SubAtt'],
            f['TDLanded'], f['TDAcc'], f['Age']
        ])

    # Calculate feature difference (A - B)
    A_features = extract_features(fighter_A)
    B_features = extract_features(fighter_B)
    input_vector = A_features - B_features

    # Scale and predict
    input_scaled = scaler.transform([input_vector])
    prob = model.predict_proba(input_scaled)[0]
    winner = "Fighter A" if prob[1] > 0.5 else "Fighter B"
    method = "Decision" if max(prob) < 0.7 else "KO/Sub"

    return {
        "Winner": winner,
        "Win Probability": f"{max(prob) * 100:.1f}%",
        "Victory Method": method
    }

def main():
    print("🥋 UFC Fight IQ Challenge
")
    print("Enter stats for each fighter below.
")

    def get_fighter_input(name):
        print(f"--- {name} ---")
        return {
            'SLpM': float(input("Strikes Landed per Minute: ")),
            'StrAcc': float(input("Striking Accuracy (%): ")),
            'SubAtt': float(input("Submission Attempts per Fight: ")),
            'TDLanded': float(input("Takedowns Landed per Fight: ")),
            'TDAcc': float(input("Takedown Accuracy (%): ")),
            'Age': float(input("Age: "))
        }

    fighter_A = get_fighter_input("Fighter A")
    print()
    fighter_B = get_fighter_input("Fighter B")

    print("
🤖 Predicting fight outcome...
")
    result = predict_fight(fighter_A, fighter_B)

    print("=== Prediction Result ===")
    print(f"Winner: {result['Winner']}")
    print(f"Win Probability: {result['Win Probability']}")
    print(f"Victory Method: {result['Victory Method']}")
    print("=========================")

if __name__ == "__main__":
    main()