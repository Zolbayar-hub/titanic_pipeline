# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT * from Titanic")
display(df)

# COMMAND ----------

df = spark.sql("SELECT MAX(Fare) AS MAXFare from Titanic")
display(df)

# COMMAND ----------

passengers = spark.sql("SELECT Name, Age, Fare FROM Titanic")
display(passengers)

# COMMAND ----------

passengers = passengers[['Name', 'Age', 'Fare']]

# COMMAND ----------

df = spark.sql("SELECT Name, Max(Fare) AS MAXFare from Titanic GROUP BY Name ORDER BY MAXFare DESC")
display(df)

# COMMAND ----------


