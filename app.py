import streamlit as st
import os
from predict import predict_crop
from voice_input import get_voice_text
from duckduckgo_search import DDGS


def get_crop_image(crop):
    path = f"images/{crop.lower()}.jpg"
    
    if os.path.exists(path):
        return path
    else:
        return "images/default.jpg"

# 🎨 CSS
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.title {
    text-align:center;
    font-size:50px;
    font-weight:800;
    color:#00ffcc;
}

.subtitle {
    text-align:center;
    color:#ccc;
    margin-bottom:20px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,0.1);
}

.result {
    background: linear-gradient(135deg,#00ffcc,#00cc99);
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:black;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# 🌾 Header
st.markdown('<div class="title">🌾 AI Crop Recommendation</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Farming using AI (Kannada + English)</div>', unsafe_allow_html=True)

st.divider()

# 🎯 Layout
col1, col2 = st.columns(2)

# 🎤 VOICE SECTION
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎤 Voice Input")

    if st.button("🎙️ Speak Now"):
        text = get_voice_text()

        if text:
            st.success(f"You said: {text}")

            # ✅ UPDATED
            crop, crop_kn, soil, rainfall, temperature = predict_crop(text)

            st.write("### Conditions")
            st.write(f"🌱 Soil: {soil}")
            st.write(f"🌧 Rainfall: {rainfall}")
            st.write(f"🌡 Temp: {temperature}")

            # ✅ RESULT (ENGLISH + KANNADA)
            st.markdown(
                f'<div class="result">🌾 {crop} ({crop_kn})</div>',
                unsafe_allow_html=True
            )

            # ✅ IMAGE
            img = get_crop_image(crop)
            st.image(img, width=400)

# ✍️ TEXT SECTION
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✍️ Text Input")

    user_text = st.text_input("Enter your condition")

    if user_text:
        # ✅ UPDATED
        crop, crop_kn, soil, rainfall, temperature = predict_crop(user_text)

        st.write("### Conditions")
        st.write(f"🌱 Soil: {soil}")
        st.write(f"🌧 Rainfall: {rainfall}")
        st.write(f"🌡 Temp: {temperature}")

        # ✅ RESULT (ENGLISH + KANNADA)
        st.markdown(
            f'<div class="result">🌾 {crop} ({crop_kn})</div>',
            unsafe_allow_html=True
        )

        # ✅ IMAGE
        st.image(
            f"https://source.unsplash.com/600x300/?{crop}",
            use_container_width=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

st.progress(100, text="AI Processing Complete 🚀")