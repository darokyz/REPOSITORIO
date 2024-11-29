
df_millennials_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")


df_millennials_sql.show()

""""" +--------+
|count(1)|
+--------+
| 4538524|
+--------+"""