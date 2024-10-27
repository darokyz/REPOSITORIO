import boto3

# Cria um cliente S3
s3 = boto3.resource('s3')

# Nome do bucket
bucket = 'otaviomeubucket'

# Cri o bucket (caso não exista)
try:
    s3.create_bucket(Bucket=bucket)
    print(f'Bucket {bucket} criado com sucesso!')
except Exception as e:
    print(f'Erro ao criar o bucket: {e}')

# Caminho do arquivo local
arquivo = r'C:\Users\Otavi\Downloads\alunosdados.csv'  

# Nome do arquivo no bucket
nome_arquivo = 'alunosdados.csv'

#  upload do arquivo para o bucket
try:
    s3.Bucket(bucket).upload_file(arquivo, nome_arquivo)
    print(f'Arquivo {nome_arquivo} enviado para o bucket {bucket} com sucesso! <3')
except Exception as e:
    print(f'Erro ao enviar o arquivo: {e}')
