# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

adult_person = [['Name', 'Age', 'Gender']]

# COMMAND ----------

df = (
    spark.sql("SELECT Name, Age, Sex FROM Titanic")
)
display(df)

# COMMAND ----------


df = df.withColumn(
    "Sex",
    F.when(F.col("Sex") == "male", "Male"). otherwise(F.col("Sex"))

)
display(df)


# COMMAND ----------

insert_query = '''
insert into Titanic(Name, Sex)
values('Zolo', 'Female')
'''

display(insert_query)


# COMMAND ----------

insert_query = '''
insert into passenger_info(Name, Sex, Age)
values('Tom Hardy', 'Male', 37)
'''

display(insert_query)

# COMMAND ----------

insert_query = '''
insert into ticket_info(Ticket, Fare, Pclass)
values('PC 17599', 75, 1)
'''
display(insert_query)

# COMMAND ----------

insert_query = '''
insert into survival_status(Survived, Parch, SibSp)
values(1, 0, 0)'''

display(insert_query)

# COMMAND ----------


