# scripts/scraper.py

import os
import pandas as pd
from google_play_scraper import Sort, reviews_all


def create_data_dir(path: str = "data"):
    """Create data directory if not exists."""
    os.makedirs(path, exist_ok=True)


def fetch_reviews(app_id: str, bank: str, max_reviews: int = 400) -> list:
    """Fetch reviews from Google Play Store using google-play-scraper."""
    print(f"🔍 Scraping reviews for {bank}...")
    reviews = reviews_all(
        app_id,
        sleep_milliseconds=0,
        lang='en',
        country='et',
        sort=Sort.NEWEST
    )

    return [{
        'review': r['content'],
        'rating': r['score'],
        'date': r['at'],
        'bank': bank,
        'source': 'Google Play'
    } for r in reviews[:max_reviews]]


def save_reviews_to_csv(reviews: list, filename: str = "data/raw_reviews.csv"):
    """Save reviews as a CSV file."""
    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False)
    print(f"✅ Raw reviews saved to {filename}")
