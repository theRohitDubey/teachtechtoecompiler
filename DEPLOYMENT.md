# Deploy Multi-Compiler to Render - Step-by-Step Guide

**Get your 50+ language compiler live in 5 minutes!**

---

## Prerequisites

- ✅ GitHub account
- ✅ Render account (free)
- ✅ This project files

---

## Step 1: Prepare Your GitHub Repository

### Create a New Repository

1. Go to **GitHub.com** → Sign in
2. Click **"New Repository"**
3. **Repository name:** `teach-tech-toe-multi-compiler`
4. **Description:** "50+ Languages Online Compiler"
5. **Visibility:** Public (required for Render free tier)
6. Click **"Create Repository"**

### Push Your Code

```bash
# Navigate to project folder
cd teach-tech-toe-multi-compiler

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - 50+ languages compiler"

# Add remote (replace USERNAME)
git remote add origin https://github.com/USERNAME/teach-tech-toe-multi-compiler.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 2: Connect to Render

### Connect Your GitHub Account

1. Go to **Render.com** → Sign up/Sign in
2. If first time: Authorize GitHub access
3. Click **"New +"** button (top-right)
4. Select **"Web Service"**

### Select Repository

1. Click **"Connect a repository"**
2. Search for: `teach-tech-toe-multi-compiler`
3. Click **"Connect"**

### Configure Service

Fill in these settings:

| Field | Value |
|-------|-------|
| **Name** | `teach-tech-toe-compiler` |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app:app --host 0.0.0.0 --port $PORT` |
| **Instance Type** | `Free` (starts with free) |

### Environment Variables (Optional)

If you want to use Judge0 as fallback:

```
JUDGE0_KEY=your_rapidapi_key_here
```

Get a free key at: https://rapidapi.com/judge0-official/api/judge0-ce

### Deploy

Click **"Create Web Service"** 

Render will:
1. Install dependencies (1-2 min)
2. Start your server (< 1 min)
3. Assign a public URL ✅

---

## Step 3: Access Your Live Compiler

Once deployment completes (green checkmark in Render dashboard):

```
https://teach-tech-toe-compiler.onrender.com
```

**Success!** Your compiler is now live! 🎉

---

## Step 4: Update Your Teach Tech Toe Platform

### Option A: Embed in iframe

Add to your Teach Tech Toe website:

```html
<!-- In your index.html or relevant page -->
<section id="compiler-section">
  <h2>Try Our 50+ Languages Compiler</h2>
  
  <iframe 
    src="https://teach-tech-toe-compiler.onrender.com" 
    width="100%" 
    height="800px"
    style="border: 2px solid #ff6b1a; border-radius: 8px; margin: 20px 0;">
  </iframe>
</section>
```

### Option B: Link in Navigation

```html
<!-- In your navigation menu -->
<a href="https://teach-tech-toe-compiler.onrender.com" 
   target="_blank" 
   class="nav-link">
  🚀 Online Compiler (50+ Languages)
</a>
```

### Option C: Embed in Dashboard

```html
<!-- Add a card/button to your main platform -->
<div class="tool-card">
  <h3>Online Compiler</h3>
  <p>Code in 50+ languages instantly</p>
  <a href="https://teach-tech-toe-compiler.onrender.com" 
     class="btn btn-primary">
    Open Compiler
  </a>
</div>
```

---

## 🔄 Update Process

### Make Changes Locally

```bash
# Edit files (app.py, index.html, etc.)
# Then commit and push:

git add .
git commit -m "Add more languages"
git push origin main
```

Render **automatically redeploys** when you push! ✅

---

## 📊 Monitor Your Service

### Check Status

1. Go to Render Dashboard
2. Find your service: `teach-tech-toe-compiler`
3. You'll see:
   - ✅ **Status** (Running/Crashed)
   - 📊 **Usage** (CPU, Memory)
   - 📈 **Analytics** (Requests/hour)
   - 🔍 **Logs** (Error messages)

### View Logs

```
Render Dashboard → Your Service → Logs
```

Use logs to debug issues.

---

## 🆓 Free Tier Limitations

| Feature | Limit |
|---------|-------|
| **Execution Time** | 30 seconds |
| **Memory** | 512 MB |
| **CPU** | Shared (throttled) |
| **Monthly Hours** | 750 (24/7 service) |
| **Idle Timeout** | 15 minutes (goes to sleep) |
| **Concurrent Users** | ~5-10 |

### What This Means

✅ **Works Great For:**
- Educational use
- Small to medium traffic
- Learning projects
- Demos

⚠️ **Limitations:**
- Service sleeps after 15 min inactivity (wakes on first request)
- First request takes ~1 minute on free tier
- Limited to ~5-10 concurrent users

### Upgrade When Needed

Want production-grade performance?

1. Go to **Render Dashboard** → **Your Service**
2. Click **"Settings"** → **"Plan"**
3. Upgrade to **Starter** ($7/month) or higher
4. Instant activation ⚡

---

## 🚀 Advanced: Custom Domain

### Add Your Domain

1. Go to **Render Dashboard** → **Your Service**
2. Click **"Settings"** → **"Custom Domain"**
3. Enter your domain: `compiler.teachtechtoe.com`
4. Add DNS records as instructed
5. SSL certificate auto-installed ✅

Your compiler is now at:
```
https://compiler.teachtechtoe.com
```

---

## 🔧 Troubleshooting

### Service Won't Start

**Error in Logs:**
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution:**
- Add missing package to `requirements.txt`
- Commit and push
- Render redeploys automatically

### Execution Timeout (>30 seconds)

**Problem:** Code takes too long to run

**Solution:**
- Optimize code
- Add timeout alert in frontend
- Upgrade to paid plan for more time

### "Cannot reach backend"

**Problem:** Connection refused

**Solution:**
- Wait 1-2 minutes (free tier startup)
- Refresh browser
- Check Render logs for errors
- Service might have crashed

### High Memory Usage

**Problem:** Service crashes frequently

**Solution:**
- Upgrade to Starter plan
- Optimize code
- Limit execution time
- Add memory monitoring

---

## 📈 Performance Optimization

### Make It Faster

1. **Cache Language List** - Fetch once on startup
2. **Connection Pooling** - Reuse HTTP connections
3. **Code Compression** - Minify frontend assets
4. **CDN** - Serve static files globally (pro tier)

### Monitor Performance

Render Dashboard shows:
- Response time
- CPU usage
- Memory usage
- Error rate

Aim for < 2 second response time.

---

## 🔒 Security Best Practices

### Add Rate Limiting

```python
# In app.py
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/execute")
@limiter.limit("10/minute")
async def execute_code(request: CodeRequest):
    # ... rest of code
```

### Validate Input

```python
@app.post("/api/execute")
async def execute_code(request: CodeRequest):
    # Check code length
    if len(request.code) > 100000:
        raise HTTPException(status_code=413, detail="Code too large")
    
    # Sanitize language
    if request.language not in ALLOWED_LANGUAGES:
        raise HTTPException(status_code=400, detail="Invalid language")
```

### Enable HTTPS

✅ Render automatically installs SSL/TLS certificates

### Add Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/api/execute")
async def execute_code(request: CodeRequest):
    logger.info(f"Code executed: {request.language}")
```

---

## 📚 Next Steps

1. ✅ Deploy to Render (above steps)
2. 📱 Add to your platform navigation
3. 📊 Monitor performance in Render dashboard
4. 🔧 Make improvements based on user feedback
5. 💰 Upgrade plan if needed

---

## 🎓 What Your Users Get

With this compiler integrated into Teach Tech Toe, students can:

✨ **Learn by doing**
- Write code immediately
- See results instantly
- No installation needed

🌍 **Access anywhere**
- Mobile-friendly
- Cloud-based
- Always available

🚀 **Support 50+ languages**
- Learn any language
- Switch instantly
- Full documentation

💪 **Professional tools**
- Input/output handling
- Error reporting
- Code downloading

---

## 📞 Support

### If Something Goes Wrong

1. **Check Render Logs**
   - Render Dashboard → Logs
   - Look for error messages

2. **Verify Files**
   - All files pushed to GitHub?
   - `requirements.txt` has all packages?
   - `Procfile` correct?

3. **Test Locally**
   ```bash
   python app.py
   # Visit http://localhost:8000
   ```

4. **Check GitHub Commits**
   - Latest code pushed?
   - No merge conflicts?

---

## 🎉 Congratulations!

Your Teach Tech Toe platform now has:

✅ 50+ language support  
✅ Cloud-based (no installation)  
✅ Professional interface  
✅ Real-time execution  
✅ Completely FREE  

Start teaching and learning with confidence! 🚀

---

**Questions?** Check README.md or contact support!
