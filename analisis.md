# Universidad EAFIT - ST0263: Tópicos Especiales en Telemática, 2018-2

## Proyecto 3: Big Data

## Documento análisis.md

### Problema a resolver

El aumento del uso de redes sociales ha hecho que cada vez se hagan más estudios sobre ellas, de manera de ocuparlas como fuentes de información sobre diferentes temas que van desde la publicidad a estudios socioculturales. De esta manera, durante los últimos años, se ha desarrollado y perfeccionado la forma de extraer y analizar esta información por medio del análisis de sentimientos. Este análisis consiste en determinar la opinión de comentarios en la web sobre diversos temas. Es así, como por medio de diferentes algoritmos se ha buscado obtener la opinión de los usuarios de Internet de forma automática abarcando la mayor cantidad de gente posible (Montesinos, 2014).

El análisis de sentimientos o sentiment analysis es el estudio por el cual se determina la opinión de las personas en Internet sobre algún tema en específico, prediciendo la polaridad de los usuarios (a favor, en contra, neutro, etc), abarcando temas que van desde productos, películas, servicios a intereses socio-culturales como elecciones, guerras, fútbol, etc.

Este será el caso de aplicación que desarrollaremos en el proyecto 3, el objetivo será hacer análisis de sentimientos en tiempo real de tweets en la red social de twitter para determinar los sentimientos que pueden sentir las personas a través del determinado uso de ciertas palabras. La idea inicial es aplicar este análisis a temas deportivos orientándose fundamentalmente hacia el fútbol para determinar si la polaridad de los comentarios es positiva o negativa.

### Arquitectura preliminar de datos

![alt text](https://github.com/yaguirre/sparkStreaming-Kafka-Demo/blob/master/images/arquitectura%20de%20datos.png)

### Fuentes y naturaleza de los datos + Tecnologías a utilizar  
La fuente de los datos es la red social Twitter, el formato de los datos es no estructurado, son tweets en tiempo real de usuarios que opinan sobre un tópico a analizar.
Para extraer los datos de Twitter se utilizara tweepy, una librería de python usada para acceder a la  API de Twitter, esta API nos brinda funciones de extracción de tweets en tiempo real (Twitter Streaming API).


### Sistema de ingesta de datos + Tecnologías a utilizar
Para la ingesta de datos usamos Apache Kafka, una plataforma de streaming distribuida, que usa una mensajería de publicación-suscripción y ofrece un servicio distribuido y replicado. El stream de Twitter, es ingestado por Kafka y enviado como señales a Kafka.

También usaremos Tweepy, la librería de Python para acceder a la API de Twitter y así obtener los tweets 


### Almacenamiento de los datos + Tecnologías a utilizar
Para el almacenamiento de los datos generados por Spark Streaming utilizaremos HDFS 


### Análisis de datos + Tecnologías a utilizar
Spark Streaming recibe los datos de Kafka y los procesa con el Spark Engine, para el análisis de los tweets y juzgarlos como positivos o negativos 

### Referencias
>  * **Montesinos, L. (2014). ANÁLISIS DE SENTIMIENTOS Y PREDICCIÓN DE EVENTOS EN TWITTER. Santiago de Chile: UNIVERSIDAD DE CHILE FACULTAD DE CIENCIAS FÍSICAS Y MATEMÁTICAS. Retrieved from [http://repositorio.uchile.cl/bitstream/handle/2250/130479/cf-montesinos_lg.pdf](http://repositorio.uchile.cl/bitstream/handle/2250/130479/cf-montesinos_lg.pdf)**