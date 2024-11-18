# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = (
  spark.sql("SELECT * FROM titanic")
  .fillna({"Age": 0})
  .withColumn("short_name", F.substring(F.col("name"), 1, 4))
  .withColumn("first_name", F.split(F.col("name"), " ")[0]) \
  .withColumn("last_name", F.split(F.col("name"), " ")[1])

  .orderBy(F.col("Age").asc())
  )
display(df)


# COMMAND ----------

df = (
  spark.sql("SELECT * FROM titanic")
  .fillna({"Age": 0})
  .withColumn("last_name", F.split(F.col("Name"), ",")[0]) \
  .withColumn("first_name", F.split(F.split(F.col("Name"), ",")[1], " ")[2])

  .orderBy(F.col("Age").asc())
  )
display(df)
