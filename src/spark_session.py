"""
Création et gestion de la session Spark
"""
from pyspark.sql import SparkSession
import sys
sys.path.append("..")
from config.settings import SPARK_CONFIG


def get_spark_session(app_name: str = None) -> SparkSession:
    """
    Crée ou récupère une session Spark configurée pour le Data Lake
    """
    builder = SparkSession.builder

    for key, value in SPARK_CONFIG.items():
        if key == "spark.app.name" and app_name:
            builder = builder.config(key, app_name)
        else:
            builder = builder.config(key, value)

    spark = builder.getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    return spark


def stop_spark_session(spark: SparkSession):
    """Arrête proprement la session Spark"""
    if spark:
        spark.stop()