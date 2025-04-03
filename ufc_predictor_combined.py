import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import messagebox
import random

class UFCFightModel:
    def __init__(self, model, scaler):
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

# Load sample data
df = pd.read_csv("ufc_fights_sample.csv")
df = df.dropna(subset=[
    'A_SLpM', 'A_StrAcc', 'A_SubAtt', 'A_TDAtt', 'A_TDAcc', 'A_Age',
    'B_SLpM', 'B_StrAcc', 'B_SubAtt', 'B_TDAtt', 'B_TDAcc', 'B_Age', 'Winner', 'Fighter_A', 'Fighter_B'
])
df['Winner'] = df['Winner'].map({'A': 1, 'B': 0})

X = []
y = []
for _, row in df.iterrows():
    A = [row['A_SLpM'], row['A_StrAcc'], row['A_SubAtt'], row['A_TDAtt'], row['A_TDAcc'], row['A_Age']]
    B = [row['B_SLpM'], row['B_StrAcc'], row['B_SubAtt'], row['B_TDAtt'], row['B_TDAcc'], row['B_Age']]
    X.append(np.array(A) - np.array(B))
    y.append(row['Winner'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled, y)
train_model = UFCFightModel(model, scaler)

# Tkinter GUI
def show_fight():
    global current_row, fighter_A, fighter_B
    current_row = df.sample(1).iloc[0]

    fighter_A = {
        'SLpM': current_row['A_SLpM'],
        'StrAcc': current_row['A_StrAcc'],
        'SubAtt': current_row['A_SubAtt'],
        'TDLanded': current_row['A_TDAtt'],
        'TDAcc': current_row['A_TDAcc'],
        'Age': current_row['A_Age']
    }
    fighter_B = {
        'SLpM': current_row['B_SLpM'],
        'StrAcc': current_row['B_StrAcc'],
        'SubAtt': current_row['B_SubAtt'],
        'TDLanded': current_row['B_TDAtt'],
        'TDAcc': current_row['B_TDAcc'],
        'Age': current_row['B_Age']
    }

    info_A = f"Fighter A\n" + "\n".join([f"{k}: {v}" for k, v in fighter_A.items()])
    info_B = f"Fighter B\n" + "\n".join([f"{k}: {v}" for k, v in fighter_B.items()])

    label_A.config(text=info_A)
    label_B.config(text=info_B)
    name_label.config(text="")


def make_choice(user_pick):
    prediction = train_model.predict(fighter_A, fighter_B)
    actual_winner = "Fighter A" if current_row['Winner'] == 1 else "Fighter B"
    actual_name = current_row['Fighter_A'] if actual_winner == "Fighter A" else current_row['Fighter_B']
    your_name = current_row['Fighter_A'] if user_pick == "Fighter A" else current_row['Fighter_B']

    result = f"Your Pick: {user_pick} ({your_name})\nModel Prediction: {prediction['Winner']}\nActual Winner: {actual_winner} ({actual_name})\nWin Probability: {prediction['Win Probability']}\nVictory Method: {prediction['Victory Method']}"
    if user_pick == actual_winner:
        result += "\n\n🎉 Well done! You guessed it right."
    name_label.config(text=f"Fighter A: {current_row['Fighter_A']}    |    Fighter B: {current_row['Fighter_B']}")
    messagebox.showinfo("Fight Result", result)
    show_fight()

# GUI setup
root = tk.Tk()
root.title("🥋 UFC Fight Predictor")

explanation = (
    "\nTerm Guide:\n"
    "SLpM: Strikes Landed per Minute\n"
    "StrAcc: Striking Accuracy (%)\n"
    "SubAtt: Submission Attempts per Fight\n"
    "TDLanded: Takedowns Attempted\n"
    "TDAcc: Takedown Accuracy (%)\n"
    "Age: Fighter's age\n"
)

tk.Label(root, text="Choose the winner based on the stats below:", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text=explanation, font=("Courier", 10), justify="left").pack()

frame = tk.Frame(root)
frame.pack(pady=10)

label_A = tk.Label(frame, text="", justify="left", font=("Courier", 10))
label_A.grid(row=0, column=0, padx=20)
label_B = tk.Label(frame, text="", justify="left", font=("Courier", 10))
label_B.grid(row=0, column=1, padx=20)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_A = tk.Button(btn_frame, text="Pick Fighter A", command=lambda: make_choice("Fighter A"), width=20)
btn_A.grid(row=0, column=0, padx=10)
btn_B = tk.Button(btn_frame, text="Pick Fighter B", command=lambda: make_choice("Fighter B"), width=20)
btn_B.grid(row=0, column=1, padx=10)

name_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
name_label.pack(pady=5)

next_btn = tk.Button(root, text="Next Fight", command=show_fight, width=20)
next_btn.pack(pady=10)

show_fight()
root.mainloop()
