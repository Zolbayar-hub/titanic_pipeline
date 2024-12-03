# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = (
  spark.sql("select PassengerId, Name, Age, Sex from titanic")
)
display(df)

# COMMAND ----------

passenger_info = df.select('PassengerId', 'Name', 'Sex', 'Age')
display(passenger_info)

# COMMAND ----------

from pyspark.sql.functions import col, when

df = df.withColumn(
  "Age",
  when(col("PassengerId") == 5, 40).otherwise(col("Age"))
)
display(df)

# COMMAND ----------

from pyspark.sql. functions import col, when

df = df.withColumn(
  "Sex",
  when(col("PassengerId") ==7, "female").otherwise(col("Sex"))
)
display(df)

# COMMAND ----------

from pyspark.sql.functions import col, when

df = df.withColumn(
  "Name",
  when(col("PassengerId") == 1, "Byamba Enkhbat").otherwise(col("Name"))
)
display(df)

# COMMAND ----------

df = df[["PassengerId", "Name", "Fare", "Pclass"]]

# COMMAND ----------

from pyspark.sql.functions import col, when

df = df.withColumn(
  "Fare",
  when(col("PassengerId") == 4, 40).otherwise(col("Fare"))
).withColumn(
  "Pclass",
  when(col("PassengerId") == 4, 1).otherwise(col("Pclass"))
)
display(df)
