# Databricks notebook source

import pandas as pd
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("select * from titanic")
display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("died")
