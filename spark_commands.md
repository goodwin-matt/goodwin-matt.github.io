---
layout: page
permalink: /spark_commands/
---

<center> <h4> Common Hive and Spark Commands</h4> </center>


| Description                                                          | Hive Command                                                                             | Spark DataFrame Command                                                                             |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Count number of rows in table                                        | select count(*) from df                                                                  | df.count()                                                                                          |
| Show top 10 rows                                                     | select * from df limit 10                                                                | df.show(n=10)                                                                                       |
| Select col1 and col2                                                 | select col1, col2, from df                                                               | df.select(['col1','col2'])                                                                          |
| Get distinct rows                                                    | select count(distinct(*)) from df                                                        | df.distinct()                                                                                       |
| Show column types                                                    | describe extended df                                                                     | df.dtypes()                                                                                         |
| Order dataframe                                                      | select * from df order by col1 desc                                                      | df.sort(col("col1").desc()))                                                                        |
| Where clause                                                         | select * from df where col1='value'                                                      | df.filter(col('col1')=='value')                                                                     |
| Group by col1 and sum col2                                           | select sum(col2) as col1_sum from df group by col1                                       | df.groupby('col1').agg(sum('col2').alias('col1_sum')                                                |
| Save to table                                                        | create table table_name as select * from df                                              | df.write.mode("overwrite").saveAsTable('table_name')                                                |
| Window function                                                      | select col1, row_number() over (partition by col1 order by col2 desc) as row_num from df | window = Window.partitionBy('col1').orderBy(col('col2').desc()) <br> df.withColumn("row_num", row_number().over(window)) |
| Case statement                                                       | select case when col1 between x and y then 'xy' else 'other' end as xy_case from df      | df.withColumn("xy_case", when((col('col1')>x) & (col('col1')<y), 'xy').otherwise('other')           |
| Replace nulls with value                                             | select coalesce(col1, cast(0 as bigint)) as col1_nonull from df                          | df.fillna({'col1':0})                                                                               |
| Inner join                                                           | select a.*, b.* from df a inner join df2 b on a.col1=b.col1                              | df.join(df2, on='col1', how='inner')                                                                |
| Left join (keep all rows of left table)                              | select a.*, b.* from df a left join df2 b on a.col1=b.col1                               | df.join(df2, on='col1', how='left')                                                                 |
| Left semi join (keel all rows of left table that are in right table) | select a.*, b.* from df a left semi join df2 b on a.col1=b.col1                          | df.join(df2, on='col1', how='left_semi')                                                            |
| Full join (keep all rows of both tables)                             | select a.*, b.* from df a full join df2 b on a.col1=b.col1                               | df.join(df2, on='col1', how='full')                                                                 |
| Union                                                                | select * from df union df2                                                               | df.union(df2).distinct()                                                                            |
| Union All                                                            | select * from df union all df2                                                           | df.union(df2)                                                                                       |
| Select rows based off pattern                                        | select * from df where col1 like pattern                                                 |                                                                                                     |


