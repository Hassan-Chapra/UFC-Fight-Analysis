# UFC-Fight-analysis
Predict UFC fights using machine learning and real fighter stats.
# 🥋 UFC Fight Predictor

This project predicts UFC fight outcomes based on fighter stats using machine learning. It uses a Random Forest model trained on historical UFC data to estimate:

- 🏆 Fight winner
- 📊 Win probability
- 🥊 Likely method of victory (KO/Sub/Decision)

## 🔧 Features
- Live web app (Streamlit)
- Fighter stats input and real-time prediction
- Efficiency metrics built from raw stats
- Includes preprocessing, model training, and prediction scripts

## 🧪 Example Stats Input
- SLpM: Strikes Landed per Minute
- SApM: Strikes Absorbed per Minute
- Takedown Accuracy/Defense
- Submission Attempts
- Average Fight Time
- Age

## 📦 Run It Locally
```bash
git clone https://github.com/yourusername/UFC-Fight-Predictor
cd UFC-Fight-Predictor
pip install -r requirements.txt
streamlit run app/app.py
```

## 📁 Folder Structure
```
UFC-Fight-Predictor/
├── data/                  # Sample datasets
├── model/                 # Trained model file
├── README.md              # Project documentation
└── requirements.txt       # Dependencies
```

## ☁️ Deployment
Host via [Streamlit Cloud](https://streamlit.io/cloud) or [Hugging Face Spaces](https://huggingface.co/spaces).

---
Built with ❤️ for MMA fans and data nerds.
