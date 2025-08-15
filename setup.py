#!/usr/bin/env python3
"""
Setup script for CMI Behavior Classifier
This script automates the installation and setup process.
"""

import os
import sys
import subprocess
import platform
import requests
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

def check_git():
    """Check if git is installed"""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        print("✅ Git is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed. Please install Git first.")
        return False

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

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    # Determine the correct pip command
    if platform.system() == "Windows":
        pip_cmd = "venv\\Scripts\\pip"
    else:
        pip_cmd = "venv/bin/pip"
    
    try:
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def download_models():
    """Download model files from Google Drive"""
    print("📥 Downloading model files from Google Drive...")
    
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

def run_tests():
    """Run basic tests"""
    print("🧪 Running basic tests...")
    
    # Determine the correct python command
    if platform.system() == "Windows":
        python_cmd = "venv\\Scripts\\python"
    else:
        python_cmd = "venv/bin/python"
    
    try:
        # Test model loading by importing the app
        result = subprocess.run([python_cmd, "-c", "import app; print('✅ Model loading test passed')"], 
                              capture_output=True, text=True, check=True)
        print("✅ Basic tests passed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main setup function"""
    print("🧠 CMI Behavior Classifier - Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check Git
    if not check_git():
        print("💡 Git is optional but recommended for version control")
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check model files (will download if missing)
    if not check_model_files():
        print("\n⚠️  Setup completed but model files are missing.")
        print("   Please download the models manually from:")
        print("   https://drive.google.com/file/d/16ldFJFaC9gUyY7Ezmh-jUrNA8j_xvcOQ/view?usp=sharing")
        print("   Extract the files to the models/ directory")
    else:
        # Run tests
        if not run_tests():
            print("\n⚠️  Setup completed but tests failed.")
            print("   You can still try running the app.")
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Activate the virtual environment:")
    if platform.system() == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("2. Run the application:")
    print("   python run_app.py")
    
    print("3. Open your browser and go to: http://localhost:8501")
    print("\n📚 For more information, see README.md")
    print("=" * 50)

if __name__ == "__main__":
    main()
