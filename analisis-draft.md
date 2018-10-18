# Universidad EAFIT - ST0263: Tópicos Especiales en Telemática, 2018-2

## Proyecto  3: Big Data

## Documento Análisis-draft.md

### Integrantes
1. Yorman Andres Aguirre Martinez
2. Andrés Gómez Vásquez 
3. Mariana Ramirez Duque

## Proyecto Seleccionado
**Realizar una prueba de concepto o demo sobre Data Streaming desde Twitter utilizando una de las siguientes tecnologías: Kafka, Storm, Flink o Flume.**

###¿Por qué  seleccionamos este proyecto?
* Nos reunimos a ver opción por opción cuál nos llamaba más la atención de manera que todo el grupo quedara satisfecho con el proyecto a realizar, la mejor opción en la que todos sentimos que nos gustaria más trabajar fue la segunda.

* Comparandola con las demás opciones nos parecio que no era tan complicado de realizar pero tampoco tan facil para un equipo de 3 personas.

* Al buscar información de este tipo de aplicaciones con estas herramientas en internet encontramos muchos videos e información al respecto que nos dio la seguridad para irnos por este lado.

* Lo seleccionamos porque fue el que más nos llamó la atención y con el que todos estuvimos de acuerdo.

## Referenciación de conceptos y tecnologias

### ¿Qué son los datos de streaming?

Los datos de streaming son datos que se generan constantemente a partir de miles de fuentes de datos, que normalmente envían los registros de datos simultáneamente en conjuntos de tamaño pequeño (varios kilobytes). Los datos de streaming incluyen diversos tipos de datos, como archivos de registros generados por los clientes que utilizan sus aplicaciones móviles o web, compras electrónicas, actividades de los jugadores en un juego, información de redes sociales, operaciones bursátiles o servicios geoespaciales, así como telemetría de dispositivos conectados o instrumentación en centros de datos.

Estos datos deben procesarse de forma secuencial y gradual registro por registro o en ventanas de tiempo graduales, y se utilizan para una amplia variedad de tipos de análisis, como correlaciones, agregaciones, filtrado y muestreo. La información derivada del análisis aporta a las empresas visibilidad de numerosos aspectos del negocio y de las actividades de los clientes, como el uso del servicio (para la medición/facturación), la actividad del servidor, los clics en un sitio web y la ubicación geográfica de dispositivos, personas y mercancías, y les permite responder con rapidez ante cualquier situación que surja. Por ejemplo, las empresas pueden supervisar los cambios en la opinión pública de sus marcas y productos al analizar constantemente las transmisiones de los medios sociales y responder rápidamente cuando sea necesario. 

### Ventajas de los datos en streaming

El procesamiento de los datos de streaming supone una ventaja en la mayoría de las situaciones en las que se generan datos nuevos y dinámicos de forma constante. Es apto para la mayoría de los sectores y casos de uso de big data. Por lo general, las empresas comienzan con aplicaciones sencillas, como la recopilación de registros del sistema, y el procesamiento rudimentario, como la implementación de cálculos mín.-máx. Más adelante, estas aplicaciones evolucionan y se pasa al procesamiento más sofisticado casi en tiempo real. En un principio, las aplicaciones pueden procesar transmisiones de datos para producir informes básicos y realizar acciones sencillas como respuesta, por ejemplo, emitir alertas cuando las medidas clave superan ciertos umbrales. Con el tiempo, dichas aplicaciones realizan un análisis de datos más sofisticado, como la aplicación de algoritmos de aprendizaje automático y la extracción de información más exhaustiva a partir de los datos. Con el tiempo, se aplican algoritmos complejos de procesamiento de eventos y transmisiones, como las ventanas de tiempo de decaimiento para encontrar las películas más populares, lo que proporciona todavía más información. 

### Apache Kafka

Apache Kafka es un sistema de almacenamiento publicador/subscriptor distribuido, particionado y replicado. Estas características, añadidas a que es muy rápido en lecturas y escrituras lo convierten en una herramienta excelente para comunicar streams de información que se generan a gran velocidad y que deben ser gestionados por uno o varias aplicaciones. Se destacan las siguientes características:
Funciona como un servicio de mensajería, categoriza los mensajes en topics.

- Los procesos que publican se denominan brokers y los subscriptores son los consumidores de los topics.

- Utiliza un protocolo propio basado en TCP y Apache Zookeeper para almacenar el estado de los brokers. Cada broker mantiene un conjunto de particiones (primaria y secundaria) de cada topic.

- Se pueden programar productores/consumidores en diferentes lenguajes: Java, Scala, Python, Ruby, C++

- Escalable y tolerante a fallos.

- Se puede utilizar para servicios de mensajería (tipo ActiveMQ o RabbitMQ), procesamiento de streams, web tracking, trazas operacionales, etc.
