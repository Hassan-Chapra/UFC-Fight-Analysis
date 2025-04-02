# 🥋 UFC Fight Predictor 🚀

This project predicts the outcome of a UFC fight based on fighter statistics using a trained machine learning model. It's a self-contained Python script — no web app, no API, just a command-line experience powered by real fight data.

## 📁 Files Included

- `ufc_predictor_combined.py` – All-in-one script (model training, prediction, CLI interface)
- `ufc_data.csv` – Full dataset for training the model
- `ufc_fights_sample.csv` – Small sample dataset for quick demos or testing
- `requirements.txt` – List of Python dependencies

## 🧠 What It Does

- Trains a machine learning model on UFC fight stats (if no model exists)
- Accepts fighter input (SLpM, accuracy, takedowns, age, etc.)
- Predicts:
  - 🏆 Winner
  - 📊 Win probability
  - 🥋 Method of victory (Decision or KO/Sub)

## 🚀 How to Use

1. **Install requirements**  
```bash
pip install -r requirements.txt
```

2. **Run the script**  
```bash
python ufc_predictor_combined.py
```

3. **Enter fighter stats when prompted**

If a model isn’t found, it will automatically train one using `ufc_data.csv`.


## ⚙️ Example Inputs
- Strikes Landed per Minute: 4.2  
- Striking Accuracy (%): 52  
- Submission Attempts per Fight: 0.6  
- Takedowns Landed per Fight: 1.8  
- Takedown Accuracy (%): 48  
- Age: 30

## 📝 Notes
- This tool is fully offline and runs in the terminal.
- Model and scaler are saved inside the script as a single object when trained.

## 📄 License

Free to use for educational, experimental, and nerdy combat sports purposes.

Created with ❤️ by IE Sports Analytics for MMA fans and data geeks 
