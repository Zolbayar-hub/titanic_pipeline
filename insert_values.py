# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = (
    spark.sql("select PassengerId, Name, Age from Titanic")
)
display(df)

# COMMAND ----------

from pyspark.sql.functions import col, when

df = df.withColumn(
    "Age",
    when(col("Age") ==38, 40). otherwise(col("Age"))
)
display(df)

# COMMAND ----------



insert_query = '''
INSERT INTO passenger_info (PassengerId, Name, Sex, Age)
VALUES (3, 'Sara Lucas', 'female', 45.5)
'''
display(insert_query)

# COMMAND ----------

person_detail = df[['Name', 'Age']]
display(person_detail)

# COMMAND ----------

insert_query = '''
insert into person_detail(Name, Age)
values('Zolo', 33)
'''
display(insert_query)

# COMMAND ----------

person_detail.createOrReplaceTempView("person_detail")
df = (
    spark.sql("SELECT Name FROM person_detail ORDER BY Age LIMIT 15")
)
display(df)

# COMMAND ----------

insert_query = '''
insert into Titanic(Name, Age)
values('Zolo', 33)
'''
display(insert_query)

# COMMAND ----------


