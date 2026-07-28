# Quick Start - Teach Tech Toe Multi-Compiler

**Get it running in 60 seconds!**

---

## ⚡ Local Development (60 seconds)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Server
```bash
python app.py
```

### Step 3: Open Browser
```
http://localhost:8000
```

**Done!** ✅

---

## 🐳 Docker (30 seconds)

```bash
docker-compose up
```

Open: `http://localhost:8000`

---

## ☁️ Deploy to Render (5 minutes)

See: **DEPLOYMENT.md** for step-by-step guide

Quick summary:
1. Push to GitHub
2. Connect Render to GitHub repo
3. Set Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
4. Deploy!

---

## 🔍 API Quick Test

### Check Health
```bash
curl http://localhost:8000/api/health
```

### Get Languages
```bash
curl http://localhost:8000/api/languages
```

### Execute Python Code
```bash
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{
    "code": "print(\"Hello, World!\")",
    "language": "python"
  }'
```

---

## 📁 File Overview

| File | Purpose |
|------|---------|
| `app.py` | FastAPI backend |
| `index.html` | Web UI frontend |
| `requirements.txt` | Python packages |
| `Procfile` | Render deployment |
| `Dockerfile` | Docker image |
| `docker-compose.yml` | Docker setup |
| `README.md` | Full docs |
| `DEPLOYMENT.md` | Render guide |

---

## 🚀 50+ Supported Languages

### Popular
Python, JavaScript, C, C++, Java, Go, Rust, PHP, Ruby, TypeScript

### Also Supported
C#, Kotlin, Swift, R, Bash, SQL, Scala, Perl, Lua, Haskell, Clojure, Elixir, Julia, Dart, and more!

---

## 🎯 Next Steps

1. ✅ Get it running locally (above)
2. 📖 Read **README.md** for features
3. 🚀 Deploy to Render using **DEPLOYMENT.md**
4. 🔗 Integrate with Teach Tech Toe platform

---

## ❓ Troubleshooting

### Port 8000 in use?
```bash
python app.py --port 8001
```

### Module not found?
```bash
pip install -r requirements.txt --upgrade
```

### CORS errors?
✅ Already configured! Should work out of box.

---

## 💡 Tips

- **Keyboard Shortcut:** Ctrl+Enter to run code
- **Share Code:** Click "Share" button (copies code)
- **Download:** Save code as `.py`, `.cpp`, `.java`, etc.
- **Input:** Use "Input (stdin)" field for user input
- **Mobile:** Fully responsive design

---

**That's it! Happy coding!** 🎉
