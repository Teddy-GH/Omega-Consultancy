import pandas as pd
from pathlib import Path

def load_raw_reviews(csv_path='../data/raw_reviews.csv') -> pd.DataFrame:
    return pd.read_csv(csv_path)

def preprocess_reviews(df: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicates and nulls
    df = df.drop_duplicates()
    df = df.dropna(subset=['review', 'rating', 'date'])

    # Normalize dates
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

    return df

def save_clean_reviews(df: pd.DataFrame, output_path='../data/clean_reviews.csv'):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
