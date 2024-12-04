import requests
import pandas as pd

api_key = "68d09bec79b0663ed164081763de0b00"

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    filmes = []
    for movie in data['results']:
        filmes.append({
            'Título': movie['title'],
            'Data de Lançamento': movie['release_date'],
            'Visão Geral': movie['overview'],
            'Número de Votos': movie['vote_count'],
            'Média de Votos': movie['vote_average']
        })
    df = pd.DataFrame(filmes)
    print(df)
else:
    print("Erro na requisição:", response.status_code)
