"""
Teach Tech Toe - Multi-Compiler Backend
Supports 50+ Languages via Piston API
Fallback to Judge0 for cloud execution
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import httpx
import asyncio
import os

app = FastAPI(title="Teach Tech Toe Multi-Compiler")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str
    language: str
    stdin: str = ""

# Piston API - 50+ languages support
PISTON_API = "https://emkc.org/api/v2"
# Judge0 API - Cloud-based (free tier available)
JUDGE0_API = "https://judge0-ce.p.rapidapi.com"
JUDGE0_KEY = os.getenv("JUDGE0_KEY", "")  # Optional: Add your RapidAPI key

# Language ID mappings for both APIs
PISTON_LANGUAGES = {
    "python": "python",
    "py-simple": "python",
    "javascript": "javascript",
    "js": "javascript",
    "node": "javascript",
    "cpp": "cpp",
    "c++": "cpp",
    "c": "c",
    "java": "java",
    "html": "html",
    "css": "css",
    "php": "php",
    "go": "go",
    "rust": "rust",
    "ruby": "ruby",
    "typescript": "typescript",
    "ts": "typescript",
    "r": "r",
    "bash": "bash",
    "shell": "bash",
    "csharp": "csharp",
    "c#": "csharp",
    "kotlin": "kotlin",
    "swift": "swift",
    "perl": "perl",
    "lua": "lua",
    "sql": "sql",
    "scala": "scala",
    "groovy": "groovy",
    "haskell": "haskell",
    "clojure": "clojure",
    "elixir": "elixir",
    "erlang": "erlang",
    "julia": "julia",
    "matlab": "octave",
    "ocaml": "ocaml",
    "pascal": "pascal",
    "commonlisp": "lisp",
    "scheme": "scheme",
    "prolog": "prolog",
    "dart": "dart",
    "objective-c": "objective-c",
    "f#": "fsharp",
    "fsharp": "fsharp",
}

JUDGE0_LANGUAGES = {
    "c": 49,
    "cpp": 54,
    "c#": 51,
    "csharp": 51,
    "java": 62,
    "python": 71,
    "py-simple": 71,
    "javascript": 63,
    "js": 63,
    "node": 63,
    "go": 60,
    "rust": 73,
    "ruby": 72,
    "php": 68,
    "swift": 83,
    "kotlin": 78,
    "typescript": 74,
    "ts": 74,
    "r": 80,
}

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "Teach Tech Toe Multi-Compiler",
        "version": "2.0",
        "description": "Supports 50+ programming languages",
        "backends": ["Piston", "Judge0"],
        "docs": "Visit /docs for API documentation"
    }

@app.get("/api/health")
async def health():
    """Health check"""
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(f"{PISTON_API}/runtimes")
            piston_status = "operational" if response.status_code == 200 else "error"
    except:
        piston_status = "error"
    
    return {
        "status": "operational",
        "piston": piston_status,
        "backend": "Piston API + Judge0"
    }

@app.get("/api/languages")
async def get_languages():
    """Get list of supported languages"""
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(f"{PISTON_API}/runtimes")
            if response.status_code == 200:
                runtimes = response.json()
                languages = []
                for runtime in runtimes[:50]:  # Limit to 50 for UI
                    languages.append({
                        "name": runtime.get("language"),
                        "version": runtime.get("version"),
                        "runtime": runtime.get("runtime")
                    })
                return {"total": len(languages), "languages": languages}
    except Exception as e:
        return {"error": str(e)}
    
    return {"languages": list(PISTON_LANGUAGES.keys())}

@app.post("/api/execute")
async def execute_code(request: CodeRequest):
    """Execute code using Piston API (primary) or Judge0 (fallback)"""
    code = request.code
    language = request.language.lower()
    stdin = request.stdin
    
    # Handle HTML special case
    if language == "html":
        return {
            "success": True,
            "output": "✅ HTML/CSS/JS rendered in browser",
            "execution_time": 0
        }
    
    # Map language to Piston format
    piston_lang = PISTON_LANGUAGES.get(language, language)
    
    try:
        # Try Piston API first (primary)
        return await execute_via_piston(code, piston_lang, stdin)
    except Exception as piston_error:
        print(f"Piston error: {piston_error}")
        
        # Fallback to Judge0 if available
        if JUDGE0_KEY and language in JUDGE0_LANGUAGES:
            try:
                return await execute_via_judge0(code, language, stdin)
            except Exception as judge0_error:
                return {
                    "success": False,
                    "output": f"Both compilers failed:\nPiston: {str(piston_error)}\nJudge0: {str(judge0_error)}"
                }
        
        return {
            "success": False,
            "output": f"Compilation Error:\n{str(piston_error)}\n\nTry a different language or check syntax."
        }

async def execute_via_piston(code: str, language: str, stdin: str = ""):
    """Execute code via Piston API"""
    payload = {
        "language": language,
        "source": code,
        "stdin": stdin
    }
    
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            f"{PISTON_API}/execute",
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        
        output = ""
        if result.get("stdout"):
            output += result["stdout"]
        if result.get("stderr"):
            output += f"\nError:\n{result['stderr']}"
        if result.get("compile_output"):
            output += f"\nCompile:\n{result['compile_output']}"
        
        return {
            "success": True,
            "output": output or "Execution completed with no output",
            "execution_time": result.get("run", {}).get("wall", 0)
        }

async def execute_via_judge0(code: str, language: str, stdin: str = ""):
    """Execute code via Judge0 API (cloud-based fallback)"""
    lang_id = JUDGE0_LANGUAGES.get(language.lower())
    if not lang_id:
        raise ValueError(f"Judge0 doesn't support {language}")
    
    headers = {
        "X-RapidAPI-Key": JUDGE0_KEY,
        "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    
    payload = {
        "source_code": code,
        "language_id": lang_id,
        "stdin": stdin
    }
    
    async with httpx.AsyncClient(timeout=30) as client:
        # Submit
        response = await client.post(
            f"{JUDGE0_API}/submissions",
            json=payload,
            headers=headers,
            params={"wait": "true"}
        )
        response.raise_for_status()
        result = response.json()
        
        output = result.get("stdout", "") or result.get("stderr", "") or "No output"
        
        return {
            "success": result.get("status_id") in [1, 2],  # 1=Accepted, 2=Partial
            "output": output,
            "execution_time": result.get("time", 0)
        }

@app.post("/api/ai-review")
async def ai_review_code(request: CodeRequest):
    """AI code review (placeholder for future AI integration)"""
    # This can be integrated with Claude API, OpenAI, or similar
    return {
        "review": "Code review feature coming soon!",
        "suggestions": [
            "Add error handling",
            "Add comments for complex logic",
            "Follow PEP 8 style guide (if Python)"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
