# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT * FROM Titanic")

# COMMAND ----------

df = spark.sql("SELECT Name, MAX(Age) AS MaxAge, COUNT(*) AS Count FROM Titanic GROUP BY Name")
display(df)

# COMMAND ----------

df = spark.sql("SELECT Name, Age FROM Titanic WHERE Age = (SELECT MAX(Age) FROM Titanic) OR Age = (SELECT MIN(Age) FROM Titanic)")
display(df)

# COMMAND ----------


