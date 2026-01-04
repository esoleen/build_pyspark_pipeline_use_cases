# build_pyspark_pipeline_use_cases
## Overwiew

This project demonstrates a collection of data pipeline use cases designed to showcase common patterns in data processing, transformation, and enrichment. Each use case highlights a specific scenario—such as filtering, aggregating, deduplicating, or restructuring data. Our all pipelines will be structured like below

Step 1: Data ingestion
 - Using Apache Spark (Pyspark)

Step 2: Data Processing
 - using Windowed grouped aggregation (Structured streaming)

Step 3: Data Storage
- using  relational database ( PostgreSQL)

Step 4: Automation 
- Using Apache Airflow
## case 1: 

Supposed we worked in a big insurrance company and analytics data stored in a data lake. An analyst tells you they need hourly, daily, and weekly active user data for a dashboard that refreshes every hour.