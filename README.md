# Health Prediction System (Machine Learning + Streamlit)

A multi-disease prediction project that estimates risk for:
- Diabetes
- Heart Disease
- Stroke

The project includes model training notebooks, pre-trained model files, and a Streamlit web application for interactive predictions.

## Project Highlights

- End-to-end ML workflow for 3 healthcare classification tasks
- Comparison of multiple classifiers:
  - Logistic Regression
  - Random Forest
  - Decision Tree
  - AdaBoost
  - Voting Classifier (ensemble)
- Hyperparameter tuning with GridSearchCV
- Streamlit UI for easy user input and prediction display

## Project Structure

```text
.
|-- UI.py
|-- diabetes.ipynb
|-- HeartDiseaseTrain.ipynb
|-- Stroke.ipynb
|-- Data/
|   |-- diabetes.csv
|   |-- HeartDiseaseTrain-Test.csv
|   |-- healthcare-dataset-stroke-data.csv
|-- Pickle/
|   |-- DiabetesClassifier.pkl
|   |-- HeartDiseaseClassifier.pkl
|   |-- StrokeClassifier.pkl
|-- Pics/
```

## Model Performance (From Notebook Outputs)

### 1) Diabetes
- Logistic Regression: 0.9038
- Random Forest: 0.9904
- Decision Tree: 0.9519
- AdaBoost: 0.9327
- Voting Classifier: 0.9808

### 2) Heart Disease
- Logistic Regression: 0.8146
- Random Forest: 0.9854
- Decision Tree: 0.9854
- AdaBoost: 0.9073
- Voting Classifier: 0.9854

### 3) Stroke
- Logistic Regression: 0.7505
- Random Forest: 0.9393
- Decision Tree: 0.9364
- AdaBoost: 0.9393
- Voting Classifier: 0.9384

Notes:
- The Streamlit app loads and uses the saved models from the Pickle folder.
- Accuracy is reported from held-out test sets in the notebooks.

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- streamlit-navigation-bar
- Jupyter Notebook

## Installation

### 1) Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2) Create and activate a virtual environment (recommended)

Windows (PowerShell):
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the UI

Use this command from the project root:

```bash
python -m streamlit run UI.py
```

Then open the local URL printed in terminal (typically http://localhost:8501).

## How to Use the App

1. Open Home page for overview.
2. Select one of the disease tabs (Diabetes / Heart Disease / Stroke).
3. Enter patient features in the form.
4. Click the prediction button.
5. Read risk result and recommendations shown by the app.

## Re-Train Models (Optional)

If you want to regenerate or improve models:

1. Run each notebook:
   - diabetes.ipynb
   - HeartDiseaseTrain.ipynb
   - Stroke.ipynb
2. Ensure models are saved to:
   - Pickle/DiabetesClassifier.pkl
   - Pickle/HeartDiseaseClassifier.pkl
   - Pickle/StrokeClassifier.pkl
3. Re-run Streamlit app.

## Known Notes and Troubleshooting

### Scikit-learn pickle compatibility warnings
- Models were originally trained with an older scikit-learn release.
- If you see warnings like InconsistentVersionWarning, predictions can still run, but retraining in your current environment is recommended for long-term stability.

### Command not found: streamlit
If streamlit is not recognized, use:

```bash
python -m streamlit run UI.py
```

### Missing modules
Install dependencies again:

```bash
python -m pip install -r requirements.txt
```

## Team

- Khizar Ali
- Kashif Khan

## Disclaimer

This project is for educational purposes only and is not a substitute for professional medical diagnosis or treatment.
