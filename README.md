# SpotifyAPI_PySpark_Mongodb

This demo contains a API system and Spark, MongoDB connection. There's a 2 worker node and 1 master of spark containers also there's a single mongodb.
![Screenshot from 2024-06-18 23-05-31](https://github.com/mcagriaktas/SpotifyAPIs_Spark_Mongo/assets/52080028/b378b3aa-7598-40a0-8469-afaaf72b6d82)

Set-up
1. git clone this project from GitHub
2. Your mongodb data will be in mongodb => mongo_data folder.
3. You can use your local scrip the container master: .master("spark://172.80.0.110:7077"), but you can use also in sparkMaster => submitfiles folder.
   ![Screenshot from 2024-06-18 23-16-53](https://github.com/mcagriaktas/SpotifyAPIs_Spark_Mongo/assets/52080028/69baf8e3-7788-4ba3-9faa-bdc193878012)
4. cd the git clone path, docker-compose.yamp up -d --build
5. You can easly create a app for Spotify API: https://developer.spotify.com/documentation/web-api
6. Then check the main.py, how to start spark and connect spark-master container and mongodb.
