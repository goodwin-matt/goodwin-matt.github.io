---
layout: page
permalink: /spark_commands/
---

<center> <h4> Common Spark Commands</h4> </center>


Important imports:
```python
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Window
spark = SparkSession.builder.enableHiveSupport().getOrCreate()
```


| Command      | Description |
| ----------- | ----------- |
| df.count() | Return number of rows in data frame|
| df.show(n=10)| Show top 10 rows|
| df.select(['col1','col2'])| Select col1 and col2|
| df.distinct() | Get distinct rows|
| df.dtypes()| Show column types|
| df.groupby('col1').agg(sum('col2').alias('col1_sum')| Group by col1 and sum col2|
| df.filter(col('col1')=='value')| This is how to do a where clause on the dataframe|
| df.cache()| Put dataframe into memory|
| df.persist()| Write to disk|
| df.unpersist() | Delete from disk|
| spark.read.parquet()| Read parquet file|
| spark.read.table()| Read hive table|
| spark.createDataFrame([(row1),(row2)], [colNames])| Create a dataframe from scratch|
| df.write.mode("overwrite").saveAsTable('table name')| Save to table|



