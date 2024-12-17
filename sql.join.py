# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("select * from Titanic")

# COMMAND ----------

passenger_information = df[["PassengerId", "Name", "Sex", "Age"]]
display(passenger_information)

# COMMAND ----------

ticket_information = df[["PassengerId", "Ticket", "Fare", "Pclass"]]
display(ticket_information)

# COMMAND ----------

passenger_information.createOrReplaceTempView("passenger_information")
ticket_information.createOrReplaceTempView("ticket_information")

df = spark.sql("SELECT passenger_information.PassengerId, Name, Ticket, Fare FROM passenger_information JOIN ticket_information ON passenger_information.PassengerId = ticket_information.PassengerId")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT 
# MAGIC     passenger_information.PassengerId,
# MAGIC     Name,
# MAGIC     Ticket,
# MAGIC     Fare
# MAGIC FROM 
# MAGIC     passenger_information
# MAGIC JOIN 
# MAGIC     ticket_information
# MAGIC ON 
# MAGIC     passenger_information.PassengerId = ticket_information.PassengerId;

# COMMAND ----------

display(_sqldf)
