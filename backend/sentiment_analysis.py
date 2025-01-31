from backend.reddit_api import fetch_test_pennystocks_posts
from textblob import TextBlob
from ollama import chat
from ollama import ChatResponse
from collections import defaultdict

def analyze_sentiment(text:str)->int:
    polarity, subjectivity = TextBlob(text).sentiment
    
    #Very subjective brings score -> 0, very objective does not affect score
    score = polarity * (1-subjectivity)
    return score

def getTickers(text:str)->list[str]:
    try:
        response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': f'Extract all stock tickers from the following text, including those for companies whose names were mentioned without their tickers. Return only valid stock tickers as a space-separated list with no additional text: {text}',
        },
        ])
        tickers = " ".split(response['message']['content'])
        return tickers
    except Exception as e:
        return str(e)
    
def mapTickerScores(tickers: list[list[str]], scores: list[int])->None:
    tickerScores = defaultdict(lambda x: [0, 0])
    for i, tickerList in enumerate(tickers):
        for ticker in tickerList:
            tickerScores[ticker][1] += scores[i]
            tickerScores[ticker][0] += 1
    
    for ticker, scoreVals in tickerScores.items():
        numScores, totalScore = scoreVals
        # TODO: Retrieve current score from db
        curScore = None
        avgScore = (totalScore+curScore) / (numScores+1)

        # TODO: Set new score in db
        
    return

def retrieve_max_tickers()->list[str]:
    # TODO: Retreive top 20 ticker scores from db
    return []

def calculate_all_sentiment()-> None:
    posts = fetch_test_pennystocks_posts()
    tickers = []
    scores = []
    for post in posts:
        scores.append(analyze_sentiment(post))
        tickers.append(getTickers(post))
    
    mapTickerScores(tickers, scores)
    return