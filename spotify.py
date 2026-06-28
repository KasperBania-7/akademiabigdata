import io, sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("Spotify").master("local[*]").getOrCreate()

dane = spark.read.format("csv").option("header","true").option("inferSchema","true").csv("spotify_churn_dataset.csv")


analiza = (
    dane.groupBy('subscription_type')
    .agg(round(avg('skip_rate'),2).alias('Częstotliwość przeskakiwania'),
         round(avg('songs_played_per_day'),2).alias('Piosenek dziennie'),
         round(avg('listening_time'),2).alias('Czas słuchania'))
)
analiza.show()





