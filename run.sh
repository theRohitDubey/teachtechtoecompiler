#!/bin/bash

# Teach Tech Toe Multi-Compiler - Startup Script

echo "🚀 Starting Teach Tech Toe Multi-Compiler..."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed"
    exit 1
fi

echo "✅ Python3 found"
echo ""

# Install dependencies if not present
echo "📦 Checking dependencies..."
pip install -q -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "🌐 Starting server..."
echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
echo "   Teach Tech Toe Multi-Compiler"
echo "   📍 http://127.0.0.1:8000"
echo ""
echo "   🎉 Server running! Open the URL in your browser."
echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the server
python3 app.py
