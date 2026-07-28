@echo off
REM Teach Tech Toe Multi-Compiler - Windows Startup Script

echo.
echo 🚀 Starting Teach Tech Toe Multi-Compiler...
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Install dependencies
echo 📦 Installing dependencies...
pip install -q -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.

echo 🌐 Starting server...
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo    Teach Tech Toe Multi-Compiler
echo    📍 http://127.0.0.1:8000
echo.
echo    🎉 Server running! Open the URL in your browser.
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the server
python app.py

pause
