# Databricks notebook source
import pandas as pd
from pyspark.sql import functions as F


# COMMAND ----------

df = spark.sql('select * from Titanic')
female_survivors = df.filter(F.col('Sex') == 'female').groupBy('Survived').count()
display(female_survivors)

# COMMAND ----------

female_survivors.write.mode("overwrite").saveAsTable("female_survivors")

# COMMAND ----------


