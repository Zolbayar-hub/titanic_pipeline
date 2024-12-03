# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("select PassengerId, Name, Age, Fare, Pclass from Titanic")

# COMMAND ----------


df = df.withColumn(
    "Name",
    F>when(F.col("PassengerId") ==8, "Zolbayar").otherwise(F.col("Name"))
)
display(df)

# COMMAND ----------

df = df.withColumn(
    "Age",
    F.when(F.col("Age") ==2, 43).otherwise(F.col("Age"))
)
display(df)

# COMMAND ----------

df = df.withColumn(
    "Fare",
    F.when(F.col("PassengerId") ==4, 150 ).otherwise(F.col("Fare"))
)
display(df)

# COMMAND ----------

df = df[["PassengerId", "Name", "Fare", "Pclass"]]

# COMMAND ----------

df = df.withColumn(
  "Fare",
  F.when(F.col("PassengerId") == 4, 40).otherwise(F.col("Fare"))
).withColumn(
  "Pclass",
  F.when(F.col("PassengerId") == 4, 1).otherwise(F.col("Pclass"))
)
display(df)

# COMMAND ----------


