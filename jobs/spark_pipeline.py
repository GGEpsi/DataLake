import spark_ingest
import spark_transform
import spark_curate

if __name__ == "__main__":
    spark_ingest.main()
    spark_transform.main()
    spark_curate.main()