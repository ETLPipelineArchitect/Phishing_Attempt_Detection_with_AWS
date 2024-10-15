from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("PhishingDataAnalysis").getOrCreate()

# Load Processed Data
processed_data_path = "s3://your-bucket/phishing_data/processed/data.parquet"
phishing_df = spark.read.parquet(processed_data_path)

# Analyze Top Phishing Domains
top_domains = phishing_df.groupBy('domain').count().orderBy('count', ascending=False).limit(10)
top_domains.show()

top_domains.write.csv("s3://your-bucket/phishing_data/output/top_domains.csv", mode='overwrite')
