	from pyspark.sql import SparkSession
	from pyspark.ml.feature import Bucketizer
	import numpy as np
	import pandas as pd

	shuffle_parts = 400

	sess = (SparkSession
		    .builder
		    .master('yarn')
		    .enableHiveSupport()
		    .config("spark.sql.shuffle.partitions", str(shuffle_parts))
		    .config("spark.sql.hive.convertMetastoreParquet", "false")
		    .config("spark.submit.deployMode", "client")
		    )
	spark = sess.getOrCreate()

	# arguments
	name_of_table = ‘’
	column_to_bin = ''
	num_bins = 1000
	user_max = None
	user_min = None
	out_path = ‘’

	# read in dataframe
	df = spark.sql('select {0} from {1}'.format(column_to_bin, name_of_table))

	# get max
	if user_max is None:
	  user_max = df.agg({column_to_bin: "max"}).collect()[0]['max({0})'.format(column_to_bin)]

	# get min
	if user_min is None:
	  user_min = df.agg({column_to_bin: "min"}).collect()[0]['min({0})'.format(column_to_bin)]

	# get buckets
	splits = np.linspace(user_min-1,user_max+1,num_bins)
	bucketizer = Bucketizer(splits=splits.tolist(),inputCol=column_to_bin, outputCol="buckets")
	df_buck = bucketizer.setHandleInvalid("keep").transform(df)


	# group by on buckets
	df_buck = df_buck.groupby('buckets').count()
	df_buck = df_buck.toPandas()

	df_agg = pd.DataFrame(range(len(splits) - 1))
	df_agg.columns = ['buckets']
	df_agg['splits'] = splits[1:]

	df_agg = df_agg.merge(df_buck, on='buckets', how='left')
	df_agg = df_agg.fillna({'count':0})


	df_agg = spark.createDataFrame(df_agg)
	df_agg.coalesce(1).write.mode("overwrite").option("header", "true").csv(out_path)

