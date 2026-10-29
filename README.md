Proyecto Big Data: Análisis de accidentes de tránsito en Colombia

Análisis del archivo datos.py

Con este archivo se realizará el procesamiento batch de los datos abiertos sobre accidentes de tránsito en Colombia, utilizando Python y Apache Spark (PySpark). El programa permitirá explorar y analizar la información almacenada en Hadoop HDFS, identificar valores nulos y registros duplicados, obtener estadísticas generales y generar gráficas para visualizar los accidentes según el tipo de vehículo, el departamento y la gravedad. De esta manera, se busca transformar los datos en información útil para comprender mejor su comportamiento y distribución.

Instrucciones de ejecución

1. Iniciar los servicios de Hadoop

start-all.sh

2. Crear el directorio en HDFS

hdfs dfs -mkdir -p /datos

3. Descargar el dataset

Ubicarse en el directorio de trabajo:

cd /home/hadoop

Descargar los datos abiertos de accidentes de tránsito desde datos.gov.co:

wget -O accidentes.csv 'https://www.datos.gov.co/resource/6jmc-vaxk.csv?$limit=500000'

4. Cargar el archivo CSV en HDFS

hdfs dfs -put /home/hadoop/accidentes.csv /datos

5. Verificar el archivo en HDFS

hdfs dfs -ls /datos

6. Crear o editar el programa de procesamiento

nano datos.py

En este archivo se encuentra el código Python que utiliza PySpark para leer y procesar los datos almacenados en HDFS.

7. Ejecutar el procesamiento batch

spark-submit datos.py

El programa consulta el esquema, muestra los primeros registros, calcula estadísticas generales, identifica valores nulos, elimina duplicados y genera tres gráficas sobre los accidentes de tránsito.

8. Visualizar las gráficas generadas

Iniciar un servidor HTTP desde el directorio donde se guardaron las gráficas:

python3 -m http.server 8000 --bind 0.0.0.0

Consultar la dirección IP de Ubuntu:

hostname -I

Desde el navegador de Windows, reemplazar IP_DE_UBUNTU por la dirección IP obtenida y abrir los siguientes enlaces:

http://IP_DE_UBUNTU:8000/grafico_1_tipo_vehiculo.png

http://IP_DE_UBUNTU:8000/grafico_2_departamento.png

http://IP_DE_UBUNTU:8000/grafico_3_gravedad.png

9. Resultados

El programa genera las siguientes gráficas:

grafico_1_tipo_vehiculo.png: diez tipos de vehículos con mayor cantidad de registros.

grafico_2_departamento.png: diez departamentos con mayor cantidad de registros.

grafico_3_gravedad.png: distribución de los registros según la gravedad del accidente.

Los resultados permiten explorar el dataset y visualizar patrones en los registros analizados.

Tecnologías utilizadas

Python 3

Apache Spark (PySpark)

Hadoop HDFS

Matplotlib

Datos abiertos de Colombia

Fuente de datos

Dataset de accidentes de tránsito de datos.gov.co:

https://www.datos.gov.co/resource/6jmc-vaxk.csv

Autor

Proyecto académico individual de Big Data.
