# UFC Fight Predictor

This project predicts UFC fight outcomes based on fighter statistics using a machine learning model.

## What It Does

- Predicts the winner between two UFC fighters
- Estimates win probability
- Suggests the most likely method of victory (KO, submission, or decision)

## Included

- `ufc_fights_sample.csv` — Sample UFC fight data for training or testing
- `requirements.txt` — Dependencies for running the model
- `model/` — Folder for saving trained ML models

## Getting Started

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/UFC-Fight-analysis
cd UFC-Fight-analysis
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Use the CSV**
You can load the dataset using:
```python
import pandas as pd
df = pd.read_csv("ufc_fights_sample.csv")
```

## Structure

```
UFC-Fight-analysis/
├── model/                  # Trained models (empty by default)
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
├── ufc_fights_sample.csv   # Sample UFC dataset
```

## License

Open-source and available for learning or experimentation.