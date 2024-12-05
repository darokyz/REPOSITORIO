import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, to_date, when, array, lit

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

RAW_JSON_PATH = "s3://otaviodesafio/Raw/TMDB/JSON/action_movies_with_runtime.json"

execution_date = datetime.now()
execution_date_str = execution_date.strftime("%Y-%m-%d")
execution_path = execution_date.strftime("%Y/%m/%d")
TRUSTED_PARQUET_PATH = f"s3://otaviodesafio/Trusted/TMDB/API/{execution_path}/"
output_file_name = f"action_movies_{execution_date_str}.parquet"

datasource = glueContext.create_dynamic_frame.from_options(
    format="json",
    connection_type="s3",
    connection_options={"paths": [RAW_JSON_PATH]},
)

df = datasource.toDF()

df = df.withColumn(
    "release_date",
    when(to_date(col("release_date"), "yyyy-MM-dd").isNotNull(), to_date(col("release_date"), "yyyy-MM-dd"))
    .otherwise(lit(None))
)

df = df.withColumn("title", when(col("title").isNotNull(), col("title")).otherwise("Unknown"))
df = df.withColumn("runtime", when(col("runtime").isNotNull(), col("runtime")).otherwise(0))
df = df.withColumn("vote_count", when(col("vote_count").isNotNull(), col("vote_count")).otherwise(0))
df = df.withColumn("genres", when(col("genres").isNotNull() & (col("genres") != array()), col("genres")).otherwise(array(lit("Unknown"))))
df = df.withColumn("popularity", when(col("popularity").isNotNull(), col("popularity")).otherwise(0.0))
df = df.withColumn("overview", when(col("overview").isNotNull(), col("overview")).otherwise("No overview available"))
df = df.withColumn("original_language", when(col("original_language").isNotNull(), col("original_language")).otherwise("Unknown"))
df = df.withColumn("production_countries", when(col("production_countries").isNotNull() & (col("production_countries") != array()), col("production_countries")).otherwise(array(lit("Unknown"))))
df = df.withColumn("director", when(col("director").isNotNull(), col("director")).otherwise("Unknown"))
df = df.filter(col("release_date").isNotNull())
df = df.withColumn("execution_date", lit(execution_date_str))

transformed_dynamic_frame = DynamicFrame.fromDF(df, glueContext, "transformed_dynamic_frame")

glueContext.write_dynamic_frame.from_options(
    frame=transformed_dynamic_frame,
    connection_type="s3",
    connection_options={
        "path": TRUSTED_PARQUET_PATH,
        "partitionKeys": ["execution_date"],
    },
    format="parquet"
)

output_file_path = f"{TRUSTED_PARQUET_PATH}{output_file_name}"
df.write.mode("overwrite").parquet(output_file_path)

 # foi acrescentada algumas mudanças nesse codigo pois a execuçao do codigo antigo estava particionando o arquivo pelas datas contidas no conteudo dele "realease_date" mas esse ja esta atualizado para data de execuçao