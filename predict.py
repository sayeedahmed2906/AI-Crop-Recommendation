import pickle
import pandas as pd
from googletrans import Translator

# 🌐 Translator
translator = Translator()

# 📦 Load model
model = pickle.load(open("model.pkl", "rb"))

# 📊 Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# 🎯 Features
FEATURES = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']


# 🌐 Translate Kannada → English
def translate_to_english(text):
    try:
        translated = translator.translate(text, dest='en')
        return translated.text.lower()
    except:
        return text.lower()
    
def translate_to_kannada(text):
    try:
        translated = translator.translate(text, dest='kn')
        return translated.text
    except:
        return text

# 🎯 Extract keywords (Kannada + English)
def extract_keywords(text):
    text = text.lower()

    # 🌱 Soil
    if any(word in text for word in ["black", "ಕಪ್ಪು"]):
        soil = "black"
    elif any(word in text for word in ["red", "ಕೆಂಪು"]):
        soil = "red"
    else:
        soil = "alluvial"

    # 🌧 Rainfall
    if any(word in text for word in ["high", "more", "heavy", "ಹೆಚ್ಚು"]):
        rainfall = "high"
    elif any(word in text for word in ["low", "less", "ಕಡಿಮೆ"]):
        rainfall = "low"
    else:
        rainfall = "medium"

    # 🌡 Temperature
    if any(word in text for word in ["summer", "hot", "ಬೇಸಿಗೆ", "ಬಿಸಿ"]):
        temperature = "high"
    elif any(word in text for word in ["winter", "cold", "ಚಳಿ"]):
        temperature = "low"
    else:
        temperature = "medium"

    return soil, rainfall, temperature


# 🔥 FIXED FEATURE GENERATION (IMPORTANT)
def generate_features(soil, rainfall, temperature):

    filtered = df.copy()

    # 🌡 Temperature filter
    if temperature == "low":
        filtered = filtered[filtered["temperature"] < 20]
    elif temperature == "high":
        filtered = filtered[filtered["temperature"] > 25]
    else:
        filtered = filtered[(filtered["temperature"] >= 20) & (filtered["temperature"] <= 30)]

    # 🌧 Rainfall filter
    if rainfall == "low":
        filtered = filtered[filtered["rainfall"] < 100]
    elif rainfall == "high":
        filtered = filtered[filtered["rainfall"] > 200]
    else:
        filtered = filtered[(filtered["rainfall"] >= 100) & (filtered["rainfall"] <= 200)]

    # ⚠️ fallback
    if filtered.empty:
        filtered = df

    # ✅ PICK RANDOM ROW (THIS FIXES YOUR ISSUE)
    sample = filtered.sample(n=1)

    return sample[['N','P','K','temperature','humidity','ph','rainfall']].values[0]


# 🔮 Prediction function
def predict_crop(text):

    text = translate_to_english(text)

    soil, rainfall, temperature = extract_keywords(text)

    features = generate_features(soil, rainfall, temperature)

    input_df = pd.DataFrame([features], columns=FEATURES)

    prediction = model.predict(input_df)
    crop_name = prediction[0]
    crop_kn = translate_to_kannada(crop_name)

    return crop_name, crop_kn, soil, rainfall, temperature