import pandas as pd
import boto3

s3 = boto3.client('s3')

bucket = 'otaviomeubucket'

# Caminho do arquivo local
arquivo = r'C:\Users\Otavi\Downloads\alunosdados.csv'

# Carrega o arquivo CSV
try:
    df = pd.read_csv(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
    exit()

# Manipulações e filtragens dos dados
df['Valor mensal da bolsa'] = df['Valor mensal da bolsa'].replace({'R\\$': '', ',': ''}, regex=True).astype(float)
df_filtrado = df[(df['Valor mensal da bolsa'] > 500) & (df['Período de recebimento da bolsa'].str.contains('2024'))]

agg_df = df['Valor mensal da bolsa'].agg(['mean', 'sum'])

df['Tipo de Bolsa'] = df['Valor mensal da bolsa'].apply(lambda x: 'Alta Bolsa' if x > 600 else 'Baixa Bolsa')
df['Bolsa em Dólares'] = df['Valor mensal da bolsa'] / 5
df['Ano de Início'] = df['Período de recebimento da bolsa'].str.extract(r'(\d{4})').astype(int)
df['Aluno(a) bolsista'] = df['Aluno(a) bolsista'].str.upper()

# Exibi dados filtrados
print("Dados filtrados:")
print(df_filtrado)

# Exibi agregações
print("\nAgregações:")
print(agg_df)

# Exibi dados com manipulações
dados_manipulados = df[['Aluno(a) bolsista', 'Valor mensal da bolsa', 'Tipo de Bolsa', 'Bolsa em Dólares', 'Ano de Início']]
print("\nDados com manipulações:")
print(dados_manipulados.head())

# Gera um novo arquivo CSV com os dados filtrados e manipulados
output_file = r'C:\Users\Otavi\Downloads\alunos_dados_processados.csv'
dados_manipulados.to_csv(output_file, index=False)

# Faz upload do arquivo CSV para o bucket S3
try:
    s3.upload_file(output_file, bucket, 'alunos_dados_processados.csv')
    print(f"Arquivo {output_file} enviado para o bucket {bucket} com sucesso.")
except Exception as e:
    print(f"Erro ao fazer upload do arquivo: {e}")
