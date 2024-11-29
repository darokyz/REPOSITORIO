from pyspark.sql.functions import expr

df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (floor(rand() * (2010 - 1945 + 1)) + 1945).cast("int")
)

df_nomes.show(10)

""""" +-----------------+------------+---------------+-------------+
|            Nomes|Escolaridade|           País|AnoNascimento|
+-----------------+------------+---------------+-------------+
|   Yolanda Shultz|       Medio|          Chile|         1993|
|  Diane Hernandez| Fundamental|      Argentina|         1998|
|   Michael Taylor| Fundamental|        Uruguai|         1964|
|     Mark Beltran|       Medio|           Peru|         1975|
|Catherine Chatcho|    Superior|       Colômbia|         1953|
|    Judy Valencia| Fundamental|        Uruguai|         1998|
| Georgia Copeland|       Medio|      Venezuela|         2000|
|   Cheryl Baldwin|       Medio|Guiana Francesa|         1960|
|      Tina Taylor|    Superior|       Colômbia|         1978|
|     Megan Rivera|       Medio|          Chile|         1966|
+-----------------+------------+---------------+-------------+
only showing top 10 rows"""""

df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2001)