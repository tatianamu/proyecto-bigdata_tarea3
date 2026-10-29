# Importamos librerías necesarias
from pyspark.sql import SparkSession, functions as F
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Inicializamos Spark
spark = SparkSession.builder.appName('datos').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

# Ruta del archivo CSV en HDFS
file_path = 'hdfs://localhost:9000/datos/accidentes.csv'

# Leemos el archivo CSV
df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load(file_path)

# Imprimimos el esquema
df.printSchema()

# Mostramos las primeras filas
df.show(5)

# Contamos los registros
print("Total de accidentes:", df.count())

# Mostramos estadísticas generales
df.describe().show()

# Contamos los valores nulos
df.select([
    F.sum(F.col(c).isNull().cast('int')).alias(c)
    for c in df.columns
]).show()

# Eliminamos registros duplicados
df = df.dropDuplicates()

print("Registros después de eliminar duplicados:", df.count())

# Gráfica 1: accidentes por tipo de vehículo
tipos = df.groupBy('tipo_vehiculo').count().orderBy(F.desc('count')).limit(10).toPandas()

plt.figure(figsize=(9, 5))
plt.bar(tipos['tipo_vehiculo'].astype(str), tipos['count'])
plt.title('Top 10 tipos de vehículos involucrados')
plt.ylabel('Cantidad de accidentes')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('grafico_1_tipo_vehiculo.png')
plt.close()

# Gráfica 2: accidentes por departamento
deptos = df.groupBy('departamento_accidente').count().orderBy(F.desc('count')).limit(10).toPandas()

plt.figure(figsize=(9, 5))
plt.barh(deptos['departamento_accidente'].astype(str), deptos['count'], color='seagreen')
plt.gca().invert_yaxis()
plt.title('Top 10 departamentos con más accidentes')
plt.xlabel('Cantidad de accidentes')
plt.tight_layout()
plt.savefig('grafico_2_departamento.png')
plt.close()

# Gráfica 3: accidentes por gravedad
graves = df.groupBy('gravedad_accidente').count().toPandas()

plt.figure(figsize=(8, 5))
plt.bar(graves['gravedad_accidente'].astype(str), graves['count'], color='salmon')
plt.title('Accidentes por gravedad')
plt.ylabel('Cantidad de accidentes')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('grafico_3_gravedad.png')
plt.close()

# Mensaje final
print("Gráficos guardados correctamente:")
print("grafico_1_tipo_vehiculo.png")
print("grafico_2_departamento.png")
print("grafico_3_gravedad.png")

# Cerramos Spark
spark.stop()

