# SpotifyAPI_PySpark_Mongodb

This demo contains an API system, a Spark-MongoDB connection, and consists of 2 worker nodes and 1 master node for Spark containers, along with a single MongoDB instance.

![Screenshot from 2024-06-18 23-05-31](https://github.com/mcagriaktas/SpotifyAPIs_Spark_Mongo/assets/52080028/b378b3aa-7598-40a0-8469-afaaf72b6d82)

Setup:

1. Clone this project from GitHub.
2. Your MongoDB data will be in the mongodb => mongo_data folder.
3. You can use your local script to start the container master: .master("spark://172.80.0.110:7077"), or you can use the script in the sparkMaster => submitfiles folder.
   
   ![Screenshot from 2024-06-18 23-16-53](https://github.com/mcagriaktas/SpotifyAPIs_Spark_Mongo/assets/52080028/69baf8e3-7788-4ba3-9faa-bdc193878012)
   
4. Navigate to the git clone path and check the spark and mongodb folder for how to build your containers.
5. You can easily create an app for the Spotify API: https://developer.spotify.com/documentation/web-api.
6. Then, check the main.py file to see how to start Spark and connect the Spark master container to MongoDB.
