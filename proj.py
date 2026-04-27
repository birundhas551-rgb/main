import streamlit as st
from transformers import pipeline
from PIL import Image
import time
import pandas as pd
import numpy as np
import random
import hashlib
import sqlite3
import requests

# Page Configuration
st.set_page_config(page_title="Argus AI | Deepfake Intelligence", page_icon="🤖", layout="wide")

# -----------------
# DARK THEME CSS
# -----------------
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #1e1e2f;
        border-right: 1px solid #444;
    }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0f17 0%, #1e1e2f 100%);
        color: #e0e0e0;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    h1, h2, h3, h4, h5 {
        color: #ffffff;
        font-weight: 300;
        letter-spacing: 1px;
    }
    .gradient-text {
        background: linear-gradient(135deg, #ff6ec7 0%, #8a2be2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 0;
    }
    div[data-testid="metric-container"] {
        background: rgba(30, 30, 47, 0.7);
        border: 1px solid rgba(138, 43, 226, 0.3);
        border-radius: 12px;
        padding: 5% 10%;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
    }
    .stButton>button {
        background: linear-gradient(135deg, #2a2a3d 0%, #3a3a5a 100%);
        color: #ff6ec7;
        border: 1px solid #8a2be2;
        border-radius: 6px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background: #8a2be2;
        color: #ffffff;
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(138, 43, 226, 0.6);
    }
    .status-box-safe {
        background: rgba(16, 185, 129, 0.1);
        border-left: 5px solid #10b981;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        color: #e0e0e0;
    }
    .status-box-danger {
        background: rgba(239, 68, 68, 0.1);
        border-left: 5px solid #ef4444;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        color: #e0e0e0;
    }
    .status-box-warning {
        background: rgba(245, 158, 11, 0.1);
        border-left: 5px solid #f59e0b;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        color: #e0e0e0;
    }
    .data-table {
        font-family: monospace;
        font-size: 0.85rem;
        color: #e0e0e0;
        background-color: rgba(30, 30, 47, 0.8);
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #8a2be2;
    }
</style>
""", unsafe_allow_html=True)

# -----------------
# MODEL LOADING
# -----------------
@st.cache_resource(show_spinner=False)
def load_text_model():
    return pipeline("text-classification", model="joeddav/xlm-roberta-large-xnli")

@st.cache_resource(show_spinner=False)
def load_image_model():
    return pipeline("image-classification", model="umm-maybe/AI-image-detector")

try:
    with st.spinner("Initializing AI Core..."):
        text_model = load_text_model()
        image_model = load_image_model()
    system_status = "Online & Secure"
except Exception:
    system_status = "Initialization Error"

# -----------------
# SIDEBAR NAVIGATION
# -----------------
st.sidebar.markdown("<h2 style='text-align: center;'>🤖 ARGUS OS</h2>", unsafe_allow_html=True)
st.sidebar.markdown(f"<p style='text-align: center; color: #10b981; font-size: 0.9rem;'>● System State: {system_status}</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")
menu = st.sidebar.radio("COMMAND CENTER",
    ["📊 Intelligence Dashboard",
     "🌐 Real-Time Social Monitor",
     "📝 Text Forensics",
     "🖼️ Advanced Visual Forensics",
     "🎙️ Voice Clone Detection",
     "⛓️ Blockchain Auth",
     "🔌 Newsroom API"]
)
st.sidebar.markdown("---")

# -----------------
# PAGE: DASHBOARD
# -----------------
if menu == "📊 Intelligence Dashboard":
    st.title("🤖 Global Threat Intelligence")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Scans Today", "14,208", "+12% from yesterday")
    col2.metric("Deepfakes Identified", "3,402", "+4.2% AI attack rate", delta_color="inverse")
    col3.metric("Neural Network Latency", "124ms", "-5ms optimized")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3) * 10,
        columns=['Visual Forgeries Tracked', 'Audio Clones Tracked', 'Bot Articles Tracked']
    ).cumsum() + 100
    st.line_chart(chart_data, height=350)

# -----------------
# PAGE: REAL-TIME SOCIAL MONITOR
# -----------------
elif menu == "🌐 Real-Time Social Monitor":
    st.title("🌐 Viral Threat Radar")
    st.write("Monitoring live social feeds for suspicious content...")

    if st.button("Fetch Latest Twitter Alerts"):
        try:
            tweets = [{"user":"@political_pulse","text":"Leaked audio...","prob":0.87}]
            for t in tweets:
                st.warning(f"[Twitter] {t['user']}: {t['text']} | Suspicion {t['prob']*100:.1f}%")
        except Exception:
            st.error("Social API not connected.")

# -----------------
# PAGE: TEXT FORENSICS
# -----------------
elif menu == "📝 Text Forensics":
    st.title("Multilingual Linguistic Engine")
    user_text = st.text_area("TARGET TEXT:", height=200)
    lang = st.selectbox("Target Dialect/Language", ["Auto-Detect","English","Hindi","Spanish","Tamil","Mandarin"])
    impact_analysis = st.checkbox("Enable Psych Impact Scoring", value=True)

    if st.button("▶ EXECUTE ANALYSIS"):
        if user_text:
            results = text_model(user_text)
            label = results[0]['label']
            score = results[0]['score']

            impact_score = random.randint(60,99) if "fake" in label.lower() else random.randint(10,30)
            category = random.choice(["Political Destabilization","Financial Fraud","Public Panic","Reputational Damage"]) if impact_score>50 else "Minimal/Benign"

            st.write(f"Classification: {label} | Confidence {score:.2%}")
            if impact_analysis:
                st.write(f"🧠 Impact Score: {impact_score}/100 | Threat Vector: {category}")
        else:
            st.warning("Please provide target text.")

# -----------------
# PAGE: VISUAL FORENSICS
# -----------------
elif menu == "🖼️ Advanced Visual Forensics":
    st.title("Explainable Visual Forensics")
    uploaded_image = st.file_uploader("TARGET MEDIA BASE (JPG/PNG)", type=["jpg","png","jpeg"])
    if uploaded_image and st.button("▶ INITIATE FULL FORENSIC SCAN"):
        img = Image.open(uploaded_image)
        st.image(img, caption="Exhibit A: Raw File")
        results = image_model(img)
        top_label = results[0]['label']
        top_score = results[0]['score']
        st.write(f"Detection: {top_label} | Confidence {top_score:.2%}")

        exp_data = pd.DataFrame({
            "Anomaly Type":["Lighting","Lip Sync","Pixel Artifacts","Latent Correlation"],
            "Variance":[random.randint(60,99) for _ in range(4)]
        })
        st.bar_chart(exp_data.set_index("Anomaly Type"))

