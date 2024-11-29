import csv
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercicio Etapa 2").getOrCreate()

animais = ["leão", "tigre", "elefante", "girafa", "urso", "cavalo", "macaco", "panda", "cachorro", "gato",
           "coelho", "aguia", "jacaré", "onça", "lobo", "hipopotamo", "rato", "pantera", "galo", "cervo"]

animais_ordenados = sorted(animais)

print("Animais em ordem crescente:")
print(animais_ordenados)

df_animais = spark.createDataFrame([(animal,) for animal in animais_ordenados], ["Animal"])

caminho_csv = "/content/animais_ordenados.csv"

df_animais.write.csv(caminho_csv, header=True)

print(f"A lista de animais foi salva em {caminho_csv}")

#Animais em ordem crescente:
#['aguia', 'cachorro', 'cavalo', 'cervo', 'coelho', 'elefante', 'galo', 'gato', 'girafa', 'hipopotamo', 'jacaré', 'leão', 'lobo', 'macaco', 'onça', 'panda', 'pantera', 'rato', 'tigre', 'urso']
#A lista de animais foi salva em /content/animais_ordenados.csv