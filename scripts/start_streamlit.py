#!/usr/bin/env python3
"""
Streamlit Startup Script for Web Activity Agent System.
This script starts the Streamlit application with proper configuration.
"""

import subprocess
import sys
import os
import time
import requests
from pathlib import Path

def check_backend_server():
    """Check if FastAPI backend server is running."""
    try:
        response = requests.get("http://127.0.0.1:8000/api/health", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def start_streamlit():
    """Start the Streamlit application."""
    
    print("🚀 Starting Web Activity Agent System - Streamlit App")
    print("=" * 60)
    
    # Check if FastAPI server is running
    print("🔍 Checking FastAPI backend status...")
    if not check_backend_server():
        print("❌ FastAPI backend is not running!")
        print("📝 Please start the backend first:")
        print("   python main.py")
        print()
        print("⏳ Waiting for the backend to start...")
        
        # Wait for server to start
        max_attempts = 30
        for attempt in range(max_attempts):
            if check_backend_server():
                print("✅ Backend is now running!")
                break
            print(f"⏳ Attempt {attempt + 1}/{max_attempts} - Waiting...")
            time.sleep(2)
        else:
            print("❌ Backend did not start. Please start it manually.")
            return False
    else:
        print("✅ Backend is running!")
    
    print()
    print("📊 Streamlit Configuration:")
    print("   Host: localhost")
    print("   Port: 8501")
    print("   URL: http://localhost:8501")
    print()
    print("🔗 Available Services:")
    print("   FastAPI Backend: http://127.0.0.1:8000")
    print("   Streamlit Frontend: http://localhost:8501")
    print("=" * 60)
    
    # Start Streamlit
    try:
        print("🎨 Starting Streamlit application...")
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Streamlit application stopped.")
    except Exception as e:
        print(f"❌ Error starting Streamlit: {e}")
        return False
    
    return True

if __name__ == "__main__":
    start_streamlit()
