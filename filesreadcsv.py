lista = []
datos=open('datos.csv','r')
_=datos.readline()
for linea in datos.readlines():
    datos_separados = linea.split(",")
    print(datos_separados)
datos.close()

#ventas totales
#ventas totales por ano 
#venta totales por trimestre
#promedio de ventas por ano 