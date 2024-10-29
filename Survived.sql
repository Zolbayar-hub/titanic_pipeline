-- Databricks notebook source
-- MAGIC %python
-- MAGIC import pandas as pd
-- MAGIC from pyspark.sql import functions as F
-- MAGIC # added comment
-- MAGIC # comment for test branch 

-- COMMAND ----------

select PassengerID, Name, Sex, Survived from titanic where Survived = 1

-- COMMAND ----------

SELECT SUM(Survived) AS number_of_survivors FROM hive_metastore.default.titanic

-- COMMAND ----------

create table if not exists survivors as
select PassengerId, Name, Sex, Survived from titanic where Survived = 1
