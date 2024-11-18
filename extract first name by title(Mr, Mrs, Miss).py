# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = (
  spark.sql("SELECT * FROM titanic")
  .fillna({"Age": 0})
  .withColumn(
    "first_name",
    F.trim(
        F.regexp_extract(F.col("Name"), r'\b(?:Mr\.|Mrs\.|Miss\.|Master\.)\s+(\w+)', 1)
    )
)
  .orderBy(F.col("Age").asc())
  )
display(df)


# COMMAND ----------


