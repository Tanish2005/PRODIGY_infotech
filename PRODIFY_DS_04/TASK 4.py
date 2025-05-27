import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob


data = pd.read_csv('social_media_posts.csv')


if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'], errors='coerce')  # coerce invalid parsing to NaT


def get_sentiment(text):
    analysis = TextBlob(str(text))
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'


data['Sentiment'] = data['text'].apply(get_sentiment)


plt.figure(figsize=(8,5))
sns.countplot(x='Sentiment', data=data, order=['Positive', 'Neutral', 'Negative'])
plt.title('Sentiment Distribution in Social Media Posts')
plt.show()


if 'date' in data.columns:
    sentiment_time = data.groupby([data['date'].dt.date, 'Sentiment']).size().unstack().fillna(0)
    sentiment_time.plot(kind='line', figsize=(12,6))
    plt.title('Sentiment Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Posts')
    plt.show()


if 'brand' in data.columns:
    plt.figure(figsize=(12,6))
    sns.countplot(x='brand', hue='Sentiment', data=data,
                  order=data['brand'].value_counts().index)
    plt.title('Sentiment by Brand')
    plt.xticks(rotation=45)
    plt.show()


print(data[['text', 'Sentiment']].head(10))
