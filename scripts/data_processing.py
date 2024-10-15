import re
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, col, udf, lower
from pyspark.sql.types import IntegerType, DoubleType

# Initialize Spark Session
spark = SparkSession.builder.appName("PhishingDataAnalysis").getOrCreate()

# Read Data from S3
target_s3_bucket = "s3://your-bucket/phishing_data/raw/*.csv"
phishing_df = spark.read.csv(target_s3_bucket, header=True, inferSchema=True)

# Data Cleaning and Transformation
phishing_df = phishing_df.dropna(how='any')

# Extract protocol
phishing_df = phishing_df.withColumn('protocol', regexp_extract('url', r'^(https?://)', 1))

# Save Processed Data
processed_data_path = "s3://your-bucket/phishing_data/processed/data.parquet"
phishing_df.write.parquet(processed_data_path, mode='overwrite')
