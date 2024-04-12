import requests
from flask import Flask, render_template, request
import json

app = Flask(__name__)

API_KEY = "fERa6zvJRB5VMQ1S"
BRAIN_ID = "181440"
BASE_URL = f"http://api.brainshop.ai/get?bid={BRAIN_ID}&key={API_KEY}&uid=1&msg="


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_bot_response", methods=["POST"])
def get_bot_response():
    message = request.form["message"]
    bot_response = send_message(message)
    return json.dumps({"bot_response": bot_response})


def send_message(message):
    response = requests.get(BASE_URL + message)
    return response.json()["cnt"]


if __name__ == "__main__":
    app.run(debug=True)
