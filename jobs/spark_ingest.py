from spark_config import spark

RAW_PATH = "../data_lake/raw"

def ingest_transactions():
    df = spark.read.option("header", True).csv(f"{RAW_PATH}/transactions")
    df.printSchema()
    print("Transactions:", df.count())

def ingest_sales():
    df = spark.read.option("header", True).csv(f"{RAW_PATH}/sales")
    df.printSchema()
    print("Sales:", df.count())

def ingest_logs():
    df = spark.read.option("header", True).csv(f"{RAW_PATH}/logs")
    df.printSchema()
    print("Logs:", df.count())

if __name__ == "__main__":
    ingest_transactions()
    ingest_sales()
    ingest_logs()
