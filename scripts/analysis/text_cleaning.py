import re
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    text = text.lower().strip()
    return text

def preprocess_text(df: pd.DataFrame) -> pd.DataFrame:
    df['cleaned_review'] = df['review'].apply(clean_text)
    return df
