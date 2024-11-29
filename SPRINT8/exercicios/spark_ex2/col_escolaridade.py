from pyspark.sql.functions import rand, when

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental")
    .when(rand() < 0.66, "Medio")
    .otherwise("Superior")
)

df_nomes.show(10)

""""" +-----------------+------------+
|            Nomes|Escolaridade|
+-----------------+------------+
|   Yolanda Shultz|       Medio|
|  Diane Hernandez| Fundamental|
|   Michael Taylor| Fundamental|
|     Mark Beltran|       Medio|
|Catherine Chatcho|    Superior|
|    Judy Valencia| Fundamental|
| Georgia Copeland|       Medio|
|   Cheryl Baldwin|       Medio|
|      Tina Taylor|    Superior|
|     Megan Rivera|       Medio|
+-----------------+------------+
only showing top 10 rows """""
