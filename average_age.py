# Databricks notebook source
from pyspark.sql import functions as F


# COMMAND ----------

df = spark.sql("SELECT * from Titanic")

# COMMAND ----------

passengers = df[["Name", "Age", "Sex"]]
display(passengers)

# COMMAND ----------

df = spark.sql("SELECT AVG(Age) AS Average_Age FROM Titanic")
df = display(df)

# COMMAND ----------

df = spark.sql("SELECT Name, Max(Age) AS Max_age from Titanic GROUP BY Name")
display(df)

# COMMAND ----------


