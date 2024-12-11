# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT Name, MIN(Fare) as MinFare FROM Titanic GROUP BY Name ORDER BY MinFare")
display(df)

# COMMAND ----------


