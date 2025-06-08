import pandas as pd

def load_news_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    
    df['date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce')

    # Drop rows where date couldn't be parsed
    df = df.dropna(subset=['date'])
    
    return df



def load_news_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    # Use utc=True to handle potential mixed time zones and silence the warning
    df['date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce', utc=True)


    df = df.dropna(subset=['date'])

    return df


