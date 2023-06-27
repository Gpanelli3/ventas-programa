lista = []
datos=open('datos.csv','r')
_=datos.readline()

eleccion=int(input('MENU \n 1- VENTAS TOTALES POR ANO \n 2- VENTAS TOTALES POR TRIMESTRE \n 3- PROMEDIO VENTAS POR ANO \n 4-SALIR'))


def ventasTotales():
        total=0
        b=int(input('ingresar el ano para saber las ventas totales'))
        for linea in datos.readlines():
            datos_separados = linea.strip().split(";")  

            if int(datos_separados[0])==b:
                datos_separados.pop(0)
                #print(datos_separados)
                for linea in datos_separados:
                    linea=int(linea)
                    total+=linea
        print(f'el total de ventas del {b} es: {total}')

def ventasPorTrimestre():
        trimestre=int(input('ingresar el trimestre que quiera saber las ventas totales \n 1-Primer trimestre \n 2-Segundo trimestre \n 3-Tercer trimestre '))
        totalTrimestre=0
        mes=0

        for linea in datos.readlines():
            datos_separados=linea.split(';')
            dat=int(datos_separados[trimestre])
            totalTrimestre+=dat
        print(f'el total de ventas del trimestre consultado es {totalTrimestre}')

def promedio():
        contador=0
        total=0
        promedio=0
        b=int(input('ingresar el ano para saber el promedio de ventas de ese ano'))
        for linea in datos.readlines():
            datos_separados = linea.strip().split(";")  
            contador+=1

            if int(datos_separados[0])==b:
                datos_separados.pop(0)

                for linea in datos_separados:
                    linea=int(linea)
                    total+=linea
                    promedio=total/contador

        print(f'el promedio de las ventas totales es: {promedio}')




if eleccion == 1:
    ventasTotales()
elif eleccion == 2:
    ventasPorTrimestre()
elif eleccion == 3:
    promedio()
# elif eleccion == 4:
#         False



datos.close()

            

        





        