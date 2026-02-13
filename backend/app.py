from flask import Flask, jsonify
from models.model import analyze_gameplay

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Gaming Coach Backend Running"

@app.route("/analyze")
def analyze():
    result = analyze_gameplay({})
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
