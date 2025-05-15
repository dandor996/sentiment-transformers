import pandas as pd
import re

def load_sentiment140(path: str):
    """
    Load the Sentiment140 CSVfile.
    Columns: target, id, date, flag, user, text
    Target: 0 = negative, 2 = neutral, 4 = positive
    """
    df = pd.read_csv()

def clean_text(text):
    # Basic cleaning: remove URLs, mentions, special characters
    text = re.sub(r"http\\S+|www\\S+","", text)
    text = re.sub(r"@[A-Za-z0-9]+", "", text)
    text = re.sub(r"[^a-zA-Z\\s]", "", text)
    text = text.lower().strip()
    
def preprocess_df(df: pd.DataFrame):
    df['text'] = df['text'].apply(clean_text)
    return df