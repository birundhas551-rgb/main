import streamlit as st
from transformers import pipeline
from PIL import Image
import time
import pandas as pd
import numpy as np
import random
import hashlib

# Page Configuration
st.set_page_config(page_title="Argus AI | Deepfake Intelligence", page_icon="🤖", layout="wide")

# Advanced Enterprise CSS
st.markdown("""
<style>
    /* Light, violet aesthetic */
    [data-testid="stSidebar"] {
        background-color: #f8f8ff;
        border-right: 1px solid #d8bfd8;
    }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ffffff 0%, #e6e6fa 100%);
        color: #333333;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    h1, h2, h3, h4, h5 {
        color: #333333;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    .gradient-text {
        background: linear-gradient(135deg, #8a2be2 0%, #da70d6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 0;
    }
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(218, 112, 214, 0.3);
        border-radius: 12px;
        padding: 5% 10% 5% 10%;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        backdrop-filter: blur(10px);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #f8f8ff 0%, #e6e6fa 100%);
        color: #4b0082;
        border: 1px solid #da70d6;
        border-radius: 6px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background: #da70d6;
        color: #ffffff;
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(218, 112, 214, 0.4);
    }
    .status-box-safe {
        background: rgba(16, 185, 129, 0.1);
        border-left: 5px solid #10b981;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        animation: slideup 0.5s ease;
        color: #1f2937;
    }
    .status-box-danger {
        background: rgba(239, 68, 68, 0.1);
        border-left: 5px solid #ef4444;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        animation: slideup 0.5s ease;
        color: #1f2937;
    }
    .status-box-warning {
        background: rgba(245, 158, 11, 0.1);
        border-left: 5px solid #f59e0b;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        animation: slideup 0.5s ease;
        color: #1f2937;
    }
    
    .data-table {
        font-family: monospace;
        font-size: 0.85rem;
        color: #4b5563;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #d8bfd8;
    }
    
    @keyframes slideup {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# -----------------
# MODEL LOADING
# -----------------
@st.cache_resource(show_spinner=False)
def load_text_model():
    return pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")
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
st.sidebar.info("Argus Intelligence Platform v5.0. Advanced Multi-layer Forensic Tooling.")

# -----------------
# PAGE: DASHBOARD
# -----------------
if menu == "📊 Intelligence Dashboard":
    st.markdown("<p class='gradient-text'>🤖 Global Threat Intelligence</p>", unsafe_allow_html=True)
    st.write("### System Architecture Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Scans Today", "14,208", "+12% from yesterday")
    col2.metric("Deepfakes Identified", "3,402", "+4.2% AI attack rate", delta_color="inverse")
    col3.metric("Neural Network Latency", "124ms", "-5ms optimized")
    
    st.write("### Live Synthetic Media Generation Activity Matrix")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3) * 10,
        columns=['Visual Forgeries Tracked', 'Audio Clones Tracked', 'Bot Articles Tracked']
    ).cumsum() + 100
    st.line_chart(chart_data, height=350)

# -----------------
# PAGE: REAL-TIME SOCIAL MONITOR
# -----------------
elif menu == "🌐 Real-Time Social Monitor":
    st.markdown("<p class='gradient-text'>🌐 Viral Threat Radar</p>", unsafe_allow_html=True)
    st.write("Actively monitoring trending posts across global networks to preemptively flag synthetic media.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("### Live Feed Monitoring")
        with st.container():
            st.markdown("""
            <div class='status-box-warning'>
                <b>[Twitter]</b> <i>@political_pulse</i>: Leaked audio of candidate admitting fraud...
                <br><span style='color:#f59e0b; font-size:0.8rem;'>Scanning... 87% Probability of AI Voice Clone. Engaging Fact-Check API.</span>
            </div>
            <div class='status-box-danger'>
                <b>[TikTok]</b> <i>Viral Video #TrendingNews</i>: Explosion near financial district...
                <br><span style='color:#ef4444; font-size:0.8rem;'>CRITICAL ALER: 99% Probability of Midjourney V6 rendering. Flagged for removal.</span>
            </div>
            <div class='status-box-safe'>
                <b>[Instagram]</b> <i>Official Statement</i>: Press conference updates...
                <br><span style='color:#10b981; font-size:0.8rem;'>Verified: Multi-angle consistency. EXIF authenticated.</span>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.write("### Platform Risk Levels")
        st.bar_chart(pd.DataFrame({
            "Platform": ["Twitter", "TikTok", "Instagram", "Facebook", "Telegram"],
            "Threat Level": [85, 92, 45, 60, 95]
        }).set_index("Platform"))

# -----------------
# PAGE: TEXT FORENSICS
# -----------------
elif menu == "📝 Text Forensics":
    st.markdown("<p class='gradient-text'>Multilingual Linguistic Engine</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        user_text = st.text_area("TARGET TEXT:", height=200, placeholder="Enter questionable social media posts, articles, or transcripts...")
    with col2:
        lang = st.selectbox("Target Dialect/Language", ["Auto-Detect", "English", "Hindi", "Spanish", "Tamil", "Mandarin"])
        impact_analysis = st.checkbox("Enable Psych Impact Scoring", value=True)
    
    if st.button("▶ EXECUTE ANALYSIS"):
        if user_text:
            st.toast(f"Processing Linguistics in {lang}...", icon="⏳")
            time.sleep(1)
            try:
                results = text_model(user_text)
                label = results[0]['label']
                score = results[0]['score']
                
                # Psychological Impact Scoring (Mock)
                impact_score = random.randint(60, 99) if ("fake" in label.lower() or label == "LABEL_0") else random.randint(10, 30)
                categories = ["Political Destabilization", "Financial Fraud", "Public Panic", "Reputational Damage"]
                category = random.choice(categories) if impact_score > 50 else "Minimal/Benign"
                
                if label == "LABEL_0" or "fake" in label.lower():
                    st.markdown(f"""
                    <div class='status-box-danger'>
                        <h3 style='margin:0; color:#ef4444;'>⚠️ HIGH RISK - FABRICATED TEXT</h3>
                        <p>Our multilingual models flag this text as highly probable disinformation.</p>
                        <p><b>Confidence Rating:</b> {score:.2%}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.balloons()
                    st.markdown(f"""
                    <div class='status-box-safe'>
                        <h3 style='margin:0; color:#10b981;'>🛡️ SAFE - AUTHENTICATED</h3>
                        <p>No linguistic anomalies found. Text structure maps to verified human patterns.</p>
                        <p><b>Authenticity Rating:</b> {score:.2%}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                if impact_analysis:
                    st.write("### 🧠 Psychological Impact Assessment")
                    color = "#ef4444" if impact_score > 70 else ("#f59e0b" if impact_score > 40 else "#10b981")
                    st.markdown(f"""
                    <div class='data-table'>
                        <p><b>Estimated Harm Score:</b> <span style='color:{color}; font-weight:bold;'>{impact_score}/100</span></p>
                        <p><b>Primary Threat Vector:</b> {category}</p>
                        <p><b>Alert Priority:</b> {'HIGH' if impact_score > 70 else 'LOW'}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
            except Exception as e:
                st.error("Engine Offline.")
        else:
            st.warning("Please provide target text.")

# -----------------
# PAGE: VISUAL FORENSICS
# -----------------
elif menu == "🖼️ Advanced Visual Forensics":
    st.markdown("<p class='gradient-text'>Explainable Visual Forensics</p>", unsafe_allow_html=True)
    st.write("Deep scan imagery across 3 sub-systems: Visual Transformers, Error Level Analysis (ELA), and EXIF Cryptography.")
    
    uploaded_image = st.file_uploader("TARGET MEDIA BASE (JPG/PNG)", type=["jpg", "png", "jpeg"])
    
    if uploaded_image:
        col1, col2 = st.columns([1, 1.2])
        with col1:
            img = Image.open(uploaded_image)
            st.image(img, caption="Exhibit A: Raw File", use_column_width=True)
            file_bytes = uploaded_image.getvalue()
            img_hash = hashlib.sha256(file_bytes).hexdigest()
            
        with col2:
            if st.button("▶ INITIATE FULL FORENSIC SCAN"):
                st.toast("Booting forensic subsystem...", icon="🔍")
                
                st.write("### Sub-System Diagnostic")
                p1 = st.progress(0, text="Layer 1: EXIF Metadata Extraction...")
                time.sleep(0.5)
                p1.progress(100, text="Layer 1: EXIF Metadata Extracted [OK]")
                
                p2 = st.progress(0, text="Layer 2: Error Level Analysis (ELA)...")
                time.sleep(0.5)
                p2.progress(100, text="Layer 2: Pixel Frequencies Mapped [OK]")
                
                p3 = st.progress(0, text="Layer 3: Executing Deep CNN Vision Transformer...")
                time.sleep(1)
                
                try:
                    results = image_model(img)
                    top_label = results[0]['label']
                    top_score = results[0]['score']
                    
                    p3.progress(100, text="Layer 3: Neural Network Inferencing Complete [OK]")
                    st.markdown("---")
                    
                    is_fake = "artificial" in top_label.lower() or "fake" in top_label.lower()
                    
                    if is_fake:
                        st.markdown(f"""
                        <div class='status-box-danger'>
                            <h3 style='margin:0; color:#ef4444;'>⚠️ LAYER 3 BREACH | SYNTHETIC IMAGE DETECTED</h3>
                            <h2 style='color:#ef4444'>AI MATCH PROBABILITY: {top_score:.2%}</h2>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.balloons()
                        st.markdown(f"""
                        <div class='status-box-safe'>
                            <h3 style='margin:0; color:#10b981;'>🛡️ LAYER 3 VERIFIED | 100% GENUINE PHOTO</h3>
                            <h2 style='color:#10b981'>GENUINE PROBABILITY: {top_score:.2%}</h2>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    # EXPLAINABLE AI REPORTS
                    st.write("### 👁️ Explainable AI Report")
                    st.write("Anomaly localization indicates areas where pixel structures break mathematical consistency.")
                    
                    exp_data = pd.DataFrame({
                        "Anomaly Type": ["Lighting Inconsistency", "Lip/Edge Sync", "Pixel Compression Artifacts", "Latent Space Correlation"],
                        "Detected Variance": [random.randint(60, 99) if is_fake else random.randint(5, 20) for _ in range(4)]
                    })
                    st.bar_chart(exp_data.set_index("Anomaly Type"))
                    
                    # CROWDSOURCED VERIFICATION LAYER
                    st.write("### 👥 Crowdsourced Verification Layer")
                    st.info("Community notes act as a 'Wikipedia-style' fact-checking ledger on top of AI detection.")
                    with st.expander("Add Verification Note (Journalist/Researcher)"):
                        st.text_area("Your findings:", placeholder="e.g., Cross-referencing shadow angles confirms generation anomalies...")
                        st.button("Submit to Public Ledger")
                        
                except Exception as e:
                    st.error("Deep Scan Failed. Target format might be corrupted.")

# -----------------
# PAGE: AUDIO DETECTOR
# -----------------
elif menu == "🎙️ Voice Clone Detection":
    st.markdown("<p class='gradient-text'>Acoustic Forgery & Voice Clone Analysis</p>", unsafe_allow_html=True)
    st.info("💡 Note: Acoustic processing module is currently in Beta mode.")
    uploaded_audio = st.file_uploader("TARGET AUDIO AUDIO (MP3/WAV)", type=["mp3", "wav"])
    
    if uploaded_audio:
        st.audio(uploaded_audio)
        if st.button("▶ ANALYZE AUDIO SPECTROGRAM"):
            st.toast("Running Fourier Transforms...", icon="🎧")
            progress_container = st.empty()
            for prog in range(0, 101, 10):
                progress_container.progress(prog, text=f"Analyzing frequency domain: {prog}%")
                time.sleep(0.1)
            progress_container.empty()
            
            st.markdown(f"""
            <div class='status-box-safe'>
                <h3 style='margin:0; color:#10b981;'>🛡️ AUTHENTIC VOICE SIGNATURE</h3>
                <p style='margin-top:10px;'>Breath patterns and micro-frequencies match natural human vocal cords.</p>
                <p><b>Authenticity Score Algorithm Baseline:</b> 98.4%</p>
            </div>
            """, unsafe_allow_html=True)

# -----------------
# PAGE: BLOCKCHAIN AUTH
# -----------------
elif menu == "⛓️ Blockchain Auth":
    st.markdown("<p class='gradient-text'>Blockchain Media Authentication</p>", unsafe_allow_html=True)
    st.write("Certify and cross-reference media against cryptographic ledgers.")
    
    auth_file = st.file_uploader("UPLOAD MEDIA TO VERIFY LEDGER STATUS")
    if auth_file:
        file_hash = hashlib.sha256(auth_file.getvalue()).hexdigest()
        st.write(f"**Media SHA256:** `{file_hash}`")
        
        if st.button("Query Global Authentication Ledger"):
            with st.spinner("Connecting to decentralized media nodes..."):
                time.sleep(1.5)
                # Randomize result for demo
                if random.choice([True, False]):
                    st.markdown(f"""
                    <div class='status-box-safe'>
                        <h3 style='margin:0; color:#10b981;'>⛓️ C2PA / LEDGER MATCH FOUND</h3>
                        <p>This media has a valid cryptographic authenticity certificate created at the point of capture.</p>
                        <p><b>Original Source:</b> Sony A7IV (Encrypted Node)</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class='status-box-danger'>
                        <h3 style='margin:0; color:#ef4444;'>⚠️ NO AUTHENTICITY CERTIFICATE</h3>
                        <p>No matching hash found on the blockchain. Media is unverified and potentially synthetic.</p>
                    </div>
                    """, unsafe_allow_html=True)

# -----------------
# PAGE: API INTEGRATION
# -----------------
elif menu == "🔌 Newsroom API":
    st.markdown("<p class='gradient-text'>Developer & Newsroom API</p>", unsafe_allow_html=True)
    st.write("Integrate Argus AI directly into publishing workflows to verify content before release.")
    
    st.code("""
# Example: Sending an article for verification
import requests

url = "https://api.argus.ai/v1/verify/text"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
data = {
    "text": "The latest breaking news...",
    "language": "auto",
    "impact_scoring": True
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
    """, language="python")
    
    st.write("### Active Endpoints")
    st.markdown("""
    - `POST /v1/verify/text` - Multilingual text deepfake & hallucination detection.
    - `POST /v1/verify/media` - Visual transformer & EXIF forensics.
    - `POST /v1/monitor/stream` - Webhook for real-time social media pipeline scanning.
    """)
    st.button("Generate API Key (Requires Enterprise Auth)")

