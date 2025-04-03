🥋 UFC Fight Predictor Booth Edition 🚀

This interactive UFC fight prediction game uses machine learning to simulate fight outcomes based on real-world fighter stats. Designed for booths or demo setups, it challenges users to predict winners based on performance data — then compares their guess to the model and actual result.

---

📁 Files Included

- `ufc_predictor_combined.py` – Full script: trains the model and runs the interactive GUI
- `ufc_data.csv` – Full UFC fight data used to train the model
- `ufc_fights_sample.csv` – Small curated fight set used in the game
- `requirements.txt` – Python dependencies

---

🧠 How It Works

- Trains a machine learning model (Random Forest) on hundreds of real UFC fights from `ufc_data.csv`
- Calculates differences between fighters' stats to use as features
- Uses `StandardScaler` to normalize stat differences
- Predicts fight outcomes based on:
  - 🏆 Winner
  - 📊 Win Probability
  - 🥋 Method of Victory (Decision or KO/Sub)
- GUI powered by `tkinter` lets users play a 5-fight challenge, predicting winners based on stats only

---

🎮 Gameplay Experience

- Fighters shown as "Fighter A" vs "Fighter B" with anonymized stats
- Users pick a winner based on stats alone
- The app reveals:
  - Actual fighter names
  - Model prediction and probability
  - Real UFC event name (e.g. UFC 247: Jones vs Reyes)
  - Whether the user guessed correctly
- Score is tracked over 5 fights
- Celebrates perfect scores and announces new records

---

📊 Stats Used in Prediction

- SLpM – Strikes Landed per Minute
- StrAcc – Striking Accuracy (%)
- SubAtt – Submission Attempts per Fight
- TDLanded – Takedowns Attempted
- TDAcc – Takedown Accuracy (%)
- Age – Fighter’s age at time of fight

---

🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
python ufc_predictor_combined.py
```

3. Play through the fight challenge in the GUI!

---

📝 Notes

- The model is trained on full data (`ufc_data.csv`) but game fights are sampled from `ufc_fights_sample.csv`
- All fights in the sample include real ages and event names
- Offline, fast, and beginner-friendly — perfect for booths and demos

---

📄 License

Free to use for educational, experimental, and MMA-loving purposes.

Created with ❤️ by IE Sports Analytics
