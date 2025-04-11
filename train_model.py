import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from utils.features import extract_features

# Load dataset
df = pd.read_csv("data/spam_dataset.csv")
X = df["number"].astype(str).apply(extract_features).tolist()
y = df["is_spam"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("Model saved.")
