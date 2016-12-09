from pyspark.sql import SQLContext
from pyspark import SparkContext

if __name__ == "__main__":
    #inp_file = "hdfs:///datasets/reddit/RS_full_corpus.bz2"  # Submission
    inp_file = "hdfs:///datasets/reddit/comments/2014"
    sc = SparkContext()
    sqlContext = SQLContext(sc)

    df = sqlContext.read.json(inp_file)
    swiss_subreddit_list = ['Switzerland', 'AskSwitzerland', 'Basel', 'Bern', 'BielBienne', 'Buenzli',
     'Frauenfeld', 'Fribourg', 'Geneva', 'Liestal', 'Luzern', 'Morcote', 'Neuchatel', 'Schaffhausen', 
     'SanktGallen', 'Schwiiz', 'Solothurn', 'Stans', 'Suisse', 'Thun', 'Ticino', 'Winterthur', 'Zermatt', 
     'Zug', 'Zurich', 'Breitling', 'CHTrees', 'FCBasel', 'MatterhornPorn', 'Migros', 'Schweiz', 'SwissArmy',
      'SwissArmyKnives', 'SwissBuyers', 'SwissGaming', 'SwissGuns', 'SwissHockey', 'SwissESports', 
      'SwissMountainDogs', 'SwissNews', 'SwissProblems', 'SwissRap', 'SwissSuperLeague', 'SwissHistory', 
      'CERN', 'EPFL', 'ETHZ', 'UZH']
    filt_df = df.filter(df['subreddit'].isin(swiss_subreddit_list))
    #output_file = 'hdfs:///user/karkala/filtered_submissions_swiss_subreddits_full_corpus'
    output_file = 'hdfs:///user/karkala/filtered_comments2014_swiss_subreddits'
    filt_df.write.format("com.databricks.spark.csv").save(output_file)
    sc.stop()