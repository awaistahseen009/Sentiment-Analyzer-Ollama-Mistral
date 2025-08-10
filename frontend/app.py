import streamlit as st
import requests

st.set_page_config(page_title="Sentiment Analyzer (Mistral)", page_icon="💬")
st.title("Sentiment Analyzer (Mistral)")
st.markdown("Enter a sentence and let the AI detect its sentiment!")

text_input = st.text_area("Enter your sentence here:", height=100)

sentiment_emoji = {
    "Positive": "😊",
    "Negative": "😞",
    "Neutral": "😐",
    "Error": "❌"
}

if st.button("Analyze", use_container_width=True):
    if text_input.strip():
        with st.spinner("Analyzing sentiment..."):
            try:
                res = requests.post(
                    "http://localhost:8000/analyze/",
                    data={"text": text_input}
                )
                sentiment = res.json().get("sentiment", "Error")
            except Exception as e:
                sentiment = "Error"
                st.error(f"Error: {e}")
            emoji = sentiment_emoji.get(sentiment, "❓")
            st.markdown(f"## Predicted Sentiment: {emoji} **{sentiment}**")
            if sentiment == "Positive":
                st.balloons()
            elif sentiment == "Negative":
                st.snow()
    else:
        st.warning("Please enter some text to analyze.") 