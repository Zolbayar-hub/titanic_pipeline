# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("select Name, Age, Sex from Titanic")

# COMMAND ----------

customer_df = df[["Name", "Age", "Sex"]]
display(customer_df)

# COMMAND ----------

df = spark.sql("SELECT AVG(Age) as Ave_age FROM Titanic")
display(df)

# COMMAND ----------


