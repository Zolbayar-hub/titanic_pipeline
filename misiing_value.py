# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

dbutils.widgets.text("column", "column")
dbutils.widgets.text("filter", "")

# COMMAND ----------

col = dbutils.widgets.get("column")
filter = dbutils.widgets.get("filter")

# COMMAND ----------

df = (
  spark.sql("SELECT * FROM titanic")
  .fillna({"Age": 0})
  .select("PassengerId", "Name", col)
  .withColumnRenamed("PassengerId", "Id")
  .withColumnRenamed("Name", "name")
  .filter(F.col(col)>float(filter))
  )
display(df)

# COMMAND ----------


