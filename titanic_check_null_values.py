# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT * FROM titanic")

# COMMAND ----------

df = spark.sql(
    "SELECT * FROM titanic "
    "ORDER BY (Age <= 20) DESC, Age ASC"
)
display(df)

# COMMAND ----------

from pyspark.sql import functions as F

null_counts = df.select([F.sum(F.col(c).isNull().cast("int")).alias(c) for c in df.columns])
display(null_counts)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from titanic where Age>=20 order by age ASC

# COMMAND ----------


