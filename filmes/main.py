"""
const API_KEY = '6c4ff5762de4b240174fffe805d1f2d4';
const API_BASE = 'https://api.themoviedb.org/3';
"""
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = '6c4ff5762de4b240174fffe805d1f2d4'
analyzer = SentimentIntensityAnalyzer()

def suggest_movies(i):
    phrase = i
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

        # pegando os titles dos filmes
        titles = [result['title'] for result in response['results'][:3]]

        # pegando as datas dos filmes
        release_date = [result['release_date'] for result in response['results'][:3]]

        # pegando os votos dos filmes
        vote_average = [result['vote_average'] for result in response['results'][:3]]

        # pegando os posters dos filmes
        # definindo a tring do prefixo

        prefix = "https://www.themoviedb.org/t/p/w220_and_h330_face/"

        # concatenar o prefixo com o caminho da imagem do link
        poster_path = [prefix + result['poster_path'].lstrip('/') for result in response['results'][:3]]

        #retornando os resultados como uma lista
        return [titles, poster_path, release_date, vote_average]
