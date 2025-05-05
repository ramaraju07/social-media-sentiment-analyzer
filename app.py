import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define TextBlob sentiment analysis function
def analyze_sentiment_textblob(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity

# Define VADER sentiment analysis function
def analyze_sentiment_vader(text):
    score = analyzer.polarity_scores(text)
    return score

# Streamlit UI setup
st.title("💬 Social Media Sentiment Analyzer")
st.subheader("🔍 Enter a social media post or comment for AI-powered sentiment analysis")

# Text input field for user input
user_input = st.text_area("📝 Enter text here", help="Paste or type a social media post or comment for sentiment analysis.")

# Button to trigger sentiment analysis
if st.button("🚀 Analyze Sentiment"):
    if user_input.strip():
        # Analyze sentiment using TextBlob
        polarity = analyze_sentiment_textblob(user_input)
        
        # Analyze sentiment using VADER
        vader_score = analyze_sentiment_vader(user_input)

        # Display results
        st.write("### 📊 TextBlob Polarity Score:", round(polarity, 2))
        st.write("### 🧠 VADER Sentiment Scores")
        st.write(f"Positive: {vader_score['pos']:.2f}")
        st.write(f"Negative: {vader_score['neg']:.2f}")
        st.write(f"Neutral: {vader_score['neu']:.2f}")
        st.write(f"Compound: {vader_score['compound']:.2f}")

        # Display overall sentiment
        if polarity > 0:
            st.success("😊 Overall Sentiment: Positive")
        elif polarity < 0:
            st.error("☹ Overall Sentiment: Negative")
        else:
            st.info("😐 Overall Sentiment: Neutral")
    else:
        st.warning("⚠ Please enter some text before analyzing.")

