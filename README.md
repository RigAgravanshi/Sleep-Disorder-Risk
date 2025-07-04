# Sleep Disorder Risk Predictor 💤

This is a simple **Sleep Disorder Risk Assessment Model** that predicts the likelihood of sleep disorders (None, Insomnia, Sleep Apnea) with a **91% accuracy**. 

Check it out here: https://sleep-disorder-risk-ipv.streamlit.app/

## Features ✨
- **Input Parameters**: Collects user data on:
  - Gender, Age, Sleep Duration (hours), Quality of Sleep (1–10)
  - Physical Activity Level (minutes/day), Stress Level (1–10)
  - BMI Category, Blood Pressure, Heart Rate (bpm), Daily Steps
- **Prediction**: Classifies risk of sleep disorders (None, Insomnia, Sleep Apnea)
- **Performance**: Achieves **91% accuracy** and **0.91 F1-score** using XGBoost
- **Interactive UI**: Deployed as a user-friendly web app via Streamlit Community Cloud

## Tech Stack 🛠️
- **Jupyter Notebook**: For model development and experimentation
- **Python Libraries**:
  - `pandas` & `numpy`: Data processing and manipulation
  - `scikit-learn`: Machine learning utilities and preprocessing
  - `xgboost`: Final model  
  - `pickle`: Serialization of the trained model
- **Streamlit**: Web app deployment for user input and predictions

## Project Structure 📂
- `sleeper.py`: Main Streamlit app script
- `sleep.pkl`: Trained XGBoost model
- `scaler.pkl`: Standard scaler, which was fit on the Test data
- `requirements.txt`: Python dependencies
- `Sleep_Disorder_Risk.ipynb`: Jupyter notebook
- `Sleep_health_and_lifestyle_dataset.csv`: Input dataset used to train the model
