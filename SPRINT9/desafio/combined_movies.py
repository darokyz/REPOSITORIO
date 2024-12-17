import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, lit

# Filmes a serem mantidos
# Fiz uma seleção manual dos filmes que gostaria de usar e selecionei eles aqui para buscar apenas esses filmes
filmes_a_manter = [
    "Code Geass: Lelouch of the Rebellion – Glorification",
    "One Piece: Giant Mecha Soldier of Karakuri Castle",
    "Dragon Ball Z: Lord Slug",
    "Saint Seiya: Legend of Crimson Youth",
    "Saint Seiya: The Heated Battle of the Gods",
    "Trigun: Badlands Rumble",
    "Dragon Ball Z: Broly – The Legendary Super Saiyan",
    "Dragon Ball Z: Resurrection 'F'",
    "Dragon Ball Z: Battle of Gods",
    "Pokémon: Lucario and the Mystery of Mew",
    "Doraemon: Nobita and the Galaxy Super-express",
    "Inuyasha the Movie: Affections Touching Across Time",
    "Inuyasha the Movie 2: The Castle Beyond the Looking Glass",
    "One Piece: Dead End Adventure",
    "Attack on Titan",
    "Naruto Shippuden the Movie: Bonds",
    "Saint Seiya: Warriors of the Final Holy Battle",
    "One Piece: Baron Omatsuri and the Secret Island",
    "Dragon Ball Z: Wrath of the Dragon",
    "Ghost in the Shell",
    "Dragon Ball Z: Fusion Reborn",
    "Dragon Ball: Mystical Adventure",
    "One Piece: Episode of Chopper Plus: Bloom in the Winter, Miracle Cherry Blossom",
    "One Piece: Curse of the Sacred Sword",
    "Dragon Ball Z: Bio-Broly",
    "Saint Seiya: Evil Goddess Eris",
    "One Piece: Film Z",
    "Ghost in the Shell 2: Innocence",
    "Evangelion: 1.11 You Are (Not) Alone",
    "Evangelion: 2.22 You Can (Not) Advance",
    "Evangelion: 3.33 You Can (Not) Redo",
    "Akira",
    "Spirited Away",
    "Howl's Moving Castle",
    "My Neighbor Totoro",
    "Princess Mononoke"
]

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session


data_atual = datetime.now()
execution_date_str = data_atual.strftime("%Y-%m-%d")
ano = data_atual.strftime('%Y')
mes = data_atual.strftime('%m')
dia = data_atual.strftime('%d')
execution_path = f"{ano}/{mes}/{dia}"


RAW_PARQUET_PATH = f"s3://otaviodesafio/Trusted/Movies/CSV/2024/11/29/"
JSON_ACTION_MOVIES_PATH = f"s3://otaviodesafio/Trusted/TMDB/API/2024/12/14/action_movies_2024-12-14.parquet/"


raw_parquet_df = glueContext.create_dynamic_frame.from_options(
    format="parquet",
    connection_type="s3",
    connection_options={"paths": [RAW_PARQUET_PATH]}
).toDF()

json_action_movies_df = glueContext.create_dynamic_frame.from_options(
    format="parquet",
    connection_type="s3",
    connection_options={"paths": [JSON_ACTION_MOVIES_PATH]}
).toDF()


joined_df = raw_parquet_df.join(json_action_movies_df, raw_parquet_df.id == json_action_movies_df.imdb_id, "inner")


filtered_df = joined_df.filter(col("title").isin(filmes_a_manter))


final_df = filtered_df.select(
    "original_language", "original_title", "popularity", "release_date",
    "title", "vote_average", "vote_count", "imdb_id", "genres", "runtime",
    "production_countries", "titulopincipal", "genero", "notamedia", "nomeartista", "profissao"
)


final_dynamic_frame = DynamicFrame.fromDF(final_df, glueContext, "final_dynamic_frame")


REFINED_PARQUET_PATH = f"s3://otaviodesafio/Refined/Movies/Combined/{execution_path}/"
output_file_name = f"action_movies_{execution_date_str}.parquet"

final_df.write.mode("overwrite").parquet(f"{REFINED_PARQUET_PATH}{output_file_name}")

print(f"Dados salvos em: {REFINED_PARQUET_PATH}{output_file_name}")
