from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("DailySalesPipeline") \
    .getOrCreate()

input_path = "s3://sakthi-raw-sales-data/staging/overnight_sales.csv"
output_path = "s3://sakthi-processed-sales-data/presentation/"

# Batch ingestion
sales = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(input_path)

# Data transformation
sales = sales.dropna(subset=["order_id", "amount"])
sales = sales.withColumn("amount", F.col("amount").cast("double"))

summary = sales.agg(
    F.sum("amount").alias("total_sales"),
    F.avg("amount").alias("average_order_value")
)

# Analyze DAG before execution
print("Execution plan:")
summary.explain(True)

# Retrieve calculated metrics
print("Daily Sales Report:")
summary.show(truncate=False)

# Write to presentation layer
summary.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(output_path)

print("Daily sales pipeline completed!")

spark.stop()
