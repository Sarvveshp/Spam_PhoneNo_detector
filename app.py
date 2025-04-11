from flask import Flask, render_template, request
import joblib
from utils.features import extract_features
from pymongo import MongoClient

app = Flask(__name__)
model = joblib.load("model.pkl")

client = MongoClient("mongodb://localhost:27017")
db = client["spam_db"]
collection = db["reported"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    show_report = False
    number = ""

    if request.method == "POST":
        number = request.form["number"]

        if collection.find_one({"number": number}):
            result = "⚠️ Number found in reported list. It's Spam."
        else:
            features = extract_features(number)
            prediction = model.predict([features])[0]
            result = "✅ Not Spam" if prediction == 0 else "❌ Likely Spam"
            show_report = (prediction == 0)  # Only allow report if model says not spam

    return render_template("index.html", result=result, show_report=True, number=number)



@app.route("/report", methods=["POST"])
def report():
    number = request.form["number"]
    collection.insert_one({"number": number})
    return f"<p>{number} has been reported as spam. <a href='/'>Go back</a></p>"


@app.route("/reports")
def reports():
    reported_numbers = list(collection.find())
    return render_template("reports.html", reported_numbers=reported_numbers)

if __name__ == "__main__":
    app.run(debug=True)
