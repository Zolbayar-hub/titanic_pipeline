# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("SELECT * from Titanic")
display(df)

# COMMAND ----------

spark.sql("SELECT * FROM Titanic LIMIT 5").show()


# COMMAND ----------

df = spark.sql("SELECT Name, Sex, Age from Titanic where sex = 'Female' ORDER BY Age DESC LIMIT 5")
display(df)

# COMMAND ----------

df = spark.sql('SELECT Name AS Full_name, Sex AS Gender, Age AS Age FROM Titanic WHERE Sex="Female" ORDER BY Age DESC LIMIT 5')
display(df)

# COMMAND ----------


