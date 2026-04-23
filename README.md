# 🌾 AI Crop Recommendation System

An intelligent crop recommendation system that suggests the best crop based on soil and environmental conditions using Machine Learning.

---

## 📌 Project Overview

This project helps farmers choose suitable crops by analyzing:

* Soil nutrients (N, P, K)
* Temperature
* Humidity
* pH value
* Rainfall

It also supports:

* 🌐 Kannada + English input
* 🎤 Voice-based interaction
* 🖥️ Interactive web interface

---

## 🧠 Technologies Used

* Python
* Streamlit (Frontend)
* Scikit-learn (Machine Learning)
* Random Forest Algorithm
* Google Translate API (Kannada support)
* SpeechRecognition (Voice input)

---

## ⚙️ How It Works

1. User provides input (text or voice)
2. Kannada input is translated to English
3. Keywords are extracted (soil, rainfall, temperature)
4. Features are generated using dataset
5. Machine Learning model predicts the best crop
6. Output is displayed in English + Kannada

---

## 🏗️ System Architecture

```
User Input (Text / Voice)
        ↓
Speech Recognition (if voice)
        ↓
Translation (Kannada → English)
        ↓
Keyword Extraction
        ↓
Feature Generation (N, P, K, etc.)
        ↓
Trained ML Model (Random Forest)
        ↓
Crop Prediction
        ↓
Display Result (English + Kannada + Image)
```

---

## 📊 Machine Learning Model

* Algorithm: Random Forest Classifier
* Dataset: Crop Recommendation Dataset
* Train-Test Split: 80/20
* Accuracy: ~95%+

---

## 📁 Project Structure

```
├── app.py                 # Streamlit frontend
├── predict.py             # Prediction logic
├── train.py               # Model training
├── test.py                # Testing script
├── voice_input.py         # Voice input handling
├── model.pkl              # Trained model
├── Crop_recommendation.csv
├── images/
└── requirements.txt
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the app:

```
streamlit run app.py
```

3. Open in browser:

```
http://localhost:8501
```

---

## 📱 Mobile Usage

The application can be accessed on mobile browsers or converted into a mobile app using WebView or Flutter.

---

## 🌟 Features

* AI-based crop prediction
* Kannada language support
* Voice input functionality
* Simple and user-friendly UI
* Real-time results

---

## 🚀 Future Improvements

* Real-time weather API integration
* Soil sensor data input
* Mobile app development
* Fertilizer recommendation system

---

## 👨‍💻 Author

SAYEED AHMED,
RAYAAN SHARIFF,
Mirza Zeeshan Baig.

---

## 📌 Conclusion

This project demonstrates how AI can assist farmers in making better agricultural decisions, improving productivity and efficiency.

---
