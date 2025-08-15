# 🚀 Setup Guide After Cloning

This guide explains what files you need to manually add after cloning the CMI Behavior Classifier repository and how to do it.

## 📋 What's Included in Git

The following files are **automatically included** when you clone the repository:

### ✅ **Core Application Files**

- `app.py` - Main Streamlit application
- `run_app.py` - Application launcher with dependency checks
- `requirements.txt` - Python dependencies
- `setup.py` - Automated setup script (includes model download)
- `README.md` - Project documentation
- `GIT_SETUP.md` - Git setup instructions
- `.gitignore` - Git ignore rules

### ⬇️ **Model Files** (Downloaded automatically)

- `models/model.pkl` - Pre-trained RandomForest model (199MB)
- `models/encoders.pkl` - Feature encoders for categorical variables

**Note**: Model files are **NOT included** in Git due to size limits (199MB exceeds GitHub's 100MB limit). They are automatically downloaded during setup.

## 🔧 What You Need to Do After Cloning

### 1. **Install Dependencies**

```bash
# Option 1: Use the automated setup script (Recommended)
python setup.py

# Option 2: Manual installation
pip install -r requirements.txt
```

### 2. **Model Files Are Downloaded Automatically**

The `setup.py` script will automatically:

- Download model files from Google Drive
- Extract them to the `models/` directory
- Verify they are working correctly

**Manual Download (if automatic fails):**

```bash
# Download from Google Drive
# https://drive.google.com/file/d/16ldFJFaC9gUyY7Ezmh-jUrNA8j_xvcOQ/view?usp=sharing

# Extract to models/ directory
# models/model.pkl
# models/encoders.pkl
```

### 3. **Run the Application**

```bash
# Option 1: Use the launcher (Recommended)
python run_app.py

# Option 2: Direct Streamlit command
streamlit run app.py
```

## 🎯 **What's Protected by .gitignore**

The following files are **automatically excluded** from Git for security and performance:

### 🔒 **Security & Sensitive Data**

- `.env*` files (environment variables)
- `secrets.json`, `config.json`, `credentials.json`
- `*.key`, `*.pem`, `*.p12`, `*.pfx` (certificates/keys)

### 🗂️ **Temporary & Cache Files**

- `__pycache__/`, `*.pyc`, `*.pyo`
- `*.tmp`, `*.temp`, `temp/`, `tmp/`
- `.cache/`, `.pytest_cache/`
- `*.log`, `logs/`

### 🖥️ **OS & IDE Files**

- `.DS_Store` (macOS)
- `Thumbs.db` (Windows)
- `.vscode/`, `.idea/` (IDE settings)

### 📦 **Build & Distribution Files**

- `build/`, `dist/`, `*.egg-info/`
- `venv/`, `env/`, `.venv/` (virtual environments)

### 📁 **Model Files**

- `models/*.pkl` - Excluded due to size limits (199MB)
- `models/*.joblib` - Large model files
- `models/*.h5` - Large model files

## 🚨 **Important Notes**

### ⬇️ **Model Files Are Downloaded Automatically**

- Model files are **NOT included** in Git due to GitHub's 100MB file size limit
- The `setup.py` script automatically downloads them from Google Drive
- If automatic download fails, manual download instructions are provided

### 🔧 **Data Files Are Flexible**

- CSV, JSON, and Excel files are **not excluded** by default
- You can add sample data files if needed
- Uncomment the relevant lines in `.gitignore` if you want to exclude them

### 🛡️ **Security Best Practices**

- Environment variables (`.env` files) are automatically excluded
- Sensitive configuration files are protected
- Log files and temporary data are ignored

## 🎉 **Quick Start Commands**

After cloning, run these commands in order:

```bash
# 1. Navigate to project directory
cd "CMI Behavior Classifier"

# 2. Run automated setup (includes model download)
python setup.py

# 3. Launch the application
python run_app.py
```

## 🔍 **Troubleshooting**

### **Model Files Missing**

If `models/model.pkl` or `models/encoders.pkl` are missing:

1. **Automatic Download Failed:**

   ```bash
   # Run setup again
   python setup.py
   ```

2. **Manual Download:**

   - Visit: https://drive.google.com/file/d/16ldFJFaC9gUyY7Ezmh-jUrNA8j_xvcOQ/view?usp=sharing
   - Download the zip file
   - Extract to `models/` directory

3. **Verify Files:**
   ```bash
   ls models/
   # Should show:
   # - model.pkl
   # - encoders.pkl
   ```

### **Dependencies Issues**

If you encounter dependency problems:

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **Permission Issues**

If you get permission errors:

```bash
# On Windows, run as administrator
# On macOS/Linux, use sudo if needed
sudo python setup.py
```

### **Download Issues**

If the automatic download fails:

1. **Check Internet Connection**
2. **Try Manual Download:**
   - Download from Google Drive manually
   - Extract to `models/` directory
3. **Alternative:**
   - Contact the repository owner for direct file sharing

## 📞 **Support**

If you encounter any issues:

1. Check the troubleshooting section above
2. Review the `README.md` for detailed documentation
3. Ensure all model files are present in the `models/` directory
4. Verify your Python version (3.8+ required)

---

**🎯 The application should work immediately after cloning and running the setup script!**

**📥 Model files will be downloaded automatically from Google Drive during setup.**
