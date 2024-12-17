# Databricks notebook source
from pyspark.sql import functions as F


# COMMAND ----------

passengers = spark.sql("select Name, Fare as ticket_fare from Titanic where Fare > 50")
display(passengers)

# COMMAND ----------


