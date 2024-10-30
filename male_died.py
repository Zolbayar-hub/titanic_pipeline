# Databricks notebook source
import pandas as pd
from pyspark.sql import functions as F

# COMMAND ----------


df = spark.table("Titanic")



# COMMAND ----------

died_men = df.where(F.col('Sex')=='male').where(F.col('Survived')==0)

# COMMAND ----------

display(died_men)

# COMMAND ----------

died_men.write.mode("overwrite").saveAsTable("died_men")

# COMMAND ----------


