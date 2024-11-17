# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df =spark.sql("select * from titanic")
cols = df.columns

# COMMAND ----------

dbutils.widgets.dropdown("column", "Age", cols)
dbutils.widgets.text("filter", "")

# COMMAND ----------

col = dbutils.widgets.get("column")
filter = dbutils.widgets.get("filter")
print(col, filter )

# COMMAND ----------

# MAGIC %sql
# MAGIC update titanic
# MAGIC set name = "Zoloo Damba"
# MAGIC WHERE PassengerId = 4

# COMMAND ----------

df = (
  spark.sql("SELECT * FROM titanic")
  .fillna({"Age": 0})
  .select("PassengerId", "Name", col)
  .withColumnRenamed("PassengerId", "PId")
  .withColumnRenamed("Name", "name")
  .orderBy(F.col("PId").asc())
  )
display(df)

# COMMAND ----------

df = (
  spark.sql("SELECT * FROM titanic")
  .fillna({"Age": 0})
  .select("PassengerId", "Name", col)
  .withColumnRenamed("PassengerId", "PId")
  .withColumnRenamed("Name", "name")
  .filter(F.col(col)>float(filter))
  )
display(df)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC
