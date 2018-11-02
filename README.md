# sparkStreaming-Kafka-Demo
El objetivo de este proyecto es el analisis de sentimientos por medio de Spark Streaming y Kafka, utilizando Twitter Streaming API y Python

Ejecutar:

Instalar los requisitos:

`$ sudo pip install -r requisitos.txt`

Iniciar el servicio de kafka (Configurar para que corra en localhost:9092)

Crear un topico llamado twitterstream

`$ bin/kafka-topics.sh --create --zookeeper --partitions 1 --topic twitterstream localhost:2181 --replication-factor 1`

Iniciar el streaming con tweepy:

`$ python app.py`

Para comprobar que kafka esta recibiendo mensajes:

`$ bin/kafka-console-consumer.sh --zookeeper localhost:9092 --topic twitterstream --from-beginning`

Correr el analizador de Spark Streaming:

`$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.5.1 twitterStream.py`
