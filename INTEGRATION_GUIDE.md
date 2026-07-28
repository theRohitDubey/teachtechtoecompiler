# Integration Guide - Add Multi-Compiler to Teach Tech Toe

**How to add the 50+ language compiler to your platform**

---

## 🎯 Integration Options

Pick one method:

1. **iframe Embed** (Easiest) ← Recommended for quick integration
2. **Link in Navigation**
3. **Custom Integration** (Advanced)
4. **Standalone Deployment**

---

## Option 1: iframe Embed (Recommended)

### Add to Any Page

In your Teach Tech Toe HTML page:

```html
<!-- Add this where you want the compiler -->

<section id="compiler-section" class="my-5">
  <div class="container">
    <h2 class="mb-4">
      <i class="fas fa-code"></i> Online Compiler
    </h2>
    <p class="lead text-muted mb-4">
      Write and run code in 50+ languages instantly. No installation needed!
    </p>
    
    <iframe 
      id="compiler-iframe"
      src="https://teach-tech-toe-compiler.onrender.com" 
      width="100%" 
      height="800"
      style="
        border: 2px solid #ff6b1a;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
      "
      allow="clipboard-read; clipboard-write"
      title="50+ Languages Online Compiler">
    </iframe>
  </div>
</section>

<!-- Optional: CSS for better styling -->
<style>
  #compiler-section {
    background: linear-gradient(135deg, #f6f3ec 0%, #ffffff 100%);
    padding: 40px 0;
    margin: 40px 0;
    border-radius: 8px;
  }
  
  #compiler-section h2 {
    color: #ff6b1a;
    font-weight: 700;
  }
</style>
```

### Benefits
✅ Super easy to implement  
✅ No API integration needed  
✅ Auto-updates when we update compiler  
✅ Works on mobile  
✅ Responsive design  

### Mobile Responsive Version

```html
<section id="compiler-responsive">
  <div class="container-fluid">
    <h2>Online Compiler</h2>
    
    <div class="compiler-wrapper">
      <iframe 
        src="https://teach-tech-toe-compiler.onrender.com" 
        class="compiler-frame">
      </iframe>
    </div>
  </div>
</section>

<style>
  .compiler-wrapper {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    height: 0;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.1);
    margin: 20px 0;
  }
  
  .compiler-frame {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: none;
  }
  
  @media (max-width: 768px) {
    .compiler-wrapper {
      padding-bottom: 100%; /* Full height on mobile */
    }
  }
</style>
```

---

## Option 2: Link in Navigation

### Add to Navigation Bar

```html
<!-- In your navbar/header -->
<nav class="navbar">
  <ul class="nav-links">
    <!-- Your existing links -->
    <li><a href="#home">Home</a></li>
    <li><a href="#courses">Courses</a></li>
    <li><a href="#trainers">Trainers</a></li>
    
    <!-- Add compiler link -->
    <li>
      <a href="https://teach-tech-toe-compiler.onrender.com" 
         target="_blank"
         class="nav-link-compiler">
        <i class="fas fa-code"></i> Online Compiler
      </a>
    </li>
  </ul>
</nav>

<style>
  .nav-link-compiler {
    background: linear-gradient(135deg, #ff6b1a, #ff9800) !important;
    color: white !important;
    padding: 8px 16px !important;
    border-radius: 20px !important;
    font-weight: 600 !important;
    transition: all 0.3s;
  }
  
  .nav-link-compiler:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 107, 26, 0.3);
  }
</style>
```

### Add to Dashboard/Tools Section

```html
<!-- In your platform dashboard -->
<div class="tools-grid">
  <div class="tool-card">
    <div class="tool-icon">💻</div>
    <h3>Online Compiler</h3>
    <p>Write and run code in 50+ languages instantly</p>
    <a href="https://teach-tech-toe-compiler.onrender.com" 
       target="_blank"
       class="btn btn-primary">
      Open Compiler →
    </a>
  </div>
  
  <div class="tool-card">
    <!-- Your other tools -->
  </div>
</div>

<style>
  .tools-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 20px;
  }
  
  .tool-card {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    text-align: center;
    transition: all 0.3s;
  }
  
  .tool-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
  }
  
  .tool-icon {
    font-size: 3rem;
    margin-bottom: 10px;
  }
</style>
```

---

## Option 3: Custom Integration (Advanced)

### Use Compiler API Directly

Create a custom UI that calls the compiler API:

```html
<div id="custom-compiler">
  <textarea id="code" placeholder="Write code..."></textarea>
  <button onclick="runCode()">Run</button>
  <pre id="output"></pre>
</div>

<script>
  async function runCode() {
    const code = document.getElementById('code').value;
    const language = 'python'; // or 'javascript', 'cpp', etc.
    
    try {
      const response = await fetch('https://teach-tech-toe-compiler.onrender.com/api/execute', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          code: code,
          language: language,
          stdin: ''
        })
      });
      
      const result = await response.json();
      document.getElementById('output').textContent = result.output;
    } catch (error) {
      document.getElementById('output').textContent = 'Error: ' + error.message;
    }
  }
</script>
```

### Multi-Language Dropdown

```html
<div id="custom-compiler-advanced">
  <select id="language" onchange="changeLanguage()">
    <option value="python">Python</option>
    <option value="javascript">JavaScript</option>
    <option value="cpp">C++</option>
    <option value="java">Java</option>
    <option value="go">Go</option>
    <option value="rust">Rust</option>
    <!-- Add more languages -->
  </select>
  
  <textarea id="code" placeholder="Write code..."></textarea>
  <button onclick="runCode()">▶ Run Code</button>
  
  <div id="output">
    <pre id="output-text">Output will appear here...</pre>
  </div>
</div>

<script>
  const templates = {
    python: 'print("Hello, World!")',
    javascript: 'console.log("Hello, World!")',
    cpp: '#include <iostream>\nint main() { std::cout << "Hello!"; }',
    java: 'public class Main { public static void main(String[] args) { } }',
    go: 'package main\nfunc main() { }',
    rust: 'fn main() { println!("Hello!"); }'
  };
  
  function changeLanguage() {
    const lang = document.getElementById('language').value;
    document.getElementById('code').value = templates[lang];
  }
  
  async function runCode() {
    const code = document.getElementById('code').value;
    const language = document.getElementById('language').value;
    
    const response = await fetch('https://teach-tech-toe-compiler.onrender.com/api/execute', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code, language })
    });
    
    const result = await response.json();
    document.getElementById('output-text').textContent = result.output;
  }
  
  // Initialize
  changeLanguage();
</script>
```

---

## Option 4: Standalone Deployment

### Deploy Your Own Instance

If you want your own dedicated compiler instance:

1. Follow **DEPLOYMENT.md** to deploy to Render
2. Use your URL: `https://your-compiler.onrender.com`
3. Customize further if needed

Benefits:
- Complete control
- Custom branding
- No external dependency
- Can be offline if needed

---

## 🎨 Styling Tips

### Match Your Brand

```html
<!-- Use your brand colors -->
<style>
  /* Override compiler colors -->
  /* (if using iframe, this won't work, but good for custom integration) */
  
  :root {
    --primary-color: #ff6b1a;
    --dark-bg: #1a1a1a;
    --light-bg: #f6f3ec;
  }
</style>
```

### Dark Mode Support

```html
<style>
  @media (prefers-color-scheme: dark) {
    #compiler-section {
      background: #1a1a1a;
      color: white;
    }
    
    #compiler-iframe {
      filter: invert(1) hue-rotate(180deg);
    }
  }
</style>
```

---

## 📊 Add Analytics

### Track Compiler Usage

```html
<script>
  // Google Analytics
  function openCompiler() {
    ga('send', 'event', 'compiler', 'open');
    window.open('https://teach-tech-toe-compiler.onrender.com');
  }
  
  // Custom tracking
  function trackCodeExecution(language) {
    fetch('/api/analytics', {
      method: 'POST',
      body: JSON.stringify({
        event: 'code_executed',
        language: language,
        timestamp: new Date()
      })
    });
  }
</script>
```

---

## 🚀 Performance Tips

### Lazy Load iframe

```html
<script>
  // Lazy load iframe to improve page load
  document.addEventListener('DOMContentLoaded', () => {
    const iframe = document.querySelector('#compiler-iframe');
    if (iframe) {
      setTimeout(() => {
        iframe.src = 'https://teach-tech-toe-compiler.onrender.com';
      }, 3000);
    }
  });
</script>
```

### Cache Response

```html
<script>
  const cache = {};
  
  async function runCode() {
    const key = code + language;
    if (cache[key]) {
      showOutput(cache[key]);
      return;
    }
    
    const result = await fetch(...);
    cache[key] = result;
    showOutput(result);
  }
</script>
```

---

## 📱 Mobile Optimization

```html
<!-- Ensure mobile viewport -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Responsive iframe -->
<div class="iframe-container">
  <iframe src="https://teach-tech-toe-compiler.onrender.com"></iframe>
</div>

<style>
  .iframe-container {
    position: relative;
    width: 100%;
    padding-bottom: 100%; /* Adjust as needed */
    height: 0;
    overflow: hidden;
  }
  
  .iframe-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
</style>
```

---

## ✅ Testing Checklist

Before going live:

- [ ] Test on Chrome, Firefox, Safari, Edge
- [ ] Test on mobile (iOS & Android)
- [ ] Test with different code snippets
- [ ] Test all 50+ languages
- [ ] Test error handling
- [ ] Test slow internet (throttle network)
- [ ] Check console for errors
- [ ] Verify CORS works
- [ ] Test offline behavior
- [ ] Check accessibility (keyboard navigation)

---

## 🆘 Troubleshooting

### iframe Won't Load
- Check your domain is in CORS whitelist
- Ensure HTTPS is used (Render uses HTTPS)
- Check browser console for errors

### Slow Performance
- Free Render tier sleeps after 15 min
- First request wakes it up (takes ~30 sec)
- Upgrade to paid tier for better performance

### CORS Errors
✅ Already configured! Should work.

If not:
```python
# In app.py, CORS is enabled:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📞 Support

### If You Need Help

1. Check **README.md** for features
2. Check **DEPLOYMENT.md** for deployment issues
3. Check browser console for error messages
4. Contact: teachtechtoe@gmail.com

---

## 🎉 You're All Set!

Your Teach Tech Toe platform now has a professional 50+ language compiler!

### Impact
- 👨‍🎓 Students can learn instantly
- 💪 No installation required
- 🌍 Works anywhere
- 🚀 Professional grade tool

**Happy teaching! 🎓**

---

**Next:** Read other guides for more information:
- **README.md** - Full features
- **DEPLOYMENT.md** - Deployment details
- **QUICKSTART.md** - Get started immediately
