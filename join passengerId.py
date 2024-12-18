# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("select * from Titanic")
display(df) 

# COMMAND ----------

passenger = df.select("PassengerId", "Name", "Ticket", "Fare")
display(passenger)

# COMMAND ----------

ticket = df.select("PassengerId", "Ticket", "Fare", "Pclass")
display(ticket)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT passenger.PassengerId,
# MAGIC    passenger.Name,
# MAGIC    passenger.Ticket,
# MAGIC    passenger.Fare
# MAGIC FROM Titanic AS passenger
# MAGIC JOIN Titanic AS ticket
# MAGIC ON passenger.PassengerId = ticket.PassengerId

# COMMAND ----------


