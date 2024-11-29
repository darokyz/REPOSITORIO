from pyspark.sql import SparkSession

# Criand sessão do Spark
spark = SparkSession.builder \
    .appName("Exercicio Spark") \
    .getOrCreate()
