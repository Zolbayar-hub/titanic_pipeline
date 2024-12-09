# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT name, age, sex from Titanic")
display(df)

# COMMAND ----------

df = spark.sql("SELECT age FROM Titanic WHERE sex = 'female' AND age >= 20").groupBy("age").count()
display(df)

# COMMAND ----------

df = spark.sql("SELECT Name from Titanic where Age<=20 AND sex = 'male'").groupBy("Name").count()
display(df)

# COMMAND ----------

df = df.fillna(0)
display(df)

# COMMAND ----------

df = spark.sql("SELECT Name from Titanic where Age IS NULL").groupBy("Name").count()
display(df)

# COMMAND ----------

df = spark.sql("SELECT Age from Titanic where Age IS NULL").groupBy("Age").count()
display(df)
