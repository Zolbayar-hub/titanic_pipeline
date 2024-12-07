# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

died_people = spark.sql("SELECT * From titanic  where survived ==0")
display(died_people)

# COMMAND ----------

df = spark.sql("SELECT Age FROM titanic WHERE survived == 0").groupBy("Age").count()
display(df)

# COMMAND ----------


