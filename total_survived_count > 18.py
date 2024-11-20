# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = (
  spark.sql("select age from titanic")
    )
display(df)

# COMMAND ----------

adult_df = spark.sql("select Survived from titanic where Age > 18").groupBy('Survived').count()
display(adult_df)
