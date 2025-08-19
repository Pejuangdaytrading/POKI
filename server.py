from fastapi import FastAPI
import json, os

app = FastAPI()

DATA_FILE = "user_progress.json"

def load_progress():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_progress(progress):
    with open(DATA_FILE, "w") as f:
        json.dump(progress, f, indent=4)

@app.get("/")
async def root():
    return {"status": "ok", "msg": "PokiCoin API running"}

@app.get("/api/validate/{user_id}/{ad_id}")
async def validate(user_id: str, ad_id: str):
    progress = load_progress()

    if user_id not in progress:
        progress[user_id] = {"ad1": False, "ad2": False, "balance": 0, "reward_claimed": False}

    # validasi iklan
    if ad_id in ["ad1", "ad2"]:
        progress[user_id][ad_id] = True
        save_progress(progress)
        return {"status": "success", "user": user_id, "ad": ad_id}

    # klaim reward
    if ad_id == "reward":
        if progress[user_id]["ad1"] and progress[user_id]["ad2"]:
            if not progress[user_id].get("reward_claimed", False):
                progress[user_id]["balance"] += 10
                progress[user_id]["reward_claimed"] = True
                save_progress(progress)
                return {"status": "success", "msg": "Reward claimed", "balance": progress[user_id]["balance"]}
            else:
                return {"status": "error", "msg": "Reward already claimed"}
        else:
            return {"status": "error", "msg": "Complete ads first"}

    # cek balance
    if ad_id == "balance":
        return {"status": "success", "balance": progress[user_id]["balance"]}

    return {"status": "error", "msg": "Invalid ad_id"}
