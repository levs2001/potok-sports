# Start cluster
```shell
docker compose up -f ./kafka/docker-compose.yml
~/Programms/flink-1.20.0/bin/start-cluster.sh
~/Programms/flink-1.20.0/bin/flink run -c ru.leo.potok.Process /Users/lsaskov/MyProgramms/Itmo/potok-football-flink/build/libs/potok-football-flink-1.0-all.jar

python ./generator/generator_producer.py
python ./generator/match_event_generator.py

python ./client/server_consumer.py
python ./client/client.py
```
##
[kafka ui](http://localhost:8080/ui/clusters/kraft/topics) 
[flink ui](http://localhost:8081/#/overview)

# Stop cluster
```shell
~/Programms/flink-1.20.0/bin/stop-cluster.sh
cd kafka
docker compose down
```
