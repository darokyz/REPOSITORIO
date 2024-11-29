import random
import names
import os

random.seed(40)

qtd_nomes_unicos = 3600
qtd_nomes_aleatorios = 19960000

nomes_unicos = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print("Gerando 19.960.000 nomes aleatórios...")
nomes_aleatorios = [random.choice(nomes_unicos) for _ in range(qtd_nomes_aleatorios)]

nome_arquivo = "/content/nomes_aleatorios.txt"
print(f"Salvando nomes no arquivo {nome_arquivo}...")

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    for nome in nomes_aleatorios:
        arquivo.write(nome + "\n")

print("Exibindo as primeiras 10 linhas do arquivo gerado:")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for _ in range(10):
        print(arquivo.readline().strip())

print(f"Arquivo gerado com sucesso: {nome_arquivo}")

"""Gerando 19.960.000 nomes aleatórios...
Salvando nomes no arquivo /content/nomes_aleatorios.txt...
Exibindo as primeiras 10 linhas do arquivo gerado:
Yolanda Shultz
Diane Hernandez
Michael Taylor
Mark Beltran
Catherine Chatcho
Judy Valencia
Georgia Copeland
Cheryl Baldwin
Tina Taylor
Megan Rivera
Arquivo gerado com sucesso: /content/nomes_aleatorios.txt"""