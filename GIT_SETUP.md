# 🚀 Git Setup Guide

This guide will help you push your CMI Behavior Classifier project to a Git repository.

## 📋 Prerequisites

- Git installed on your system
- A GitHub/GitLab/Bitbucket account
- Your project files ready

## 🔧 Initial Git Setup

### 1. Initialize Git Repository

```bash
# Navigate to your project directory
cd "D:\CI Project"

# Initialize git repository
git init
```

### 2. Add All Files

```bash
# Add all files to staging
git add .

# Check what files will be committed
git status
```

### 3. Make Initial Commit

```bash
# Create initial commit
git commit -m "Initial commit: CMI Behavior Classifier Web App

- Complete Streamlit web application
- Pre-trained RandomForest model integration
- Single and batch prediction functionality
- Demo mode with realistic sample data
- Comprehensive documentation and setup scripts"
```

## 🌐 Connect to Remote Repository

### Option 1: GitHub (Recommended)

1. **Create a new repository on GitHub**

   - Go to https://github.com
   - Click "New repository"
   - Name it: `CMI-Behavior-Classifier`
   - Make it public or private
   - Don't initialize with README (we already have one)

2. **Connect to GitHub repository**

   ```bash
   # Add remote origin (replace YOUR_USERNAME with your GitHub username)
   git remote add origin https://github.com/YOUR_USERNAME/CMI-Behavior-Classifier.git

   # Set main as default branch
   git branch -M main

   # Push to GitHub
   git push -u origin main
   ```

### Option 2: GitLab

1. **Create a new repository on GitLab**

   - Go to https://gitlab.com
   - Click "New project"
   - Name it: `CMI-Behavior-Classifier`

2. **Connect to GitLab repository**
   ```bash
   git remote add origin https://gitlab.com/YOUR_USERNAME/CMI-Behavior-Classifier.git
   git branch -M main
   git push -u origin main
   ```

### Option 3: Bitbucket

1. **Create a new repository on Bitbucket**

   - Go to https://bitbucket.org
   - Click "Create repository"
   - Name it: `CMI-Behavior-Classifier`

2. **Connect to Bitbucket repository**
   ```bash
   git remote add origin https://bitbucket.org/YOUR_USERNAME/CMI-Behavior-Classifier.git
   git branch -M main
   git push -u origin main
   ```

## 📁 Project Structure

Your repository should contain:

```
CMI-Behavior-Classifier/
├── app.py                 # Main Streamlit application
├── run_app.py            # Startup script with dependency checks
├── setup.py              # Automated setup script
├── requirements.txt      # Python dependencies
├── README.md            # Comprehensive documentation
├── .gitignore           # Git ignore rules
└── models/
    ├── model.pkl        # Pre-trained RandomForest model
    └── encoders.pkl     # Feature encoders for categorical variables
```

## 🔄 Future Updates

### Making Changes and Pushing

```bash
# After making changes to your code
git add .
git commit -m "Description of your changes"
git push
```

### Pulling Updates (if collaborating)

```bash
git pull origin main
```

## 🎯 Repository Features

Your repository now includes:

### ✅ **Complete Web Application**

- Streamlit-based UI with modern design
- Single prediction with pre-loaded realistic values
- Batch prediction with CSV upload

### ✅ **Comprehensive Documentation**

- Detailed README with setup instructions
- Troubleshooting guide
- Usage examples
- Technical architecture overview

### ✅ **Automated Setup**

- `setup.py` script for easy installation
- Dependency management with `requirements.txt`
- Virtual environment setup
- Model file verification

### ✅ **Testing & Quality**

- Error handling and validation
- Performance optimizations
- Pre-loaded realistic values for testing

### ✅ **Developer Experience**

- `.gitignore` for clean repository
- Clear project structure
- Multiple running methods
- Cross-platform compatibility

## 🌟 Repository Badges (Optional)

Add these badges to your README.md for a professional look:

```markdown
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.33+-red.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
```

## 🎉 Success!

Your CMI Behavior Classifier is now ready for:

- **Public sharing** on GitHub/GitLab/Bitbucket
- **Collaboration** with other developers
- **Deployment** to cloud platforms
- **Documentation** for users and contributors

The repository includes everything needed for someone to clone and run your application successfully!
