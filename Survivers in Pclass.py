# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.sql("select * from TitaniC")
display(df)

# COMMAND ----------

passenger_information = df[["Name", "Age", "PassengerId"]]
display(passenger_information)

# COMMAND ----------

# MAGIC %pip install colorama pyfiglet
# MAGIC from colorama import Fore
# MAGIC import pyfiglet
# MAGIC font = pyfiglet.figlet_format("Zolbayar")
# MAGIC display(Fore.RED + font)

# COMMAND ----------

passenger_information = df[["Name", "Age", "PassengerId"]]
display(passenger_information)

# COMMAND ----------

all_passengers = df.select("PassengerId", "Name")
display(all_passengers)

# COMMAND ----------

df = spark.sql("select PassengerId, Name from Titanic where Survived = 1 AND Pclass = 1")
display(df)

# COMMAND ----------

passenger_information = df[["PassengerId", "Name"]]
display(passenger_information)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT passenger_information.PassengerId, 
# MAGIC passenger_information.Name
# MAGIC FROM Titanic passenger_information
# MAGIC JOIN Titanic ticket_information
# MAGIC ON passenger_information.PassengerId = ticket_information.PassengerId
# MAGIC   WHERE ticket_information.Survived = 1
# MAGIC   AND ticket_information.Pclass = 3

# COMMAND ----------


