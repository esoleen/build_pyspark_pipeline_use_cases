# create a streaming DataFrame
def extract_parking_data(path, spark, dataSchema, archiveDir):
    df = spark.read\
     .format("json")\
     .schema(dataSchema)\
     .option("pathGlobFilter","*.json")\
     .option("path",path)\
     .load()
    
    return df