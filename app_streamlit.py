import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# 1. Page Configuration
st.set_page_config(page_title="AI Spam Guard", page_icon="🛡️")

# 2. Load Resources (Cached so it only happens once)
@st.cache_resource
def load_assets():
    model = joblib.load('app/spam_model.pkl')
    tfidf = joblib.load('app/tfidf_vectorizer.pkl')
    nltk.download('stopwords')
    return model, tfidf

model, tfidf = load_assets()
ps = PorterStemmer()

# 3. Preprocessing Logic
def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text).lower()
    words = text.split()
    clean_words = [ps.stem(w) for w in words if w not in stopwords.words('english')]
    return " ".join(clean_words)

# 4. The UI Layout
st.title("🛡️ Email Spam Detector")
st.write("Type or paste an email below to check if it's safe or a scam.")

email_input = st.text_area("Email Content:", height=200, placeholder="Enter email text here...")

if st.button("Analyze Email"):
    if email_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        # Process and Predict
        cleaned = clean_text(email_input)
        vectorized = tfidf.transform([cleaned]).toarray()
        prediction = model.predict(vectorized)[0]
        confidence = model.predict_proba(vectorized).max()

        # Display Results
        if prediction == 1:
            st.error(f"🚨 This is likely SPAM! (Confidence: {confidence*100:.2f}%)")
        else:
            st.success(f"✅ This looks like a legitimate HAM email. (Confidence: {confidence*100:.2f}%)")

st.markdown("---")
st.caption("Built with Python, Scikit-Learn, and Streamlit")