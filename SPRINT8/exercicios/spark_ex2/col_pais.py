from pyspark.sql.functions import rand, floor, lit

paises = ["Argentina", "Brasil", "Chile", "Colômbia", "Equador",
          "Paraguai", "Peru", "Uruguai", "Venezuela", "Bolívia",
          "Suriname", "Guiana", "Guiana Francesa"]

df_nomes = df_nomes.withColumn(
    "País",
    lit(paises)[floor(rand() * len(paises))]
)

df_nomes.show(10)

""""" +-----------------+------------+---------------+
|            Nomes|Escolaridade|           País|
+-----------------+------------+---------------+
|   Yolanda Shultz|       Medio|          Chile|
|  Diane Hernandez| Fundamental|      Argentina|
|   Michael Taylor| Fundamental|        Uruguai|
|     Mark Beltran|       Medio|           Peru|
|Catherine Chatcho|    Superior|       Colômbia|
|    Judy Valencia| Fundamental|        Uruguai|
| Georgia Copeland|       Medio|      Venezuela|
|   Cheryl Baldwin|       Medio|Guiana Francesa|
|      Tina Taylor|    Superior|       Colômbia|
|     Megan Rivera|       Medio|          Chile|
+-----------------+------------+---------------+
only showing top 10 rows"""""