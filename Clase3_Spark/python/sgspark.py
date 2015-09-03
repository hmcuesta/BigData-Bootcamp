from pyspark import SparkContext

archivo = "hdfs://localhost/user/SG/palabras.txt"

sc = SparkContext("local","Fitra")

datos = sc.textFile(archivo).cache()

numA = datos.filter(lambda t: 'a' in t).count()

numE = datos.filter(lambda t: 'e' in t).count()

print "las a: %i y las e: %i " % (numA, numE)

