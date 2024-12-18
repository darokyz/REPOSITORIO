import json
import requests
import boto3
from datetime import datetime

TMDB_API_KEY = "68d09bec79b0663ed164081763de0b00"
s3_client = boto3.client('s3')
bucket_name = 'otaviodesafio'
output_prefix = 'Raw/TMDB/JSON/'

def obter_dados_tmdb(filme_id):
    if not filme_id:
        return {}
    
    try:
        url_tmdb = f"https://api.themoviedb.org/3/movie/{filme_id}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url_tmdb)
        if response.status_code == 200:
            dados_tmdb = response.json()
            return {
                "id": dados_tmdb.get("id"),
                "imdb_id": dados_tmdb.get("imdb_id"),
                "revenue": dados_tmdb.get("revenue"),
                "budget": dados_tmdb.get("budget"),
                "title": dados_tmdb.get("title"),
                "runtime": dados_tmdb.get("runtime"),
                "vote_count": dados_tmdb.get("vote_count"),
                "release_date": dados_tmdb.get("release_date"),
                "genres": [genre['name'] for genre in dados_tmdb.get('genres', [])],
                "popularity": dados_tmdb.get("popularity"),
                "overview": dados_tmdb.get("overview"),
                "original_language": dados_tmdb.get("original_language"),
                "production_countries": [country['name'] for country in dados_tmdb.get('production_countries', [])],
                "director": next((member['name'] for member in dados_tmdb.get('credits', {}).get('crew', []) if member['job'] == 'Director'), None),
            }
        else:
            return {}
    except Exception as e:
        return {}

def buscar_filmes_acao(ano_inicio, ano_fim):
    filmes_acao = []
    pagina = 1
    total_filmes = 0
    
    while total_filmes < 2000:
        url_busca = (
            f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&language=en-US"
            f"&sort_by=popularity.desc&primary_release_date.gte={ano_inicio}-01-01"
            f"&primary_release_date.lte={ano_fim}-12-31&with_genres=28&page={pagina}"
        )
        response = requests.get(url_busca)
        if response.status_code == 200:
            dados_busca = response.json()
            filmes = dados_busca.get("results", [])
            filmes_acao.extend(filmes)
            total_filmes += len(filmes)
            pagina += 1
            if len(filmes) == 0 or total_filmes >= 2000:
                break
        else:
            break

    return filmes_acao[:2000]

def combinar_dados_tmdb(dados_filmes):
    filmes_com_dados_tmdb = []
    for i, filme in enumerate(dados_filmes):
        filme_id = filme.get("id")
        if filme_id:
            tmdb_dados = obter_dados_tmdb(filme_id)
            filme_atualizado = {**filme, **tmdb_dados}
            filmes_com_dados_tmdb.append(filme_atualizado)
            if (i + 1) % 50 == 0:
                pass
        else:
            pass
    return filmes_com_dados_tmdb

def dividir_e_salvar_no_s3(dados, prefixo_nome_arquivo):
    total_registros = len(dados)
    num_arquivos = (total_registros // 100) + (1 if total_registros % 100 != 0 else 0)
    arquivos = []

    data_atual = datetime.now()
    ano = data_atual.strftime('%Y')
    mes = data_atual.strftime('%m')
    dia = data_atual.strftime('%d')
    output_path = f"{output_prefix}{ano}/{mes}/{dia}/"
    
    for i in range(num_arquivos):
        dados_divididos = dados[i * 100 : (i + 1) * 100]
        nome_arquivo = f"{prefixo_nome_arquivo}_{ano}-{mes}-{dia}_{i+1}.json"
        
        try:
            s3_client.put_object(
                Bucket=bucket_name,
                Key=f"{output_path}{nome_arquivo}",
                Body=json.dumps(dados_divididos, ensure_ascii=False, indent=4).encode('utf-8')
            )
            arquivos.append(nome_arquivo)
        except Exception as e:
            pass
    
    return arquivos

def lambda_handler(event, context):
    dados_filmes = buscar_filmes_acao(1970, 2020)

    if dados_filmes:
        dados_com_tmdb = combinar_dados_tmdb(dados_filmes)

        arquivos_divididos = dividir_e_salvar_no_s3(dados_com_tmdb, 'action_movies_with_tmdb')

    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído com sucesso!')
    }
