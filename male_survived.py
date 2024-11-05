# Databricks notebook source
import pandas as pd
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql('select * from Titanic')
male_survivors = df.filter(F.col('Sex') == 'male').groupBy('Survived').count()
display(male_survivors)

# COMMAND ----------

# test commit
male_survivors.write.mode('overwrite').saveAsTable("male_survivors")
