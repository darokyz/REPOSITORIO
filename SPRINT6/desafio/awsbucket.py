import os
import boto3
from datetime import datetime

# Configuração
bucket_name = 'otaviodesafio'
local_folder = '/app/data'  # Pasta local dentro do container Docker
s3_prefix = 'Raw/LocalCSV/'

# Inicializa o cliente S3
s3_client = boto3.client('s3')

# Função para enviar arquivos CSV
def upload_csv_files():
    today = datetime.now().strftime('%Y%m%d')

    try:
        if not os.path.exists(local_folder):
            print(f"Pasta local não encontrada: {local_folder}")
            return

        for filename in os.listdir(local_folder):
            if filename.endswith('.csv'):
                local_file_path = os.path.join(local_folder, filename)
                category = 'Movies' if 'movies' in filename.lower() else 'Series' if 'series' in filename.lower() else None

                if category:
                    s3_path = f"{s3_prefix}{category}/{today}/{filename}"
                    print(f"Enviando {local_file_path} para {s3_path}...")
                    s3_client.upload_file(local_file_path, bucket_name, s3_path)
                    print("Upload concluído.")
                else:
                    print(f"Arquivo ignorado: {filename} (não é um arquivo de Filmes ou Séries)")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    upload_csv_files()
