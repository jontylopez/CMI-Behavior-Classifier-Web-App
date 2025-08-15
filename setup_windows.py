#!/usr/bin/env python3
"""
Windows-specific setup script for CMI Behavior Classifier
This script handles Windows compilation issues and provides alternative installation methods.
"""

import os
import sys
import subprocess
import platform
import zipfile
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def create_virtual_environment():
    """Create virtual environment"""
    if os.path.exists("venv"):
        print("✅ Virtual environment already exists")
        return True
    
    print("📦 Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating virtual environment: {e}")
        return False

def install_dependencies_windows():
    """Install dependencies with Windows-specific handling"""
    print("📦 Installing dependencies for Windows...")
    
    pip_cmd = "venv\\Scripts\\pip"
    
    # Strategy 1: Try upgrading pip first
    try:
        print("   Upgrading pip...")
        subprocess.run([pip_cmd, "install", "--upgrade", "pip"], check=True)
    except subprocess.CalledProcessError:
        print("   ⚠️  Could not upgrade pip, continuing...")
    
    # Strategy 2: Try installing with pre-compiled wheels
    try:
        print("   Attempting installation with pre-compiled wheels...")
        subprocess.run([pip_cmd, "install", "--only-binary=all", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully using pre-compiled wheels")
        return True
    except subprocess.CalledProcessError:
        print("   ❌ Pre-compiled wheel installation failed")
    
    # Strategy 3: Try installing packages one by one
    print("   Attempting individual package installation...")
    packages = ["numpy", "scikit-learn", "pandas", "streamlit", "joblib", "requests"]
    
    for package in packages:
        try:
            print(f"   Installing {package}...")
            subprocess.run([pip_cmd, "install", package], check=True)
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Failed to install {package}: {e}")
            if package in ["numpy", "scikit-learn"]:
                print(f"   💡 Try: pip install {package} --only-binary=all")
    
    # Strategy 4: Check if critical packages are installed
    try:
        import numpy
        import sklearn
        import pandas
        import streamlit
        import joblib
        import requests
        print("✅ All critical dependencies are available")
        return True
    except ImportError as e:
        print(f"❌ Missing critical dependency: {e}")
        return False

def download_models():
    """Download model files from Google Drive"""
    print("📥 Downloading model files from Google Drive...")
    
    # Import requests here after dependencies are installed
    try:
        import requests
    except ImportError:
        print("❌ requests module not found. Please install dependencies first.")
        return False
    
    # Create models directory if it doesn't exist
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    
    # Google Drive file ID from the URL
    file_id = "16ldFJFaC9gUyY7Ezmh-jUrNA8j_xvcOQ"
    
    # Google Drive direct download URL
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    
    try:
        print("   Downloading models.zip...")
        response = requests.get(download_url, stream=True)
        response.raise_for_status()
        
        # Save the zip file
        zip_path = "models.zip"
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print("   Extracting model files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall("models/")
        
        # Clean up the zip file
        os.remove(zip_path)
        
        print("✅ Model files downloaded and extracted successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error downloading model files: {e}")
        print("   Please download the models manually from:")
        print("   https://drive.google.com/file/d/16ldFJFaC9gUyY7Ezmh-jUrNA8j_xvcOQ/view?usp=sharing")
        print("   Extract the files to the models/ directory")
        return False

def check_model_files():
    """Check if model files exist"""
    model_path = "models/model.pkl"
    encoders_path = "models/encoders.pkl"
    
    if not os.path.exists(model_path):
        print("❌ models/model.pkl not found")
        print("   Attempting to download from Google Drive...")
        if download_models():
            return check_model_files()  # Check again after download
        else:
            return False
    
    if not os.path.exists(encoders_path):
        print("❌ models/encoders.pkl not found")
        print("   Attempting to download from Google Drive...")
        if download_models():
            return check_model_files()  # Check again after download
        else:
            return False
    
    print("✅ Model files found")
    return True

def main():
    """Main setup function for Windows"""
    print("🧠 CMI Behavior Classifier - Windows Setup")
    print("=" * 50)
    
    # Check if we're on Windows
    if platform.system() != "Windows":
        print("❌ This script is designed for Windows only")
        print("   Use setup.py for other operating systems")
        sys.exit(1)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies with Windows-specific handling
    if not install_dependencies_windows():
        print("\n🔧 Installation failed. Try these solutions:")
        print("\n1. Install Microsoft Visual C++ Build Tools:")
        print("   https://visualstudio.microsoft.com/visual-cpp-build-tools/")
        print("   - Download and run as administrator")
        print("   - Select 'C++ build tools' workload")
        print("   - Restart computer and try again")
        
        print("\n2. Use Anaconda/Miniconda (recommended):")
        print("   - Install from: https://www.anaconda.com/download")
        print("   - Create environment: conda create -n cmi-app python=3.9")
        print("   - Install packages: conda install numpy scikit-learn pandas")
        print("   - Install others: pip install streamlit joblib requests")
        
        print("\n3. Manual installation:")
        print("   venv\\Scripts\\activate")
        print("   pip install --upgrade pip")
        print("   pip install --only-binary=all numpy scikit-learn pandas streamlit joblib requests")
        
        sys.exit(1)
    
    # Check model files (will download if missing)
    if not check_model_files():
        print("\n⚠️  Setup completed but model files are missing.")
        print("   Please download the models manually from:")
        print("   https://drive.google.com/file/d/16ldFJFaC9gUyY7Ezmh-jUrNA8j_xvcOQ/view?usp=sharing")
        print("   Extract the files to the models/ directory")
    
    print("\n" + "=" * 50)
    print("🎉 Windows setup completed!")
    print("\n📋 Next steps:")
    print("1. Activate the virtual environment:")
    print("   venv\\Scripts\\activate")
    
    print("2. Run the application:")
    print("   python run_app.py")
    
    print("3. Open your browser and go to: http://localhost:8501")
    print("\n📚 For more information, see README.md")
    print("=" * 50)

if __name__ == "__main__":
    main()
