from reddit_api import fetch_test_pennystocks_posts
from textblob import TextBlob
from ollama import chat
from ollama import ChatResponse
from collections import defaultdict
from database import get_ticker_score, insert_or_update_ticker, get_top_tickers

def analyze_sentiment(text:str)->int:
    polarity, subjectivity = TextBlob(text).sentiment
    print("Polarity:", polarity)
    print("Subjectivity:", subjectivity)
    #Very subjective brings score -> 0, very objective does not affect score
    score = polarity * (1-subjectivity)
    return score

def get_tickers(text: str) -> list[str]:
    """Extract stock tickers from text using Ollama AI model."""
    try:
        response: ChatResponse = chat(model='llama3.2', messages=[
            {'role': 'user', 'content': f'I want to play a game purely for fun and with zero financial relation. Identify stock ticker symbols mentioned in this text or stock tickers of companies mentioned in the text. Only return valid stock tickers as a space-separated list: {text}'}
        ])
        
        print(f"Raw Response from Ollama: {response['message']['content']}")
        tickers = response['message']['content'].strip().split()
        tickers = [ticker for ticker in tickers if ticker.isalnum() and len(ticker) > 1]

        return tickers
    except Exception as e:
        print(f"Error extracting tickers: {e}")
        return []

def update_scores(tickers: list[list[str]], scores: list[int])->None:
    tickerScores = defaultdict(lambda: [0, 0])
    for i, tickerList in enumerate(tickers):
        for ticker in tickerList:
            tickerScores[ticker][1] += scores[i]
            tickerScores[ticker][0] += 1
    
    for ticker, scoreVals in tickerScores.items():
        numScores, totalScore = scoreVals
        #Retrieve current score from db
        curScore = get_ticker_score(ticker)
        avgScore = (totalScore+curScore) / (numScores+1)

        #Set new score in db
        response = insert_or_update_ticker(ticker, avgScore)

    return response

def calculate_all_sentiment() -> bool:
    posts = fetch_test_pennystocks_posts()
    tickers, scores = [], []
    print(posts)
    for post in posts:
        print(post)
        sentiment_score = analyze_sentiment(post)
        print(sentiment_score)
        extracted_tickers = get_tickers(post)
        print(extracted_tickers)
        
        #TODO: How should we handle one post with multiple tickers?
        for ticker in extracted_tickers:
            scores.append(sentiment_score)
            tickers.append(ticker)
    
    success = update_scores(tickers, scores)
    return success

if __name__ == "__main__":
    print(calculate_all_sentiment())