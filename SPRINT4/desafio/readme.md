# 🌟 Desafio de Python com Containers Docker

## 🎯 Objetivo
O objetivo deste desafio é praticar Python utilizando containers Docker, combinando conhecimentos sobre criação de Dockerfiles, execução de containers e scripts Python.

📦 Criação de uma imagem Docker para o script carguru.py.
♻️ Reutilização de containers parados.
🔐 Desenvolvimento do script hash_generator.py que gera um hash SHA-1 a partir de um input.

## 🛠️ Etapa 1: Criação do Dockerfile para carguru.py
📄 Arquivo carguru.py


### Usando a imagem base do Python
FROM python:3.9-slim

### Definindo o diretório de trabalho
WORKDIR /app

### Copiando o arquivo carguru.py para o container
COPY carguru.py .

### Comando para executar o script
CMD ["python", "carguru.py"]
🚀 Build da imagem:

docker build -t carguru-app .
▶️ Executar o container:

docker run carguru-app
🔍 Verificar containers:

docker ps -a
🔄 Reiniciar um container:

docker start <ID_DO_CONTAINER>

🔑 Hash Generator
📄 Dockerfile para o Hash Generator

### Usando a imagem base do Python
FROM python:3.9-slim

### Definindo o diretório de trabalho
WORKDIR /app

### Copiando os arquivos para o container
COPY carguru.py .
COPY hash_generator.py .

### Comando para executar o script
CMD ["python", "hash_generator.py"]
🚀 Comandos para Build e Execução do Hash Generator
##### Build da imagem:

docker build -t hash-app .
##### Executar o container:

docker run -it hash-app

Após a execução de ambos os scripts e a criação das imagens Docker, é possível observar a funcionalidade dos scripts em ambientes isolados, demonstrando a eficácia do uso de containers para rodar aplicações.

Este desafio proporcionou uma experiência prática significativa na integração de Python com Docker, permitindo uma melhor compreensão dos conceitos de containers e sua aplicação em projetos reais. 🚀✨