# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT * FROM titanic")
display(df)

# COMMAND ----------

df = df.fillna({"Age": 0})
display(df)
