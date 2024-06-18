## 1. Copy/push project to VM

## 2. Fix sh files
```commandline
sed -i 's/\r$//' spark/spark-master.sh
sed -i 's/\r$//' spark/spark-worker.sh
```
## 3. Docker compose
```commandline
docker-compose build

docker-compose up --scale spark-worker=2 -d
```

## 4. Submit spark code
```commandline
spark-submit --master spark://spark-master:7077 /opt/examples/sparktest.py
```

## 5. Spark Master UI
```
http://localhost:5050/
```

