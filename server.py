from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# File penyimpanan progress user
DATA_FILE = "user_progress.json"

# Fungsi load & save data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def home():
    return "✅ PokiCoin Backend is running!"

@app.route("/progress/<int:user_id>", methods=["GET"])
def get_progress(user_id):
    data = load_data()
    user = data.get(str(user_id), {"xp": 0, "coin": 0})
    return jsonify(user)

@app.route("/callback", methods=["POST"])
def callback():
    body = request.json
    user_id = str(body.get("user_id"))
    reward = int(body.get("reward", 0))

    data = load_data()
    if user_id not in data:
        data[user_id] = {"xp": 0, "coin": 0}

    data[user_id]["xp"] += reward
    data[user_id]["coin"] += reward

    save_data(data)
    return jsonify({"status": "ok", "new_data": data[user_id]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
