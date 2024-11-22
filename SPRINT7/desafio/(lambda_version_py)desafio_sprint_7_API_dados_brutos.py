import json
import boto3

s3_client = boto3.client('s3')
bucket_name = 'otaviodesafio'
file_key = 'action_movies_with_runtime.json'


# Func pra carregar os dados do arquivo JSON do S3
def carregar_dados_json(bucket, key):
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        dados = response['Body'].read().decode('utf-8')
        return json.loads(dados)
    except Exception as e:
        print(f"Erro ao carregar o arquivo JSON do S3: {e}")
        return []

# func para dividir em arquivos de 100 registros
def dividir_em_arquivos_json(dados, prefixo_nome_arquivo):
    total_registros = len(dados)
    num_arquivos = (total_registros // 100) + (1 if total_registros % 100 != 0 else 0)
    arquivos = []

    print(f"Dividindo os dados em {num_arquivos} arquivos... Total de filmes: {total_registros}")

    for i in range(num_arquivos):
        dados_divididos = dados[i * 100 : (i + 1) * 100]
        nome_arquivo = f"{prefixo_nome_arquivo}_{i+1}.json"
        
        print(f"Preparando para enviar o arquivo {nome_arquivo} contendo {len(dados_divididos)} registros.")

        try:
            # Envia os arquivos  para o S3
            s3_client.put_object(
                Bucket=bucket_name,
                Key=f'Raw/TMDB/JSON/{nome_arquivo}',
                Body=json.dumps(dados_divididos, ensure_ascii=False, indent=4).encode('utf-8')
            )
            arquivos.append(nome_arquivo)
            print(f"Arquivo {nome_arquivo} enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar o arquivo {nome_arquivo}: {e}")
    
    return arquivos

# função Lambda Handler (importante para o funcionamento no lambda)
def lambda_handler(event, context):

    # carrega dados do arquivo JSON do S3
    dados_filmes = carregar_dados_json(bucket_name, file_key)

    if dados_filmes:
        print(f"Total de filmes carregados: {len(dados_filmes)}")

        # chama a função para dividir os dados
        arquivos_divididos = dividir_em_arquivos_json(dados_filmes, 'action_movies_with_runtime')

        print(f"Arquivos divididos e enviados para o S3: {arquivos_divididos}")
    else:
        print("Nenhum dado foi carregado.")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído com sucesso!')
    }
