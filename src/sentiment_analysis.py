from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes sentiment of the given text and returns the mood.
    """
    analysis = TextBlob(text)
    # Simple sentiment analysis: you can use more advanced models
    if analysis.sentiment.polarity > 0:
        return 'happy'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'sad'