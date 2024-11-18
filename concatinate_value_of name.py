# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("select * from titanic")
cols = df.columns
display(df)

# COMMAND ----------

dbutils.widgets.dropdown("columns", "Age", cols)
dbutils.widgets.text("filter", "")

# COMMAND ----------

col = dbutils.widgets.get("columns")
filter = dbutils.widgets.get("filter")
print(col, filter )

# COMMAND ----------

from pyspark.sql import functions as F

df = df.withColumn("full_name", F.col("Name"))
display(df)

# COMMAND ----------

from pyspark.sql import functions as F
df = df.withColumn("full_name", F.concat(F.col("Name"), F.lit(" "), F.col("Name")))
display(df)


# COMMAND ----------


