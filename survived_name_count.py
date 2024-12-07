# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT survived, count(*) as count FROM titanic GROUP BY survived")
display(df)

# COMMAND ----------

df = spark.sql("SELECT Name from Titanic where survived == 1").groupBy('Name').count()
display(df)

# COMMAND ----------


