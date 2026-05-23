import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# 1. Load data once outside the function (HUGE speed boost)
nltk.download('stopwords')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    # Optional: Keep currency and exclamation marks as they are spam signals
    # Instead of removing EVERYTHING, just clean HTML or weird artifacts
    text = re.sub(r'<.*?>', ' ', text)  # Remove HTML tags if present
    
    # 2. Lowercase and keep letters AND numbers (or replace numbers with 'NUM')
    # Keeping numbers helps identify "Win $1000" vs "Win"
    text = re.sub('[^a-zA-Z0-9]', ' ', text)
    text = text.lower()
    
    words = text.split()
    
    # 3. Use the 'set' for O(1) lookup speed
    clean_words = [ps.stem(w) for w in words if w not in stop_words]
    
    return " ".join(clean_words)