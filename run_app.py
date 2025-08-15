#!/usr/bin/env python3
"""
CMI Behavior Classifier - Startup Script
This script checks dependencies and launches the Streamlit application.
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'streamlit',
        'pandas', 
        'numpy',
        'sklearn',
        'joblib'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} - Not installed")
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Please install dependencies using: pip install -r requirements.txt")
        return False
    
    return True

def check_model_files():
    """Check if model files exist"""
    model_path = Path("models/model.pkl")
    encoders_path = Path("models/encoders.pkl")
    
    if not model_path.exists():
        print("❌ models/model.pkl not found")
        return False
    
    if not encoders_path.exists():
        print("❌ models/encoders.pkl not found")
        return False
    
    print("✅ Model files found")
    return True

def main():
    """Main startup function"""
    print("🧠 CMI Behavior Classifier - Startup Check")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    print("\n📦 Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    
    print("\n🤖 Checking model files...")
    if not check_model_files():
        sys.exit(1)
    
    print("\n🚀 Starting CMI Behavior Classifier...")
    print("=" * 50)
    print("The web app will open in your browser automatically.")
    print("If it doesn't open, go to: http://localhost:8501")
    print("Press Ctrl+C to stop the application.")
    print("=" * 50)
    
    try:
        # Launch Streamlit app using py command
        subprocess.run(["py", "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
