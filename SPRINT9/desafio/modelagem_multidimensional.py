import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, year, month, dayofmonth, dayofweek, monotonically_increasing_id

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

PARQUET_PATH = "s3://otaviodesafio/Refined/Movies/Combined/2024/12/15/action_movies_2024-12-15.parquet/"

df = glueContext.create_dynamic_frame.from_options(
    format="parquet",
    connection_type="s3",
    connection_options={"paths": [PARQUET_PATH]}
).toDF()

dim_filme = df.select(
    col("imdb_id").alias("filme_id"),
    "original_language", "original_title", "title", "release_date", "genres", "runtime", "production_countries"
).distinct().withColumn("id", monotonically_increasing_id())

dim_artista = df.select(
    col("imdb_id").alias("artista_id"),
    "nomeartista", "profissao"
).distinct().withColumn("id", monotonically_increasing_id())

dim_tempo = df.select(
    col("release_date").alias("data_id"),
    "release_date"
).distinct() \
    .withColumn("ano", year(col("release_date"))) \
    .withColumn("mes", month(col("release_date"))) \
    .withColumn("dia", dayofmonth(col("release_date"))) \
    .withColumn("dia_semana", dayofweek(col("release_date"))) \
    .withColumn("id", monotonically_increasing_id())

dim_tipo_animacao = df.select(
    col("original_language").alias("tipo_animacao_id"),
    "original_language"
).distinct().withColumn("id", monotonically_increasing_id())

fato_popularidade = df.select(
    col("imdb_id").alias("filme_id"),
    "release_date",
    "popularity"
).withColumn("id", monotonically_increasing_id())

fato_nota_media = df.select(
    col("imdb_id").alias("filme_id"),
    "release_date",
    "vote_average"
).withColumn("id", monotonically_increasing_id())

fato_numero_votos = df.select(
    col("imdb_id").alias("filme_id"),
    "release_date",
    "vote_count"
).withColumn("id", monotonically_increasing_id())

dim_filme_dynamic_frame = DynamicFrame.fromDF(dim_filme, glueContext, "dim_filme_dynamic_frame")
dim_artista_dynamic_frame = DynamicFrame.fromDF(dim_artista, glueContext, "dim_artista_dynamic_frame")
dim_tempo_dynamic_frame = DynamicFrame.fromDF(dim_tempo, glueContext, "dim_tempo_dynamic_frame")
dim_tipo_animacao_dynamic_frame = DynamicFrame.fromDF(dim_tipo_animacao, glueContext, "dim_tipo_animacao_dynamic_frame")
fato_popularidade_dynamic_frame = DynamicFrame.fromDF(fato_popularidade, glueContext, "fato_popularidade_dynamic_frame")
fato_nota_media_dynamic_frame = DynamicFrame.fromDF(fato_nota_media, glueContext, "fato_nota_media_dynamic_frame")
fato_numero_votos_dynamic_frame = DynamicFrame.fromDF(fato_numero_votos, glueContext, "fato_numero_votos_dynamic_frame")

dim_filme_dynamic_frame.toDF().write.mode("overwrite").parquet("s3://otaviodesafio/Refined/Movies/Dimensoes/Filme/")
dim_artista_dynamic_frame.toDF().write.mode("overwrite").parquet("s3://otaviodesafio/Refined/Movies/Dimensoes/Artista/")
dim_tempo_dynamic_frame.toDF().write.mode("overwrite").parquet("s3://otaviodesafio/Refined/Movies/Dimensoes/Tempo/")
dim_tipo_animacao_dynamic_frame.toDF().write.mode("overwrite").parquet("s3://otaviodesafio/Refined/Movies/Dimensoes/TipoAnimacao/")
fato_popularidade_dynamic_frame.toDF().write.mode("overwrite").parquet("s3://otaviodesafio/Refined/Movies/Fatos/Popularidade/")
fato_nota_media_dynamic_frame.toDF().write.mode("overwrite").parquet("s3://otaviodesafio/Refined/Movies/Fatos/NotaMedia/")
fato_numero_votos_dynamic_frame.toDF().write.mode("overwrite").parquet("s3://otaviodesafio/Refined/Movies/Fatos/NumeroVotos/")
