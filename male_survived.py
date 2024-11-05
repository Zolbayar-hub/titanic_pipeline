# Databricks notebook source
import pandas as pd
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql('select * from Titanic')
display(df)

# COMMAND ----------

df = spark.sql('select * from Titanic')
male_survivors = df.filter(F.col('Sex') == 'male').where((F.col('PassengerId')==1) | (F.col('PassengerId')==5))
display(male_survivors)

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history "dbfs:/mnt/datastoragezoloo/titanic/male_survivors"

# COMMAND ----------

newDF.write.mode("overwrite").save("dbfs:/mnt/datastoragezoloo/titanic/male_survivors")
