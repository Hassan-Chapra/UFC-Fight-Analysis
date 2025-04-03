🥋 UFC Fight Predictor Booth Edition 🚀

This interactive UFC fight prediction game uses machine learning to simulate fight outcomes based on real-world fighter stats. Designed for booths or demo setups (or for fun), it challenges users to predict winners based on performance data — then compares their guess to the model and actual result.

---

📁 Files Included

- `ufc_predictor_combined.py` – Full-feature GUI script (used in booth)
- `ufc_data.csv` – Full dataset used for training the model
- `ufc_fights_sample.csv` – Sample fights with updated ages and actual UFC event names
- `requirements.txt` – Python dependencies list
- `README.md` – You're reading it!

---

🧠 What It Does

- Trains a machine learning model using UFC fight statistics (if model doesn't exist)
- Predicts:
  - 🏆 Winner
  - 📊 Win probability
  - 🥋 Method of victory (Decision or KO/Sub)
- GUI experience includes:
  - Stats-only preview to prevent bias
  - Pop-up after each fight showing:
    - Fighter names
    - Model prediction
    - Actual winner
    - UFC Event name (e.g. UFC 247: Jones vs Reyes)
  - 5-fight challenge format
  - 🎉 Celebrates perfect scores
  - 🏆 Announces new high scores (except first player)
  - Displays your score and current high score at the end

---

🚀 How to Use

🖥️ Booth Mode (GUI)

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Launch the predictor
   ```bash
   python ufc_predictor_combined.py
   ```

3. Follow on-screen instructions:
   - Enter name
   - Pick winners from stats
   - See how your picks stack up

---

⚙️ Stats Used

- **SLpM** – Strikes Landed per Minute
- **StrAcc** – Striking Accuracy (%)
- **SubAtt** – Submission Attempts per Fight
- **TDLanded** – Takedowns Attempted
- **TDAcc** – Takedown Accuracy (%)
- **Age** – Fighter’s age at the time of fight

---

📝 Notes

- Dataset includes real event names and accurate fighter ages at time of fight
- No internet needed – runs fully offline
- Random Forest model built with scikit-learn
- Built-in score tracking and session management

---

📄 License

Free to use for educational, experimental, and MMA-loving purposes.

Created with ❤️ by IE Sports Analytics.
