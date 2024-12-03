import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import col, when, split
from pyspark.sql.types import DoubleType, IntegerType, StringType

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

RAW_PATH = "s3://otaviodesafio/Raw/LocalCSV/Movies/20241031/movies.csv"
TRUSTED_PATH = "s3://otaviodesafio/Trusted/Movies/CSV/"

try:
    datasource = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths": [RAW_PATH]},
        format="csv",
        format_options={"withHeader": True, "separator": "|"}
    )

    if datasource.count() == 0:
        raise ValueError(f"O caminho especificado {RAW_PATH} está vazio ou não existe.")

    df = datasource.toDF()

    df = (
        df.withColumn("id", col("id").cast(StringType()))
          .withColumn("tituloPincipal", col("tituloPincipal").cast(StringType()))
          .withColumn("tituloOriginal", col("tituloOriginal").cast(StringType()))
          .withColumn("anoLancamento", col("anoLancamento").cast(IntegerType()))
          .withColumn("tempoMinutos", col("tempoMinutos").cast(IntegerType()))
          .withColumn("genero", split(col("genero"), ","))
          .withColumn("notaMedia", col("notaMedia").cast(DoubleType()))
          .withColumn("numeroVotos", col("numeroVotos").cast(IntegerType()))
          .withColumn("generoArtista", col("generoArtista").cast(StringType()))
          .withColumn("personagem", col("personagem").cast(StringType()))
          .withColumn("nomeArtista", col("nomeArtista").cast(StringType()))
          .withColumn("anoNascimento", col("anoNascimento").cast(IntegerType()))
          .withColumn("anoFalecimento", col("anoFalecimento").cast(IntegerType()))
          .withColumn("profissao", when(col("profissao").isNull(), "Desconhecida").otherwise(col("profissao")))
          .withColumn("titulosMaisConhecidos", when(col("titulosMaisConhecidos").isNull(), "Nenhum").otherwise(col("titulosMaisConhecidos")))
    )

    df_cleaned = df.dropDuplicates().na.drop()

    if df_cleaned.rdd.isEmpty():
        raise ValueError("O DataFrame limpo está vazio após a limpeza.")

    current_date = datetime.now()
    year = current_date.year
    month = str(current_date.month).zfill(2)
    day = str(current_date.day).zfill(2)

    output_path = f"s3://otaviodesafio/Trusted/Movies/CSV/{year}/{month}/{day}/"

    df_cleaned.write.mode("overwrite").parquet(output_path)

    print(f"Dados tratados foram salvos em: {output_path}")

except Exception as e:
    print(f"Erro durante a execução do Glue Job: {str(e)}")
