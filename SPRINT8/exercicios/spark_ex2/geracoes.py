df_nomes_renomeado = df_nomes.withColumnRenamed("País", "Pais").withColumnRenamed("Geração", "Geracao")


df_nomes_renomeado.createOrReplaceTempView("pessoas")

query = """
    SELECT
        Pais,
        CASE
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geracao X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z'
            ELSE 'Desconhecido'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao, Quantidade
"""

df_resultado = spark.sql(query)

df_resultado.show(truncate=False)

""""" +---------+------------+----------+
|Pais     |Geracao     |Quantidade|
+---------+------------+----------+
|Argentina|Baby Boomers|465998    |
|Argentina|Geracao X   |348890    |
|Argentina|Geracao Z   |372091    |
|Argentina|Millennials |350031    |
|Bolívia  |Baby Boomers|464480    |
|Bolívia  |Geracao X   |348312    |
|Bolívia  |Geracao Z   |372535    |
|Bolívia  |Millennials |348571    |
|Brasil   |Baby Boomers|464655    |
|Brasil   |Geracao X   |348655    |
|Brasil   |Geracao Z   |370877    |
|Brasil   |Millennials |349718    |
|Chile    |Baby Boomers|465203    |
|Chile    |Geracao X   |348012    |
|Chile    |Geracao Z   |371881    |
|Chile    |Millennials |349144    |
|Colômbia |Baby Boomers|464682    |
|Colômbia |Geracao X   |348050    |
|Colômbia |Geracao Z   |372482    |
|Colômbia |Millennials |349284    |
+---------+------------+----------+
only showing top 20 rows"""