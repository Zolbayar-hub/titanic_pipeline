# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT * from titanic")
display(df)

# COMMAND ----------

df = spark.sql("SELECT Embarked from Titanic where SibSp ==1").groupBy("Embarked").count()
display(df)

# COMMAND ----------

df = spark.sql("SELECT Embarked from Titanic where SibSp ==0").groupBy("Embarked").count()
display(df)

# COMMAND ----------


