"""
const API_KEY = '6c4ff5762de4b240174fffe805d1f2d4';
const API_BASE = 'https://api.themoviedb.org/3';
"""
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = '6c4ff5762de4b240174fffe805d1f2d4'
analyzer = SentimentIntensityAnalyzer()

def suggest_movies():
    phrase = input("Como voce estas se sentindo hoje ? ")
    emotion = analyzer.polarity_scores(phrase)['compound']

    if emotion <= -0.5:
        genre = "18" # Drama
    elif emotion < 0:
        genre = "35" # Comedia
    elif emotion < 0.5:
        genre = "10749" # Romance
    else :
        genre = "27" # horror

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genre}&vote_count.gte=4"
    response = requests.get(url).json()

    if response['results']:
        titles = [result['title'] for result in response['results'][:3]]
        print("Recomendo os seguintes filmes para voce: ")
        for title in titles:
            print(f"- {title}")
    else:
        print("Nao encontrei nenhuma sugestao de filme para voce")

def chatbot():
    print("Olá sou um chat de sugestao de filmes. Como posso te ajudar hoje ? ")

    while True:
        try:
            response = input().lower()
            if 'filme' or 'filmes' in response:
                suggest_movies()
            elif 'tchau' in response or 'adeus' in response:
                print("Adeus! te vejo por ai vacilao")
                break
            else:
                print("Escreve direito! ")
        except KeyboardInterrupt:
            break;

chatbot()