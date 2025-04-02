# 🥋 UFC Fight Predictor

This project predicts UFC fight outcomes using machine learning and real fighter stats.

## 🔍 What It Does

- 🏆 Predicts the winner between two UFC fighters
- 📊 Estimates win probability
- 🥊 Suggests the most likely method of victory (KO, submission, or decision)

## 📦 Included

- `ufc_fights_sample.csv` — Sample UFC fight data for training or testing
- `requirements.txt` — Python dependencies
- `model/` — Folder for saving trained ML models

## 🚀 Getting Started

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/UFC-Fight-analysis
cd UFC-Fight-analysis
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Use the Sample Data**
You can load and explore the sample dataset with:
```python
import pandas as pd
df = pd.read_csv("ufc_fights_sample.csv")
```

## 🗂️ Project Structure

```
UFC-Fight-analysis/
├── model/                  # Trained models (empty by default)
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
├── ufc_fights_sample.csv   # Sample UFC dataset
```

## 📄 License

Open-source and free to use for learning, experimentation, and further development.