from textblob import TextBlob

def analyze_text(text):
    if not text.strip():
        return "Please write something."

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1 (neg) to 1 (pos)

    if polarity > 0.2:
        return "You seem positive today 😊"
    elif polarity < -0.2:
        return "You might be feeling down 😟"
    else:
        return "You're feeling pretty neutral 🧐"
