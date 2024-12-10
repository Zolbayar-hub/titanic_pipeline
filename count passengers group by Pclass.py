# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT * FROM Titanic")

# COMMAND ----------

passengers = df.select('Name', 'Age', 'Sex', 'Pclass')
display(passengers)

# COMMAND ----------

df = spark.sql("SELECT Pclass, COUNT(*) AS Passengers FROM Titanic GROUP BY Pclass")
display(df)

# COMMAND ----------


