# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = (
    spark.sql("select PassengerId, Name, Age, Fare, Pclass from Titanic")
)
display(df)

# COMMAND ----------



df = df.withColumn(
    "Name",
    F.when(F.col("Age") ==22, "Zoloo").otherwise(F.col("Name"))
).withColumn(
    "Pclass",
    F.when(F.col("PassengerId") ==3, 1).otherwise(F.col("Pclass"))
).withColumn(
    "Age",
    F.when(F.col("PassengerId") ==9, 40).otherwise(F.col("Age"))
)



display(df)

# COMMAND ----------


