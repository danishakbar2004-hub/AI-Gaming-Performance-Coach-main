from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Gaming Coach Running"

if __name__ == "__main__":
    app.run(debug=True)

