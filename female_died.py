# Databricks notebook source

import pandas as pd
from pyspark.sql import functions as F

# COMMAND ----------


df = spark.table("Titanic")

# COMMAND ----------

died_women = df.where(F.col('Sex')=='female').where(F.col('Survived')==0)

# COMMAND ----------

display(died_women)

# COMMAND ----------

died_women.write.mode("overwrite").saveAsTable("died_women")
