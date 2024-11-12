# Databricks notebook source
import pandas as pd
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("select * from titanic limit 100")
display(df)

# COMMAND ----------

df = df.withColumn(
    'AgeGroup',
    F.when(df['Age'] <= 12, 'Child')
    .when((df['Age'] > 12) & (df['Age'] <= 18), 'Teenager')
    .when((df['Age'] > 18) & (df['Age'] <= 35), 'Adult')
    .when((df['Age'] > 35) & (df['Age'] <= 60), 'Middle-aged')
    .otherwise('Senior')
)

display(df)

# COMMAND ----------

remove_duplicates = df.drop_duplicates
display(remove_duplicates)

# COMMAND ----------

import pyspark.sql.functions as F
median_age = df.approxQuantile("Age", [0.5], 0.0)[0]
df = df.fillna({'Age': median_age})

# COMMAND ----------


