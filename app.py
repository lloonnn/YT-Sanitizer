import streamlit as st
import joblib
import time

# Page Config
st.set_page_config(
    page_title="YT-Sanitizer",
    page_icon="🛡️",
    layout="centered"
)

# Title
st.title("🛡️ YT-Sanitizer")
st.caption("Detect spam comments using machine learning")

st.divider()

# Input
comment = st.text_area(
    "Paste a YouTube comment",
    placeholder="Type or paste a comment here...",
    height=120
)

# Button
if st.button("Analyze Comment", use_container_width=True):

    if not comment.strip():
        st.warning("Please enter a comment first.")
    else:
        try:
            model = joblib.load("youtube_spam_model.pkl")

            with st.spinner("Analyzing comment..."):
                time.sleep(0.6)
                prediction = model.predict([comment])[0]
                proba = model.predict_proba([comment])[0]

            st.divider()

            if prediction == 1:
                st.error("🚨 **SPAM DETECTED**")
                st.metric("Confidence", f"{proba[1]*100:.1f}%")
            else:
                st.success("✅ **CLEAN COMMENT**")
                st.metric("Confidence", f"{proba[0]*100:.1f}%")

            st.info(
                "Detection is based on spam vocabulary, links, and bot-like patterns "
                "commonly found in YouTube comments."
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.caption("YT-Sanitizer Engine v1.0")
