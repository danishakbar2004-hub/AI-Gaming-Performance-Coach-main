from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests
import random

app = Flask(__name__, template_folder="../templates")
CORS(app)

GOOGLE_CLIENT_ID = "861763798863-bq6tkk0ah4kp6btmgnd97gfc64hpsliq.apps.googleusercontent.com"


@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# FIXED GOOGLE VERIFY
# -------------------------------
@app.route("/verify", methods=["POST"])
def verify():
    try:
        data = request.get_json()
        token = data.get("token")  # ✅ matches frontend

        if not token:
            return jsonify({"status": "error"})

        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_CLIENT_ID,
            clock_skew_in_seconds=10
        )

        if idinfo["aud"] != GOOGLE_CLIENT_ID:
            return jsonify({"status": "error"})

        return jsonify({
            "status": "success",
            "user": {
                "name": idinfo.get("name"),
                "email": idinfo.get("email")
            }
        })

    except Exception as e:
        print("Verification Error:", e)
        return jsonify({"status": "error"})


# -------------------------------
# UPDATED ANALYZE (MATCHES FRONTEND)
# -------------------------------
@app.route("/analyze", methods=["POST"])
def analyze():

    aim_accuracy = random.randint(70, 90)
    reaction_time = random.randint(220, 320)
    kd_ratio = round(random.uniform(1.2, 2.5), 2)

    trend = [
        random.randint(65, 80),
        random.randint(70, 85),
        random.randint(75, 90),
        random.randint(72, 88),
        random.randint(78, 92),
    ]

    movement_score = random.randint(70, 95)

    return jsonify({
        "aim_accuracy": aim_accuracy,
        "reaction_time": reaction_time,
        "kd_ratio": kd_ratio,
        "trend": trend,
        "movement_score": movement_score
    })


if __name__ == "__main__":
    app.run(debug=True)