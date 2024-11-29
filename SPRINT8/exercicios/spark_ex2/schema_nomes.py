arquivo_nomes = "/content/nomes_aleatorios.txt"

df_nomes = spark.read.csv(arquivo_nomes, inferSchema=True, header=False)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

print("As primeiras 10 linhas do DataFrame:")
df_nomes.show(10)

print("Esquema do DataFrame:")
df_nomes.printSchema()


"""""As primeiras 10 linhas do DataFrame:
+-----------------+
|            Nomes|
+-----------------+
|   Yolanda Shultz|
|  Diane Hernandez|
|   Michael Taylor|
|     Mark Beltran|
|Catherine Chatcho|
|    Judy Valencia|
| Georgia Copeland|
|   Cheryl Baldwin|
|      Tina Taylor|
|     Megan Rivera|
+-----------------+
only showing top 10 rows"""""
