[README.md](https://github.com/user-attachments/files/21847140/README.md)
# PokiCoin Backend

Backend sederhana untuk Telegram Bot + MiniApp, dibangun dengan Flask.  
Digunakan untuk menyimpan progress user (XP & Coin) dan validasi iklan Monetag.

## 🚀 Cara Deploy ke Render

1. Fork/clone repo ini ke akun GitHub kamu.
2. Buka [Render.com](https://render.com/).
3. Pilih **New → Web Service**.
4. Hubungkan dengan repo ini.
5. Setting:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app`
6. Deploy → Render akan memberi URL backend, contoh:
   ```
   https://pokicoin-backend.onrender.com
   ```

## 📡 Endpoint

- `GET /progress/<user_id>`  
  Ambil progress user.  

  **Contoh**:  
  ```
  https://pokicoin-backend.onrender.com/progress/12345
  ```

  **Response**:
  ```json
  {
    "xp": 10,
    "coin": 10
  }
  ```

- `POST /callback`  
  Update reward setelah user nonton iklan.  

  **Body JSON**:
  ```json
  {
    "user_id": 12345,
    "reward": 10
  }
  ```

  **Response**:
  ```json
  {
    "status": "ok",
    "new_data": {
      "xp": 20,
      "coin": 20
    }
  }
  ```

## 📂 File Penting
- `server.py` → Flask server utama
- `requirements.txt` → daftar dependensi
- `user_progress.json` → file penyimpanan progress user
