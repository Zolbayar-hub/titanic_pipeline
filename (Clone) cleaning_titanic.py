# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

df = spark.read.format("delta").load("dbfs:/user/hive/warehouse/titanic")
display(df)


# COMMAND ----------

null_cabin = df.filter(F.col('Cabin').isNull()).count()
display(null_cabin)

# COMMAND ----------

null_cabin_men = df.where(F.col('Sex')=='male').where(F.col('Cabin').isNull()).count()
display(null_cabin_men)

# COMMAND ----------

null_cabin_female = df.where(F.col('Sex')=='female').where(F.col('Cabin').isNull()).count()
display(null_cabin_female)

# COMMAND ----------

null_cabin_men = df.where(F.col('Sex')=='male').where(F.col('Cabin').isNull()).count()
display(null_cabin_men)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     Sex,
# MAGIC     COUNT(*) AS Total_Passengers,
# MAGIC     SUM(Survived) AS Survivors,
# MAGIC     ROUND((SUM(Survived) / COUNT(*)) * 100, 2) AS Survival_Rate_Percentage
# MAGIC FROM 
# MAGIC     titanic
# MAGIC WHERE 
# MAGIC     Age > 20
# MAGIC GROUP BY 
# MAGIC     Sex
# MAGIC ORDER BY 
# MAGIC     Survival_Rate_Percentage DESC;
# MAGIC

# COMMAND ----------

df = spark.read.format("delta").load("dbfs:/user/hive/warehouse/titanic")
display(df.select( 'Name','Sex','Age'))

