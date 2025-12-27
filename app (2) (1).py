import streamlit as st
from stego_utils import (
    generate_key, encrypt_message, decrypt_message,
    encode_image, decode_image, compute_psnr, capacity_bytes_from_image_bytes
)
import io


# ============ PAGE CONFIG & STYLING ============


st.set_page_config(
    page_title="Hybrid Crypto-Stego",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Custom CSS for modern, majestic design
custom_css = """
<style>
    * {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Main Background */
    body {
        background: linear-gradient(135deg, #0f0f1e 0%, #1a1a3e 50%, #0f2e4d 100%);
        color: #e0e0e0;
    }
    
    /* Header Styling */
    .main-title {
        text-align: center;
        background: linear-gradient(135deg, #00d4ff, #0099ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5em;
        font-weight: 900;
        margin-bottom: 0.5em;
        letter-spacing: 2px;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
    }
    
    .subtitle {
        text-align: center;
        color: #a0aec0;
        font-size: 1.1em;
        margin-bottom: 2em;
        letter-spacing: 1px;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1em;
        background: rgba(20, 20, 40, 0.6);
        padding: 1em;
        border-radius: 12px;
        border: 1px solid rgba(0, 212, 255, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(50, 50, 80, 0.5);
        border-radius: 8px;
        padding: 0.8em 1.5em;
        border: 1px solid rgba(0, 150, 255, 0.3);
        color: #a0aec0;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00d4ff, #0099ff);
        color: white;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4);
    }
    
    /* Container Styling */
    .content-container {
        background: rgba(20, 25, 50, 0.7);
        border-radius: 15px;
        padding: 2em;
        border: 1px solid rgba(0, 212, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Header in Tabs */
    .stTabs [data-baseweb="tab-list"] h2 {
        color: #00d4ff;
        font-weight: 800;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #4f46e5);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.7em 1.5em;
        font-weight: 600;
        font-size: 1em;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #4f46e5, #4338ca);
        box-shadow: 0 6px 25px rgba(99, 102, 241, 0.4);
        transform: translateY(-2px);
    }
    
    /* Text Area Styling */
    .stTextArea textarea {
        background: rgba(40, 50, 80, 0.6);
        color: #e0e0e0;
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 8px;
        padding: 1em;
    }
    
    /* File Uploader */
    .stFileUploader {
        border: 2px dashed rgba(0, 212, 255, 0.4);
        border-radius: 12px;
        background: rgba(40, 50, 80, 0.4);
        padding: 2em;
    }
    
    /* Messages */
    .stSuccess {
        background: rgba(34, 197, 94, 0.15);
        border: 1px solid rgba(34, 197, 94, 0.5);
        border-radius: 8px;
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.15);
        border: 1px solid rgba(239, 68, 68, 0.5);
        border-radius: 8px;
    }
    
    .stWarning {
        background: rgba(245, 158, 11, 0.15);
        border: 1px solid rgba(245, 158, 11, 0.5);
        border-radius: 8px;
    }
    
    .stInfo {
        background: rgba(59, 130, 246, 0.15);
        border: 1px solid rgba(59, 130, 246, 0.5);
        border-radius: 8px;
    }
    
    /* Code Block */
    .stCodeBlock {
        background: rgba(20, 20, 35, 0.8);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 8px;
    }
    
    /* Sidebar */
    .stSidebar {
        background: rgba(15, 15, 30, 0.9);
        border-right: 1px solid rgba(0, 212, 255, 0.2);
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, rgba(0, 212, 255, 0.3), transparent);
    }
    
    /* Column Headers */
    h3 {
        color: #00d4ff;
        font-weight: 700;
    }
    
    /* General Text */
    p, span {
        color: #d0d0e0;
    }
</style>
"""


st.markdown(custom_css, unsafe_allow_html=True)


# ============ TITLE & DESCRIPTION ============


st.markdown('<div class="main-title">🔐 Hybrid Crypto-Stego</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Secure Message Hiding Through Encryption & Steganography</div>', unsafe_allow_html=True)


st.markdown("""
<div style="text-align: center; color: #a0aec0; margin-bottom: 2em; font-size: 0.95em;">
Send secret messages securely by encrypting them with Fernet and hiding them inside images using LSB steganography.
</div>
""", unsafe_allow_html=True)


# ============ TABS ============


tabs = st.tabs(["📤 Sender", "📥 Receiver", "📊 Analysis", "ℹ️ Guide"])


# ============ SESSION STATE SETUP FOR DOWNLOAD TRACKING ============

if 'downloaded_image' not in st.session_state:
    st.session_state.downloaded_image = False
if 'downloaded_key' not in st.session_state:
    st.session_state.downloaded_key = False
if 'show_output' not in st.session_state:
    st.session_state.show_output = False


# ============ TAB 1: SENDER ============


with tabs[0]:
    st.markdown("### Encrypt & Embed Your Secret Message")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**📝 Your Secret Message**")
        message = st.text_area("Enter your secret message here", height=200, placeholder="Type your secret message...")
        
        st.markdown("**🖼️ Cover Image**")
        uploaded = st.file_uploader("Upload a PNG image (recommended for best results)", type=['png', 'jpg', 'jpeg'], key="sender_upload")
    
    with col2:
        st.markdown("**⚙️ Quick Settings**")
        show_capacity = st.checkbox("📊 Show capacity estimate", value=True)
        
        if uploaded and show_capacity:
            try:
                cap = capacity_bytes_from_image_bytes(uploaded.read())
                st.info(f"✅ **Capacity:** {cap} bytes available")
                uploaded.seek(0)
            except Exception:
                st.warning("⚠️ Could not compute capacity for this image.")
    
    st.markdown("---")
    
    if st.button("🔒 Encrypt & Embed Message", use_container_width=True):
        if not message:
            st.error("❌ Please enter a secret message first.")
        elif not uploaded:
            st.error("❌ Please upload a cover image first.")
        else:
            try:
                key = generate_key()
                ciphertext = encrypt_message(message, key)
                
                uploaded.seek(0)
                cover_bytes = uploaded.read()
                
                with st.spinner("🔄 Processing... Embedding data into image..."):
                    stego_bytes = encode_image(cover_bytes, ciphertext)
                
                # Save to session state to persist through reruns
                st.session_state.stego_bytes = stego_bytes
                st.session_state.key = key
                st.session_state.show_output = True
                st.session_state.downloaded_image = False
                st.session_state.downloaded_key = False
                
                st.success("✅ Message successfully encrypted and embedded!")
            
            except Exception as e:
                st.error(f"❌ Embedding failed: {str(e)}")
    
    if st.session_state.show_output:
        
        col_img, col_info = st.columns([2, 1])
        
        with col_img:
            st.image(st.session_state.stego_bytes, caption="📸 Your Stego Image (Preview)", use_container_width=True)
        
        with col_info:
            try:
                psnr = compute_psnr(cover_bytes, st.session_state.stego_bytes)
                st.metric("Image Quality (PSNR)", f"{psnr:.2f} dB", delta="Higher is better")
            except Exception:
                pass
        
        st.markdown("---")
        
        col_download1, col_download2 = st.columns(2)
        
        with col_download1:
            if st.download_button(
                "⬇️ Download Stego Image",
                data=st.session_state.stego_bytes,
                file_name="stego_image.png",
                mime="image/png",
                use_container_width=True
            ):
                st.session_state.downloaded_image = True
        
        with col_download2:
            if st.download_button(
                "⬇️ Download Encryption Key",
                data=st.session_state.key,
                file_name="secret.key",
                mime="application/octet-stream",
                use_container_width=True
            ):
                st.session_state.downloaded_key = True
        
        # Clear output after both downloads with a manual Clear button
        if st.session_state.downloaded_image and st.session_state.downloaded_key:
            st.success("✅ Both files downloaded successfully!")
            if st.button("Clear"):
                st.session_state.show_output = False
                st.session_state.downloaded_image = False
                st.session_state.downloaded_key = False
        
        st.markdown("---")
        st.markdown("**🔑 Your Encryption Key (Share Securely)**")
        st.code(st.session_state.key.decode(), language="text")
        st.info("⚠️ **IMPORTANT:** Share this key securely with the receiver using a separate channel (email, message, etc.)")


# ============ TAB 2: RECEIVER ============


with tabs[1]:
    st.markdown("### Extract & Decrypt Your Message")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**🖼️ Stego Image**")
        stego_file = st.file_uploader("Upload the stego image (PNG)", type=['png'], key="receiver_upload")
        
        st.markdown("**🔑 Encryption Key**")
        key_input = st.text_area("Paste the encryption key (exact copy)", height=100, placeholder="Paste the key here...")
    
    with col2:
        st.markdown("**💡 Tips**")
        st.info("""
        • Copy the key exactly as provided
        • No extra spaces or newlines
        • Make sure both files are original
        """)
    
    st.markdown("---")
    
    if st.button("🔓 Extract & Decrypt Message", use_container_width=True):
        if not stego_file:
            st.error("❌ Please upload the stego image.")
        elif not key_input:
            st.error("❌ Please provide the decryption key.")
        else:
            try:
                stego_file.seek(0)
                raw = stego_file.read()
                
                with st.spinner("🔄 Processing... Extracting and decrypting message..."):
                    ciphertext = decode_image(raw)
                    message = decrypt_message(ciphertext, key_input.encode())
                
                st.success("✅ Message successfully recovered and decrypted!")
                st.markdown("---")
                st.markdown("**📝 Your Recovered Message**")
                st.text_area("Decrypted Message", value=message, height=200, disabled=True)
                
                st.info("💾 The message has been successfully extracted!")
                
            except Exception as e:
                st.error("❌ Extraction or decryption failed.")
                st.warning("Possible reasons:\n• Incorrect encryption key\n• Image is corrupted\n• Wrong stego image format")


# ============ TAB 3: ANALYSIS ============


with tabs[2]:
    st.markdown("### Image Quality Analysis")
    
    st.markdown("Compare two images and calculate their PSNR (Peak Signal-to-Noise Ratio) to measure image quality degradation.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Original Cover Image**")
        cover_for_psnr = st.file_uploader("Upload cover image (PNG)", type=['png'], key="cpsnr")
    
    with col2:
        st.markdown("**Stego Image**")
        stego_for_psnr = st.file_uploader("Upload stego image (PNG)", type=['png'], key="spsnr")
    
    st.markdown("---")
    
    if st.button("📊 Calculate PSNR", use_container_width=True):
        if not cover_for_psnr or not stego_for_psnr:
            st.error("❌ Please upload both images.")
        else:
            try:
                with st.spinner("🔄 Calculating PSNR..."):
                    psnr = compute_psnr(cover_for_psnr.read(), stego_for_psnr.read())
                
                col_metric1, col_metric2 = st.columns(2)
                
                with col_metric1:
                    st.metric("PSNR Value", f"{psnr:.2f} dB")
                
                with col_metric2:
                    if psnr > 40:
                        quality_text = "Excellent"
                        color = "green"
                    elif psnr > 30:
                        quality_text = "Good"
                        color = "blue"
                    elif psnr > 20:
                        quality_text = "Fair"
                        color = "orange"
                    else:
                        quality_text = "Poor"
                        color = "red"
                    st.markdown(f"<h3 style='color: {color};'>Quality: {quality_text}</h3>", unsafe_allow_html=True)
                
                st.info("""
                **PSNR Guidelines:**
                - **> 40 dB:** Excellent quality (imperceptible changes)
                - **30-40 dB:** Good quality (slight degradation)
                - **20-30 dB:** Fair quality (visible degradation)
                - **< 20 dB:** Poor quality (significant degradation)
                """)
                
            except Exception as e:
                st.error("❌ PSNR calculation failed.")


# ============ TAB 4: GUIDE ============


with tabs[3]:
    st.markdown("### 📚 Complete Guide")
    
    st.markdown("#### How It Works")
    st.markdown("""
    **Step 1: Sender encrypts the message**
    - Your secret message is encrypted using Fernet (AES-128 + HMAC authentication)
    - This creates an encrypted ciphertext
    
    **Step 2: Sender embeds ciphertext in image**
    - The ciphertext is hidden in the Least Significant Bits (LSB) of image pixels
    - The image visually appears unchanged to the human eye
    - The stego image and encryption key are sent to the receiver
    
    **Step 3: Receiver extracts and decrypts**
    - The receiver extracts the LSB bits from the stego image
    - Uses the encryption key to decrypt the message
    - Original message is recovered
    """)
    
    st.markdown("#### Key Features")
    col_feat1, col_feat2 = st.columns(2)
    
    with col_feat1:
        st.markdown("""
        ✅ **Double Security**
        - Encryption (what) + Steganography (where)
        
        ✅ **Fernet Encryption**
        - Military-grade AES-128
        - HMAC authentication
        
        ✅ **LSB Steganography**
        - Minimal image quality loss
        - High capacity storage
        """)
    
    with col_feat2:
        st.markdown("""
        ✅ **PNG Recommended**
        - Lossless compression
        - Best for data preservation
        
        ✅ **Quality Metrics**
        - PSNR measurement included
        - Monitor image degradation
        
        ✅ **User Friendly**
        - No technical knowledge needed
        - Simple three-step process
        """)
    
    st.markdown("---")
    
    st.markdown("#### ⚠️ Important Tips")
    st.warning("""
    • **Use PNG images** - Avoid JPG (lossy compression destroys hidden data)
    • **Don't compress after embedding** - WhatsApp, Instagram will corrupt data
    • **Share key separately** - Never send key with stego image together
    • **Larger images work better** - More space for data embedding
    • **Check PSNR** - High PSNR (>35dB) means better image quality
    """)
    
    st.markdown("#### 📸 Image Requirements")
    st.info("""
    **Minimum Image Size:** 100x100 pixels
    
    **Recommended:** 500x500+ pixels for longer messages
    
    **File Format:** PNG (24-bit RGB)
    
    **Message Capacity:** Roughly 1/3 of image file size in bytes
    """)
    
    st.markdown("---")
    
    st.markdown("#### About This Project")
    st.markdown("""
    **Author:** 
    - Korivi Sai Praneeth  
    - ADHIREDDY LAKSHMAN
    - CHANDRU M
            
    **Department:** 
    - Artificial Intelligence & Data Science
    - Artificial Intelligence & Machine Learning
    
    
    **Technology Stack:**
    - Streamlit (Web UI)
    - Cryptography (Fernet encryption)
    - PIL & NumPy (Image processing)
    
    **License:** Educational Use
    """)


# ============ FOOTER ============


st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.85em; margin-top: 2em;">
🔐 Hybrid Cryptographic Steganography System | Secure Communication Made Simple
</div>
""", unsafe_allow_html=True)
