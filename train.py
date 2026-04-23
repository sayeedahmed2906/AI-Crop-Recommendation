import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# 📥 Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# 🎯 Features & Target
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# 🔀 Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🌲 Train Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# 🔮 Predict
y_pred = model.predict(X_test)

# 📊 Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("✅ Model Accuracy:", accuracy)

# 💾 Save model
pickle.dump(model, open("model.pkl", "wb"))

print("🎉 Model trained and saved as model.pkl")