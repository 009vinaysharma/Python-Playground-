from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer=SentimentIntensityAnalyzer()
def analyze(text):
    try:
        sentiment=analyzer.polarity_scores(text)
        if sentiment['Compound']>=0.5:
            print("Positive")
        elif sentiment['compound']<=-0.5:
            print("Negative")
        else:
            print("Neutral")
    except Exception as e:
        print(e)
text=input("please enter a text:")
analyze(text)