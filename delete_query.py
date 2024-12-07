# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT * FROM titanic limit 10")
display(df)

# COMMAND ----------

df = df.withColumn(
    "Fare",
    F.when(F.col("Survived") <= 1, 0).otherwise(F.col("Fare"))
)

display(df)

# COMMAND ----------



# COMMAND ----------

passenger_information = df[['PassengerId', 'Name', 'Sex', 'Age']]
display(passenger_information)

# COMMAND ----------

delete_query = '''
delete from Passenger_information
where Age is null
'''
display(delete_query)

# COMMAND ----------


