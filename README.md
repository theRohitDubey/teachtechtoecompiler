# Teach Tech Toe - 50+ Languages Compiler

**The Ultimate Open-Source Multi-Language Compiler**

🚀 Supports **50+ Programming Languages**  
⚡ Powered by **Piston API** (Free & Open-Source)  
☁️ Cloud Fallback with **Judge0**  
🎯 Perfect for Teach Tech Toe Platform  

---

## ✨ Features

### Supported Languages
- **Python, JavaScript, TypeScript, Node.js**
- **C, C++, C# (.NET)**
- **Java, Kotlin, Scala**
- **Go, Rust, PHP**
- **Ruby, Perl, Shell/Bash**
- **SQL, R, Haskell**
- **Swift, Objective-C**
- **And 30+ more...**

### Capabilities
✅ Real-time code execution  
✅ Standard input (stdin) support  
✅ Execution time tracking  
✅ Error reporting  
✅ Code download functionality  
✅ Share functionality  
✅ Responsive design (mobile-friendly)  
✅ Dark theme UI  
✅ Keyboard shortcuts (Ctrl+Enter to run)  

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Backend** | FastAPI (Python) |
| **Compiler API** | Piston (Primary), Judge0 (Fallback) |
| **Hosting** | Render.com (Free Tier) |
| **Database** | Optional (for future features) |

---

## 📁 Project Structure

```
teach-tech-toe-multi-compiler/
├── app.py                    # FastAPI backend
├── index.html               # Frontend UI
├── requirements.txt         # Python dependencies
├── Procfile                 # Render deployment
├── render.yaml             # Render config
├── README.md               # This file
├── DEPLOYMENT.md           # Deployment guide
├── .gitignore             # Git ignore rules
└── docker-compose.yml     # Docker setup (optional)
```

---

## 🚀 Quick Start (Local)

### Prerequisites
- Python 3.8+
- pip
- Git

### Installation

```bash
# 1. Clone or download the project
git clone <repo-url>
cd teach-tech-toe-multi-compiler

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python app.py

# 5. Open browser
# Visit: http://localhost:8000
```

**That's it!** 🎉 Your compiler is ready to use.

---

## ☁️ Deploy to Render (Free)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Teach Tech Toe Multi-Compiler"
git remote add origin https://github.com/YOUR_USERNAME/teach-tech-toe-multi-compiler.git
git branch -M main
git push -u origin main
```

### Step 2: Connect to Render

1. Go to [Render.com](https://render.com)
2. Click **"New Web Service"**
3. Select your GitHub repository
4. Configure:
   - **Name:** `teach-tech-toe-compiler`
   - **Runtime:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
5. Click **"Create Web Service"**

### Step 3: Access Your Compiler

Once deployed, your compiler will be live at:
```
https://teach-tech-toe-compiler.onrender.com
```

---

## 🔧 API Endpoints

### `/` - Root
```bash
GET /
# Returns: Service info and supported backends
```

### `/api/health` - Health Check
```bash
GET /api/health
# Returns: {status: "operational", piston: "...", backend: "..."}
```

### `/api/languages` - Supported Languages
```bash
GET /api/languages
# Returns: List of all supported languages with versions
```

### `/api/execute` - Execute Code
```bash
POST /api/execute
Content-Type: application/json

{
  "code": "print('Hello, World!')",
  "language": "python",
  "stdin": "optional input"
}

# Returns: {success: true/false, output: "...", execution_time: 0.123}
```

### `/api/ai-review` - Code Review (Future)
```bash
POST /api/ai-review
# Will integrate with Claude API or OpenAI
```

---

## 🌐 Integrating with Teach Tech Toe

### Option 1: Embed as iframe
```html
<iframe 
  src="https://teach-tech-toe-compiler.onrender.com" 
  width="100%" 
  height="600"
  style="border: none; border-radius: 8px;">
</iframe>
```

### Option 2: Link from Navigation
```html
<a href="https://teach-tech-toe-compiler.onrender.com" 
   target="_blank" 
   class="nav-link">
  Online Compiler
</a>
```

### Option 3: Custom Integration
```javascript
// Call the API directly from your app
const response = await fetch('https://teach-tech-toe-compiler.onrender.com/api/execute', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    code: userCode,
    language: 'python',
    stdin: userInput
  })
});

const result = await response.json();
console.log(result.output);
```

---

## 🐛 Troubleshooting

### "Connection Error: Cannot reach backend"
**Solution:** Server might still be starting. Wait 1-2 minutes on Render's free tier.

### "Language not supported"
**Solution:** Check the `/api/languages` endpoint for current list.

### "Execution timeout"
**Solution:** Piston has a 30-second limit. Code running longer will timeout.

### "Port already in use" (Local)
**Solution:** Change port:
```bash
python app.py --port 8001
```

### Render service crashes
**Solution:** Check logs in Render dashboard for errors.

---

## 📊 Performance Notes

### Piston API (Primary)
- ✅ 50+ languages
- ✅ Free & open-source
- ✅ Reliable
- ⚠️ Rate limited (free tier)

### Judge0 (Fallback)
- ✅ Cloud-based (no setup)
- ✅ 70+ languages
- ⚠️ Requires API key
- ⚠️ Limited free tier

---

## 🔒 Security Considerations

⚠️ **This is for learning/demo purposes only!**

For production, add:
1. **Rate Limiting** - Prevent abuse
2. **Authentication** - User verification
3. **Sandboxing** - Docker containerization
4. **Resource Limits** - CPU, memory, time limits
5. **Input Validation** - Sanitize code
6. **Logging** - Track executions

---

## 🚀 Advanced: Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t teach-tech-toe-compiler .
docker run -p 8000:8000 teach-tech-toe-compiler
```

---

## 💡 Future Enhancements

- [ ] User authentication
- [ ] Code snippet saving
- [ ] Collaborative coding
- [ ] AI code review
- [ ] Code formatting
- [ ] Syntax highlighting improvements
- [ ] Language detection
- [ ] Performance analytics
- [ ] Dark/Light theme toggle
- [ ] Keyboard shortcut help

---

## 📚 Resources

| Resource | Link |
|----------|------|
| Piston API Docs | https://piston.readthedocs.io |
| Judge0 Docs | https://judge0.com |
| FastAPI Docs | https://fastapi.tiangolo.com |
| Render Docs | https://render.com/docs |
| GitHub | https://github.com |

---

## 📜 License

Open Source - MIT License

Feel free to fork, modify, and distribute!

---

## 🤝 Contributing

Want to add more features?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

---

## 📞 Support

- **Issues:** GitHub Issues
- **Email:** teachtechtoe@gmail.com
- **Website:** https://teachtechtoe.com

---

## 🎉 Enjoy!

You now have the **most comprehensive open-source multi-language compiler**!

Perfect for:
- 👨‍🎓 Learning platforms
- 👨‍💼 Coding bootcamps
- 📚 Online education
- 🏢 Companies
- 👥 Communities

Happy coding! 💻✨
