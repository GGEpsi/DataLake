from pyspark.sql.functions import col, upper, to_date
from spark_config import spark

RAW = "../data_lake/raw"
STAGING = "../data_lake/staging"

def transform_transactions():
    df = spark.read.option("header", True).csv(f"{RAW}/transactions")

    df_clean = (
        df.dropDuplicates()
          .withColumn("amount", col("amount").cast("double"))
          .withColumn("transaction_date", to_date(col("date"), "yyyy-MM-dd"))
          .withColumn("country", upper(col("country")))
    )

    df_clean.write.mode("overwrite").parquet(f"{STAGING}/transactions")

def transform_sales():
    df = spark.read.option("header", True).csv(f"{RAW}/sales")

    df_clean = (
        df.dropDuplicates()
          .withColumn("revenue", col("revenue").cast("double"))
          .withColumn("country", upper(col("country")))
    )

    df_clean.write.mode("overwrite").parquet(f"{STAGING}/sales")

def transform_logs():
    df = spark.read.option("header", True).csv(f"{RAW}/logs")

    df_clean = (
        df.dropDuplicates()
          .withColumn("is_success", col("status") == "SUCCESS")
    )

    df_clean.write.mode("overwrite").parquet(f"{STAGING}/logs")

if __name__ == "__main__":
    transform_transactions()
    transform_sales()
    transform_logs()
