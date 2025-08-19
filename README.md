# PokiCoin Backend (Railway Ready)

Backend sederhana untuk Telegram Bot + MiniApp, dibangun dengan Flask.  
Disiapkan khusus agar bisa jalan di Railway atau Render.

## 🚀 Deploy ke Railway
1. Fork repo ini ke GitHub kamu.
2. Buka [Railway.app](https://railway.app/).
3. Klik **New Project → Deploy from GitHub Repo**.
4. Pilih repo ini.
5. Railway akan otomatis baca `Procfile` dan menjalankan:
   ```
   web: gunicorn server:app
   ```
6. Setelah deploy, Railway kasih URL misalnya:
   ```
   https://pokicoin-backend.up.railway.app
   ```

## 🚀 Deploy ke Render
1. Pilih **New Web Service** di [Render.com](https://render.com/).
2. Hubungkan repo ini.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn server:app`

## 📡 Endpoint
- GET `/progress/<user_id>` → ambil data user.
- POST `/callback` → update reward.

## 📂 File Penting
- `server.py` → Flask server
- `requirements.txt` → dependensi
- `Procfile` → command untuk Railway
- `user_progress.json` → penyimpanan data
