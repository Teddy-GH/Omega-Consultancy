from transformers import pipeline
import pandas as pd

# Load model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def compute_sentiment(text):
    try:
        result = sentiment_pipeline(text[:512])[0]  # Limit to 512 tokens
        label = result['label'].lower()
        score = result['score']
        return label, score
    except:
        return 'neutral', 0.5  # fallback

def add_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    sentiments = df['review'].apply(lambda text: compute_sentiment(text))
    df[['sentiment_label', 'sentiment_score']] = pd.DataFrame(sentiments.tolist(), index=df.index)
    return df
