# UFC Fight Predictor

This project predicts the outcome of UFC fights using machine learning. Based on fighter performance data, it estimates:

- Fight winner
- Win probability
- Likely method of victory (KO, submission, or decision)

## Features

- Streamlit web app for real-time predictions
- Random Forest model for classification
- Precomputed efficiency metrics (striking and takedowns)
- Sample dataset included for testing

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/UFC-Fight-analysis
cd UFC-Fight-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app/app.py
```

## Data

The `ufc_fights_sample.csv` file contains a few example UFC matchups, including fighter stats and outcomes, used for model training and testing.

## Project Structure

```
UFC-Fight-analysis/
├── app/                    # Streamlit app
├── model/                  # Trained model storage
├── src/                    # Model training & prediction logic
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
├── ufc_fights_sample.csv   # Sample dataset
```

## License

This project is open source. Use it, modify it, and share it.