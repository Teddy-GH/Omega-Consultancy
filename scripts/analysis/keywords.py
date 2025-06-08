import json
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(corpus: list[str], top_n: int = 10) -> list[str]:
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english', max_features=100)
    X = vectorizer.fit_transform(corpus)
    keywords = vectorizer.get_feature_names_out()
    return list(keywords[:top_n])

THEME_MAPPING = {
    'login': 'Account Access',
    'password': 'Account Access',
    'slow': 'Performance',
    'crash': 'Performance',
    'transfer': 'Transaction',
    'support': 'Customer Service',
    'good ui': 'UI/UX',
    'friendly': 'UI/UX',
}

def map_themes(keywords: list[str]) -> dict:
    theme_counts = {}
    for word in keywords:
        for key in THEME_MAPPING:
            if key in word:
                theme = THEME_MAPPING[key]
                theme_counts[theme] = theme_counts.get(theme, 0) + 1
    return theme_counts

import pandas as pd

# Load or define df_with_sentiment DataFrame here
# Example: df_with_sentiment = pd.read_csv('path_to_sentiment_file.csv')
# Make sure it has columns 'bank' and 'cleaned_review'
df_with_sentiment = pd.DataFrame({
    'bank': ['BankA', 'BankA', 'BankB', 'BankB'],
    'cleaned_review': [
        'login was slow and support was helpful',
        'good ui and friendly staff',
        'password reset crash',
        'transfer was fast but support slow'
    ]
})

themes_per_bank = {}

for bank in df_with_sentiment['bank'].unique():
    reviews = df_with_sentiment[df_with_sentiment['bank'] == bank]['cleaned_review'].tolist()
    keywords = extract_keywords(reviews, top_n=30)
    themes = map_themes(keywords)
    themes_per_bank[bank] = themes

# Print sample
import pprint
pprint.pprint(themes_per_bank)



with open("data/analysis/themes_per_bank.json", "w") as f:
    json.dump(themes_per_bank, f, indent=2)

