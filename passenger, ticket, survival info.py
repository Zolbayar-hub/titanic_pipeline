# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = (
  spark.sql("select PassengerId, Name, Sex, Age from titanic")
)
display(df)

# COMMAND ----------

passenger_info = df.select('PassengerId', 'Name', 'Sex', 'Age')
passenger_info.createOrReplaceTempView('passenger_info')
display(passenger_info)

# COMMAND ----------

ticket_info = spark.sql("select PassengerId, Ticket, Fare, Pclass from titanic")
display(ticket_info)

# COMMAND ----------

survival_status = spark.sql("select PassengerId, Survived, Parch, SibSp from titanic")
display(survival_status)

# COMMAND ----------

tables = spark.sql("SHOW TABLES")
display(tables)
