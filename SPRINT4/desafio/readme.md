# Desafio de Python com Containers Docker

## Objetivo
O objetivo deste desafio foi a prática de Python com containers Docker, combinando os conhecimentos adquiridos sobre criação de Dockerfiles, execução de containers e scripts Python.

1. **Criação de uma imagem Docker para rodar o script `carguru.py`.**
2. **Reutilização de containers parados.**
3. **Criação de um novo script `hash_generator.py` que recebe input e gera um hash SHA-1.**

---

## Etapa 1: Criação do Dockerfile para o `carguru.py`

### Arquivo `carguru.py`

# Usando a imagem base do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo carguru.py para o container
COPY carguru.py .

# Comando para executar o script
CMD ["python", "carguru.py"]

### Build da imagem:

docker build -t carguru-app .

### Executar o container:

docker run carguru-app

### Verificar containers: 

docker ps -a

### Reiniciar um container:

docker start <ID_DO_CONTAINER>

## Hash Generator:
#### Usando a imagem base do Python
FROM python:3.9-slim

#### Definindo o diretório de trabalho
WORKDIR /app

#### Copiando os arquivos para o container
COPY carguru.py .
COPY hash_generator.py .

#### Comando para executar o script
CMD ["python", "hash_generator.py"]

##### Comandos para Build e Execução do Hash Generator
##### Build da imagem:

docker build -t hash-app .
##### Executar o container:

docker run -it hash-app


Após a execução de ambos os scripts e a geração das imagens Docker, é possível observar a funcionalidade dos scripts em ambientes isolados, demonstrando a eficácia do uso de containers para rodar aplicações.

Este desafio proporcionou uma experiência prática significativa na integração de Python com Docker, permitindo uma melhor compreensão dos conceitos de containers e sua aplicação em projetos reais.



