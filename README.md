🥋 UFC Fight Predictor Booth Edition 🚀

This interactive UFC fight prediction game uses machine learning to simulate fight outcomes based on real-world fighter stats. Designed for booths or demo setups, it challenges users to predict winners based on performance data — then compares their guess to the model and actual result.

---

📁 Files Included

- `ufc_predictor_combined.py` – Terminal-based all-in-one script
- `ufc_fight_interface.py` – GUI version for live demos (booth use)
- `ufc_data.csv` – Full dataset for training the model
- `ufc_fights_sample.csv` – Sample fights used in the GUI
- `requirements.txt` – Python dependencies list

---

🧠 What It Does

- Trains a machine learning model using UFC fight statistics
- Predicts:
  - 🏆 Winner
  - 📊 Win probability
  - 🥋 Method of victory (Decision or KO/Sub)
- In the GUI version:
  - Hides fighter names to reduce bias
  - Tracks user score out of 5 fights
  - 🎉 Celebrates perfect scores
  - 🏆 Announces new high scores (except for the first user)

---

🚀 How to Use

🖥️ GUI Mode (Booth Edition)

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Launch the GUI
   ```bash
   python ufc_fight_interface.py
   ```

3. Play!
   - Enter your name
   - Pick winners based on stats
   - See if you can out-predict the model

---

⚙️ Stats Used for Prediction

- SLpM – Strikes Landed per Minute  
- StrAcc – Striking Accuracy (%)  
- SubAtt – Submission Attempts  
- TDLanded – Takedowns Attempted  
- TDAcc – Takedown Accuracy (%)  
- Age – Fighter age at the time of the bout

---

📝 Notes

- Fully offline, no internet or API required
- GUI built with Tkinter (easy to run on any Python setup)
- Backend powered by Random Forest (via scikit-learn)
- Unique fights per session (no repeats in 5-round runs)

---

📄 License

Free to use for educational, experimental, and MMA-loving purposes.

Created with ❤️ by IE Sports Analytics for MMA fans and Data nerds
