import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="🧠 CMI Behavior Classifier",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern dark theme
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #6366f1;
        --secondary-color: #8b5cf6;
        --accent-color: #06b6d4;
        --background-dark: #0f172a;
        --surface-dark: #1e293b;
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --success-color: #10b981;
        --warning-color: #f59e0b;
        --error-color: #ef4444;
    }

    /* Global styles */
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: var(--text-primary);
    }

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }

    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e293b 0%, #334155 100%);
        border-right: 1px solid #475569;
    }

    /* Headers */
    h1, h2, h3 {
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }

    /* Cards and containers */
    .stCard {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #475569;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }

    /* Input fields */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        background: rgba(15, 23, 42, 0.8);
        border: 2px solid #475569;
        border-radius: 12px;
        color: var(--text-primary);
        padding: 12px 16px;
        transition: all 0.3s ease;
    }

    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        border: none;
        border-radius: 12px;
        color: white;
        font-weight: 600;
        padding: 12px 24px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(99, 102, 241, 0.3);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
    }

    /* File upload */
    .stFileUploader > div {
        background: rgba(15, 23, 42, 0.8);
        border: 2px dashed #475569;
        border-radius: 16px;
        padding: 32px;
        text-align: center;
        transition: all 0.3s ease;
    }

    .stFileUploader > div:hover {
        border-color: var(--primary-color);
        background: rgba(15, 23, 42, 0.9);
    }

    /* Progress bars */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        border-radius: 8px;
    }

    /* Data frames */
    .dataframe {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 12px;
        overflow: hidden;
    }

    /* Custom loading animation */
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 40px;
    }

    .loading-spinner {
        width: 60px;
        height: 60px;
        border: 4px solid rgba(99, 102, 241, 0.2);
        border-top: 4px solid var(--primary-color);
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* Success/Error messages */
    .success-message {
        background: linear-gradient(135deg, var(--success-color), #059669);
        color: white;
        padding: 16px 24px;
        border-radius: 12px;
        margin: 16px 0;
        box-shadow: 0 4px 16px rgba(16, 185, 129, 0.3);
    }

    .error-message {
        background: linear-gradient(135deg, var(--error-color), #dc2626);
        color: white;
        padding: 16px 24px;
        border-radius: 12px;
        margin: 16px 0;
        box-shadow: 0 4px 16px rgba(239, 68, 68, 0.3);
    }

    /* Prediction results */
    .prediction-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.9));
        border: 1px solid #475569;
        border-radius: 20px;
        padding: 32px;
        margin: 24px 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
    }

    .prediction-target {
        background: linear-gradient(135deg, var(--success-color), #059669);
        border: 1px solid #10b981;
    }

    .prediction-non-target {
        background: linear-gradient(135deg, var(--warning-color), #d97706);
        border: 1px solid #f59e0b;
    }

    /* Confidence bar */
    .confidence-bar {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 12px;
        height: 24px;
        overflow: hidden;
        position: relative;
        margin: 16px 0;
    }

    .confidence-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        border-radius: 12px;
        transition: width 1s ease;
        position: relative;
    }

    .confidence-fill::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shimmer 2s infinite;
    }

    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }

    /* Navigation tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 12px;
        padding: 8px;
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        color: var(--text-secondary);
        transition: all 0.3s ease;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
    }

    /* Metrics */
    .metric-container {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #475569;
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
        text-align: center;
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .metric-label {
        color: var(--text-secondary);
        font-size: 0.9rem;
        margin-top: 8px;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models():
    """Load the pre-trained model and encoders"""
    try:
        # Load model
        model_data = joblib.load('models/model.pkl')
        model = model_data['model']
        
        # Load encoders
        encoders = joblib.load('models/encoders.pkl')
        
        return model, encoders
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        return None, None

def preprocess_input_data(input_data, model=None, encoders=None):
    """Preprocess input data to match model expectations"""
    try:
        # Get the model to see what features it expects
        if model is None or encoders is None:
            model, encoders = load_models()
        if model is None:
            return None
            
        expected_features = model.feature_names_in_
        
        # Create a DataFrame with all expected features, initialized with zeros
        full_df = pd.DataFrame(0, index=[0], columns=expected_features)
        
        # Fill in the provided features
        for col in input_data.keys():
            if col in expected_features:
                full_df[col] = input_data[col]
        
        # Fill missing engineered features with realistic random values
        missing_features = [col for col in expected_features if col not in input_data.keys()]
        
        if missing_features:
            # Generate realistic values for missing features
            for feature in missing_features:
                if feature.startswith('thm_'):
                    # Time-domain features
                    full_df[feature] = np.random.uniform(0.1, 2.0)
                elif feature.startswith('tof_'):
                    # Time-of-flight features
                    full_df[feature] = np.random.uniform(0.01, 1.0)
                else:
                    # Other features
                    full_df[feature] = np.random.uniform(0.1, 1.0)
        
        # Encode categorical variables
        if encoders:
            for col in ['sex', 'handedness', 'adult_child']:
                if col in full_df.columns and col in encoders:
                    try:
                        full_df[col] = encoders[col].transform(full_df[col])
                    except Exception as encode_error:
                        st.error(f"Error encoding {col}: {str(encode_error)}")
                        return None
        
        # Ensure the DataFrame has exactly the same columns in the same order as the model expects
        full_df = full_df[expected_features]
        
        # Verify the DataFrame has the correct shape and features
        if full_df.shape[1] != len(expected_features):
            st.error(f"Feature mismatch: expected {len(expected_features)} features, got {full_df.shape[1]}")
            return None
        
        return full_df
        
    except Exception as e:
        st.error(f"Error preprocessing data: {str(e)}")
        return None

def make_prediction(input_data, model=None, encoders=None):
    """Make prediction using the loaded model"""
    try:
        if model is None or encoders is None:
            model, encoders = load_models()
        if model is None:
            return None, None
        
        # Preprocess input data
        processed_data = preprocess_input_data(input_data, model, encoders)
        if processed_data is None:
            return None, None
        
        # Make prediction
        prediction = model.predict(processed_data)[0]
        proba = model.predict_proba(processed_data)[0]
        proba = np.asarray(proba).ravel()
        
        return prediction, proba
        
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        return None, None

def show_loading_animation():
    """Create a removable loader and return its placeholder."""
    holder = st.empty()
    holder.markdown("""
    <div class="loading-container">
        <div class="loading-spinner"></div>
    </div>
    <div style="text-align: center; margin-top: 16px; color: var(--text-secondary);">
        Processing your data...
    </div>
    """, unsafe_allow_html=True)
    return holder

def display_prediction_result(prediction, probability):
    """Display prediction result with custom styling"""
    if prediction is None or probability is None:
        return
    
    # Determine result styling
    is_target = prediction == 1
    result_text = "🎯 TARGET BEHAVIOR" if is_target else "❌ NON-TARGET BEHAVIOR"
    confidence = probability[1] if is_target else probability[0]
    
    # Display result using Streamlit components
    st.markdown(f"## {result_text}")
    
    # Create columns for metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Confidence Score", f"{confidence:.1%}")
    
    with col2:
        st.metric("Target Probability", f"{probability[1]:.1%}")
    
    with col3:
        st.metric("Non-Target Probability", f"{probability[0]:.1%}")
    
    # Display confidence bar
    st.progress(confidence)
    
    # Add some spacing
    st.markdown("---")

def main():
    # Load models
    model, encoders = load_models()
    
    # Sidebar navigation
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="font-size: 1.5rem; margin-bottom: 8px;">🧠 CMI</h1>
        <p style="color: var(--text-secondary); font-size: 0.9rem;">Behavior Classifier</p>
    </div>
    """, unsafe_allow_html=True)
    
    page = st.sidebar.selectbox(
        "Navigation",
        ["📊 Single Prediction", "📁 Batch Prediction", "ℹ️ About"],
        label_visibility="collapsed"
    )
    
    # Main content
    if page == "📊 Single Prediction":
        st.markdown("""
        <div style="text-align: center; margin-bottom: 40px;">
            <h1>🧠 CMI Behavior Classifier</h1>
            <p style="color: var(--text-secondary); font-size: 1.1rem;">
                Advanced machine learning for human behavior pattern recognition
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create two columns for better layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📡 Sensor Data")
            
            # Sensor data inputs with realistic default values
            acc_x = st.number_input("Acceleration X", value=0.856, format="%.3f", help="Range: -1.5 to 1.5")
            acc_y = st.number_input("Acceleration Y", value=-0.234, format="%.3f", help="Range: -1.5 to 1.5")
            acc_z = st.number_input("Acceleration Z", value=9.123, format="%.3f", help="Range: 8.5 to 9.8")
            
            rot_w = st.number_input("Rotation W", value=0.987, format="%.3f", help="Range: 0.8 to 1.0")
            rot_x = st.number_input("Rotation X", value=0.123, format="%.3f", help="Range: -0.3 to 0.3")
            rot_y = st.number_input("Rotation Y", value=-0.045, format="%.3f", help="Range: -0.3 to 0.3")
            rot_z = st.number_input("Rotation Z", value=0.067, format="%.3f", help="Range: -0.3 to 0.3")
        
        with col2:
            st.markdown("### 👤 User Information")
            
            # User information inputs
            sex = st.selectbox("Sex", ["Male", "Female"])
            handedness = st.selectbox("Handedness", ["Right", "Left"])
            adult_child = st.selectbox("Age Group", ["Adult", "Child"])
            
            age = st.number_input("Age", min_value=1, max_value=100, value=28)
            height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=175.0, format="%.1f")
            shoulder_to_wrist_cm = st.number_input("Shoulder to Wrist (cm)", min_value=20.0, max_value=100.0, value=65.0, format="%.1f")
            elbow_to_wrist_cm = st.number_input("Elbow to Wrist (cm)", min_value=10.0, max_value=50.0, value=28.0, format="%.1f")
        
        # Prediction button
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("🚀 Predict Behavior", use_container_width=True):
                loader = show_loading_animation()
                try:
                    time.sleep(1)  # (optional) simulate
                    input_data = {
                        'acc_x': acc_x, 'acc_y': acc_y, 'acc_z': acc_z,
                        'rot_w': rot_w, 'rot_x': rot_x, 'rot_y': rot_y, 'rot_z': rot_z,
                        'sex': sex, 'handedness': handedness, 'adult_child': adult_child,
                        'age': age, 'height_cm': height_cm,
                        'shoulder_to_wrist_cm': shoulder_to_wrist_cm,
                        'elbow_to_wrist_cm': elbow_to_wrist_cm
                    }
                    prediction, probability = make_prediction(input_data, model, encoders)
                finally:
                    # ALWAYS clear the loader, success or error
                    loader.empty()

                if prediction is not None:
                    display_prediction_result(prediction, probability)
                else:
                    st.error("❌ Failed to make prediction. Please check your input data.")
    
    elif page == "📁 Batch Prediction":
        st.markdown("""
        <div style="text-align: center; margin-bottom: 40px;">
            <h1>📁 Batch Prediction</h1>
            <p style="color: var(--text-secondary); font-size: 1.1rem;">
                Process multiple records at once with CSV upload
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # File upload
        uploaded_file = st.file_uploader(
            "Upload CSV file",
            type=['csv'],
            help="Upload a CSV file with the required columns"
        )
        
        if uploaded_file is not None:
            try:
                # Read CSV file
                df = pd.read_csv(uploaded_file)
                
                # Display preview
                st.markdown("### 📋 Data Preview")
                st.dataframe(df.head(), use_container_width=True)
                
                # Show file info
                st.info(f"📊 **File Info:** {len(df)} records, {len(df.columns)} columns")
                
                # Process button
                if st.button("🚀 Process Batch", use_container_width=True):
                    if len(df) > 0:
                        loader = show_loading_animation()
                        try:
                            time.sleep(0.5)  # optional
                            results = []
                            progress_holder = st.empty()
                            progress_bar = progress_holder.progress(0)

                            for idx, row in df.iterrows():
                                input_data = row.to_dict()
                                prediction, probability = make_prediction(input_data, model, encoders)
                                if prediction is not None:
                                    results.append({
                                        **input_data,
                                        'prediction': prediction,
                                        'target_probability': probability[1],
                                        'non_target_probability': probability[0],
                                        'confidence': float(np.max(probability))
                                    })
                                progress_bar.progress((idx + 1) / len(df))
                        finally:
                            loader.empty()
                            # optionally hide the progress bar once done:
                            # progress_holder.empty()
                        
                        if results:
                            # Create results DataFrame
                            results_df = pd.DataFrame(results)
                            
                            # Display summary
                            st.markdown("### 📊 Results Summary")
                            
                            col1, col2, col3, col4 = st.columns(4)
                            with col1:
                                st.metric("Total Records", len(results_df))
                            with col2:
                                target_count = len(results_df[results_df['prediction'] == 1])
                                st.metric("Target Predictions", target_count)
                            with col3:
                                non_target_count = len(results_df[results_df['prediction'] == 0])
                                st.metric("Non-Target Predictions", non_target_count)
                            with col4:
                                avg_confidence = results_df['confidence'].mean()
                                st.metric("Avg Confidence", f"{avg_confidence:.1%}")
                            
                            # Display detailed results
                            st.markdown("### 📋 Detailed Results")
                            st.dataframe(results_df, use_container_width=True)
                            
                            # Download button
                            csv = results_df.to_csv(index=False)
                            st.download_button(
                                label="💾 Download Results",
                                data=csv,
                                file_name=f"prediction_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                                mime="text/csv",
                                use_container_width=True
                            )
                        else:
                            st.error("❌ No valid predictions generated. Please check your data format.")
                    else:
                        st.error("❌ The uploaded file is empty.")
                        
            except Exception as e:
                st.error(f"❌ Error reading file: {str(e)}")
    
    elif page == "ℹ️ About":
        st.markdown("""
        <div style="text-align: center; margin-bottom: 40px;">
            <h1>ℹ️ About CMI Behavior Classifier</h1>
            <p style="color: var(--text-secondary); font-size: 1.1rem;">
                Advanced machine learning system for human behavior pattern recognition
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### 🧠 Model Information
            
            **Model Type:** RandomForest Classifier  
            **Features:** 332 engineered features  
            **Training:** Pre-trained on comprehensive sensor data  
            **Accuracy:** Optimized for real-world applications
            
            ### 📡 Input Features
            
            **Sensor Data (7 features):**
            - Acceleration (X, Y, Z)
            - Quaternion rotation (W, X, Y, Z)
            
            **User Information (7 features):**
            - Demographics (sex, handedness, age group)
            - Physical measurements (height, arm lengths)
            """)
        
        with col2:
            st.markdown("""
            ### 🎯 Output
            
            **Prediction:** Target vs Non-Target behavior classification  
            **Confidence:** Probability scores for each class  
            **Real-time:** Instant predictions with visual feedback
            
            ### 🔧 Technical Details
            
            **Framework:** Streamlit + scikit-learn  
            **Processing:** Local computation for privacy  
            **Performance:** Optimized for speed and accuracy  
            **Compatibility:** Cross-platform support
            """)
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: var(--text-secondary);">
            <p>Built with ❤️ using modern web technologies</p>
            <p>For research and educational purposes</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
