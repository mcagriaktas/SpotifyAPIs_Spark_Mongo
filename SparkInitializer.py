from pyspark.sql import SparkSession

class SparkInitializer:
    @staticmethod
    def initialize_spark():
        spark = SparkSession.builder \
            .appName("APIsProject") \
            .master("spark://172.80.0.110:7077") \
            .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.0") \
            .config("spark.mongodb.read.uri", "mongodb://cagri:3541@172.80.0.10:27017/spotify.albums?authSource=admin") \
            .config("spark.mongodb.write.uri", "mongodb://cagri:3541@172.80.0.10:27017/spotify.albums?authSource=admin") \
            .getOrCreate()
        spark.sparkContext.setLogLevel("WARN")

        return spark