# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = (
    spark.sql("select PassengerId, Name, Age, Sex from titanic")
)
display(df)

# COMMAND ----------

insert_query = '''
insert into Titanic(PassengerId, Name, Age)
values(3, "Zolo", 33)
'''
display(insert_query)



# COMMAND ----------

new_column = df[["Name", "Age", "PassengerId"]]

# COMMAND ----------

insert_query = '''
insert into new_column(Name, Age, PassengerId)
values("Zolo", 33, 3)
'''
display(insert_query)

# COMMAND ----------

insert_query = '''
insert into survival_status(PassengerId, Survived, Parch, SibSp)
values(891, 1, 0, 1)
'''
