from SparkInitializer import SparkInitializer

from pyspark.sql.types import *
from pyspark.sql.functions import *

import requests
import base64
import time

class SpotifyDataProcessor:
    """
    A class to process Spotify data for a list of artists.

    Args:
        spark (SparkSession): The Spark session object.

    Attributes:
        spark (SparkSession): The Spark session object.
    """

    def __init__(self, spark):
        self.spark = spark

    def process_artists(self, file_path):
        """
        Process Spotify data for a list of artists.

        Args:
            file_path (str): The path to the file containing artist names.

        """
        with open(file_path, 'r', encoding='utf-8') as file:
            artist_names = file.read().splitlines()

        for name in artist_names:
            data = self.get_spotify_data(artist_name=name)
            if data:
                data = self.filter_data(data)
                data = data.withColumn("group_name", lit(name).cast(StringType()))          
                self.write_to_mongodb(data)
                data.show()
            else: 
                print("No data found for", name)
            time.sleep(5)

    def get_spotify_data(self, artist_name):
        """
        Get Spotify data for an artist.

        Args:
            artist_name (str): The name of the artist.

        Returns:
            dict: The Spotify data for the artist.

        """
        client_id = '***'
        client_secret = '***'
        auth_url = 'https://accounts.spotify.com/api/token'

        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())

        response = requests.post(auth_url, data={'grant_type': 'client_credentials'}, 
                                 headers={'Authorization': f'Basic {client_creds_b64.decode()}'})
        token_response_data = response.json()
        access_token = token_response_data['access_token']

        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        search_url = 'https://api.spotify.com/v1/search'
        params = {
            'q': f'{artist_name}',
            'type': 'artist'
        }
        response = requests.get(search_url, headers=headers, params=params)
        data = response.json()

        if 'artists' in data and data['artists']['items']:
            artist_id = data['artists']['items'][0]['id']
            print(f"Artist ID for {artist_name}: {artist_id}")

            albums_url = f'https://api.spotify.com/v1/artists/{artist_id}/albums'
            params = {
                'include_groups': 'album', 
                'limit': None
            }
            response = requests.get(albums_url, headers=headers, params=params)
            data = response.json()
            
            return data
        else:
            print("Artist not found")
            return {}

    def filter_data(self, data):
        """
        Filter data.

        Args:
            data (dict): The data to filter.

        Returns:
            DataFrame: The filtered DataFrame.

        """
        schema = StructType([
            StructField("album_type", StringType(), True),
            StructField("total_tracks", IntegerType(), True),
            StructField("name", StringType(), True),
            StructField("release_date", StringType(), True),
            StructField("id", StringType(), True)
        ])

        albums = [{
            "album_type": album.get("album_type"),
            "total_tracks": album.get("total_tracks"),
            "name": album.get("name"),
            "release_date": album.get("release_date"),
            "id": album.get("id")
        } for album in data.get('items', [])]

        df = self.spark.createDataFrame(albums, schema=schema)

        return df

    def write_to_mongodb(self, data):
        """
        Write data to MongoDB.

        Args:
            data (DataFrame): The DataFrame to write.

        """
        data.write.format("mongo") \
            .option("uri", "mongodb://cagri:3541@172.80.0.10:27017/spotify.albums?authSource=admin") \
            .mode("append") \
            .save()    


if __name__ == "__main__":
    spark = SparkInitializer.initialize_spark()
    processor = SpotifyDataProcessor(spark)
    processor.process_artists('group_names.txt')
    spark.stop()
