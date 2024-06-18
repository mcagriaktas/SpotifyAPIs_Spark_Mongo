from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("testSpark") \
    .master("spark://172.80.0.110:7077") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .getOrCreate()

# Define schema for the DataFrame
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Create data
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show DataFrame content
df.show()

# Stop the Spark session
spark.stop()

