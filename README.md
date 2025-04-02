# 🥋 UFC Fight IQ Predictor (CLI Version)

This command-line tool predicts the outcome of a UFC fight based on fighter stats using a pre-trained machine learning model.

## 🔍 What It Does
- Predicts the winner between two UFC fighters
- Calculates win probability
- Suggests likely method of victory (KO/Sub or Decision)

## 🧠 Stats Used
- Strikes Landed per Minute (SLpM)
- Striking Accuracy (%)
- Submission Attempts per Fight
- Takedowns Landed per Fight
- Takedown Accuracy (%)
- Fighter Age

## 📦 Files Included
- `ufc_event_demo.py`: CLI program for entering stats and predicting outcomes
- `ufc_model.pkl`: Trained Random Forest model with scaler
- `requirements.txt`: Required Python packages

## 🚀 How to Use

1. Make sure you have Python 3 installed.

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the predictor:
```bash
python ufc_event_demo.py
```

4. Enter stats for Fighter A and Fighter B when prompted.

## 📄 License

Open-source and free to use for educational and experimental purposes.