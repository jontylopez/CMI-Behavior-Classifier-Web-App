# 🧠 CMI Behavior Classifier Web App

A machine learning web application that classifies human behavior patterns based on sensor data and user characteristics using pre-trained scikit-learn models.

## 🚀 Features

- **📊 Single Prediction**: Input sensor readings and user information for instant behavior predictions
- **📁 Batch Prediction**: Upload CSV files for bulk processing
- **🎯 Real-time Results**: Color-coded predictions with confidence scores
- **💾 Data Export**: Download prediction results as CSV files
- **🎨 Modern UI**: Beautiful and intuitive user interface built with Streamlit

## 📋 Required Input Features

### 📡 Sensor Data (7 features)

- `acc_x`, `acc_y`, `acc_z` - Acceleration values (realistic ranges: -1.5 to 1.5 for X/Y, 8.5-9.8 for Z)
- `rot_w`, `rot_x`, `rot_y`, `rot_z` - Quaternion rotation values (W: 0.8-1.0, X/Y/Z: -0.3 to 0.3)

### 👤 User Information (7 features)

- `sex` - Male/Female
- `handedness` - Right/Left
- `adult_child` - Adult/Child
- `age` - Age in years
- `height_cm` - Height in centimeters
- `shoulder_to_wrist_cm` - Shoulder to wrist measurement
- `elbow_to_wrist_cm` - Elbow to wrist measurement

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Quick Setup (Recommended)

```bash
# Clone the repository
git clone <your-repository-url>
cd CMI-Behavior-Classifier

# Run the automated setup script
python setup.py
```

📖 **For detailed setup instructions after cloning, see [SETUP_AFTER_CLONE.md](SETUP_AFTER_CLONE.md)**

### Manual Step-by-Step Setup

1. **Clone the repository**

   ```bash
   git clone <your-repository-url>
   cd CMI-Behavior-Classifier
   ```

2. **Verify project structure**

   ```bash
   # Ensure you have the following structure:
   ls -la
       # Should show:
    # - app.py
    # - run_app.py
    # - setup.py
    # - requirements.txt
    # - README.md
    # - models/
    #   ├── model.pkl
    #   └── encoders.pkl
   ```

3. **Create and activate virtual environment (recommended)**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Model files are downloaded automatically**

   ```bash
   # The setup.py script will automatically download model files from Google Drive
   # If manual download is needed:
   # Visit: https://drive.google.com/file/d/16ldFJFaC9gUyY7Ezmh-jUrNA8j_xvcOQ/view?usp=sharing
   # Extract to models/ directory
   ```

6. **Test the installation**
   ```bash
   # Run the startup script to check everything
   python run_app.py
   ```

## 🚀 Running the Application

### Method 1: Using the Startup Script (Recommended)

```bash
python run_app.py
```

### Method 2: Direct Streamlit Command

```bash
streamlit run app.py
```

### Method 3: Using Python Module

```bash
python -m streamlit run app.py
```

## 🌐 Accessing the Web App

After running the application:

- **Local URL**: http://localhost:8501
- **Network URL**: http://[your-ip]:8501 (for access from other devices)

The app will automatically open in your default browser.

## 📖 Usage Guide

### 📊 Single Prediction

1. Navigate to the "Single Prediction" page
2. The form is pre-loaded with realistic sensor values
3. Modify values as needed or use the defaults
4. Click "Predict Behavior" to get instant results
5. View color-coded prediction with confidence scores

### 📁 Batch Prediction

1. Navigate to the "Batch Prediction" page
2. Upload a CSV file with the required format
3. Preview the uploaded data
4. Click "Make Batch Predictions" to process all records
5. View summary statistics and detailed results
6. Download results as a CSV file

### 📄 CSV File Format

Your CSV file should contain columns with the following names:

```csv
acc_x,acc_y,acc_z,rot_w,rot_x,rot_y,rot_z,sex,handedness,adult_child,age,height_cm,shoulder_to_wrist_cm,elbow_to_wrist_cm
0.856,-0.234,9.123,0.987,0.123,-0.045,0.067,Male,Right,Adult,28,175.0,65.0,28.0
```

## 🏗️ Technical Architecture

### Model Structure

- **Model Type**: RandomForest Classifier (scikit-learn)
- **Features**: 332 engineered features including:
  - Raw sensor data (7 features)
  - Time-domain features (`thm_1` to `thm_5`)
  - Time-of-flight features (`tof_1_v0` to `tof_5_v63`)
  - User demographics and measurements

### Data Processing Pipeline

1. **Input Validation**: Check for required features and data types
2. **Feature Encoding**: Transform categorical variables using saved encoders
3. **Missing Feature Generation**: Generate engineered features for demo purposes
4. **Model Prediction**: Generate predictions and probability scores
5. **Result Formatting**: Format output with confidence scores and visual feedback

### File Structure

```
CMI-Behavior-Classifier/
├── app.py                 # Main Streamlit application
├── run_app.py            # Startup script with dependency checks
├── setup.py              # Automated setup script
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .gitignore           # Git ignore rules
└── models/
    ├── model.pkl        # Pre-trained RandomForest model
    └── encoders.pkl     # Feature encoders for categorical variables
```

## 🎨 UI Components

### Navigation

- Sidebar navigation between Single Prediction, Batch Prediction, and About pages
- Responsive design that works on desktop and mobile devices

### Input Forms

- **Number Inputs**: For sensor data and measurements with appropriate ranges and help text
- **Select Boxes**: For categorical variables (sex, handedness, age group)
- **File Upload**: Drag-and-drop CSV file upload with validation

### Results Display

- **Color-coded Predictions**: Green for target behavior, red for non-target
- **Confidence Bars**: Visual representation of prediction confidence
- **Metrics**: Detailed probability scores for each class
- **Data Tables**: Interactive tables for batch results

## 🔧 Configuration

### Model Files

- `models/model.pkl`: Pre-trained scikit-learn RandomForest classifier
- `models/encoders.pkl`: Feature encoders for categorical variables

### App Settings

- Page title: "CMI Behavior Classifier"
- Page icon: 🧠
- Layout: Wide layout for better data visualization
- Sidebar: Expanded by default for easy navigation

## 🚨 Error Handling

The application includes comprehensive error handling for:

- **Model Loading Errors**: Graceful fallback if models can't be loaded
- **Data Validation Errors**: Clear error messages for missing or invalid features
- **File Upload Errors**: Validation of CSV format and required columns
- **Prediction Errors**: Error handling for model prediction failures

## 📊 Output Format

### Single Prediction Results

- Prediction label (Target/Non-Target)
- Confidence score (percentage)
- Individual class probabilities
- Visual confidence bar

### Batch Prediction Results

- Summary statistics (total records, target/non-target counts)
- Detailed results table with all original features plus:
  - `prediction`: Predicted class (0=non-target, 1=target)
  - `target_probability`: Probability of target class
  - `non_target_probability`: Probability of non-target class
  - `confidence`: Maximum probability score

## 🔒 Security Considerations

- No sensitive data is stored or transmitted
- All processing is done locally
- File uploads are validated for format and content
- No external API calls or data sharing

## 🐛 Troubleshooting

### Common Issues

1. **Model Loading Error**

   ```bash
   # Check if model files exist
   ls models/
   # If missing, ensure you have the correct model files
   ```

2. **Missing Dependencies**

   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt
   # Or install individually
   pip install streamlit pandas numpy scikit-learn joblib
   ```

3. **Python Version Issues**

   ```bash
   # Check Python version
   python --version
   # Should be 3.8 or higher
   ```

4. **Port Already in Use**

   ```bash
   # Streamlit will automatically try different ports
   # Check the terminal output for the correct URL
   ```

5. **CSV Upload Issues**
   - Verify CSV file contains all 14 required columns
   - Check column names match exactly (case-sensitive)
   - Ensure data types are appropriate

### Performance Issues

- **DataFrame Fragmentation**: Fixed in current version using `pd.concat()`
- **Memory Usage**: Efficient data handling with pandas
- **Model Loading**: Cached for efficient repeated use

## 📈 Performance

- **Model Loading**: Cached for efficient repeated use
- **Single Predictions**: Near-instantaneous results
- **Batch Processing**: Optimized for large datasets
- **Memory Usage**: Efficient data handling with pandas

## 🧪 Testing

### Test the Application

1. Run the application: `python run_app.py`
2. Navigate to Single Prediction page
3. Use the pre-loaded realistic values
4. Verify predictions work correctly

## 🤝 Contributing

This application is designed to work with pre-trained models. To contribute:

1. Ensure your models are compatible with scikit-learn
2. Test with sample data before deployment
3. Follow the established code structure and error handling patterns
4. Update requirements.txt if adding new dependencies

## 📄 License

This project is designed for educational and research purposes. Please ensure you have appropriate permissions for any models or data used.

## 🆘 Support

### Getting Help

1. Check the troubleshooting section above
2. Verify your Python version and dependencies
3. Test with the pre-loaded realistic values
4. Check the terminal output for error messages

### Common Commands

```bash
# Check Python version
python --version

# Check installed packages
pip list

# Run startup check
python run_app.py
```

---

**Built with ❤️ using Streamlit and scikit-learn**

For support or questions, please refer to the technical documentation or contact your system administrator.
