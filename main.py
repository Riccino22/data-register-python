import pandas


serie = pandas.Series([ 1 , 2 , 3 , 4 ])
serie.name = "nombre"

totalNombres = []
totalApellidos = []
totalEdades = []

def insertData():
    nombre = input("\nA. Como te llamas?: ")
    apellido = input("B. Cual es tu apellido?: ")
    edad = int(input("C. Dinos tu edad: "))

    totalNombres.append(nombre)
    totalApellidos.append(apellido)
    totalEdades.append(edad)
    
    df = pandas.DataFrame({
    'NOMBRE' : totalNombres,
    'APELLIDO' : totalApellidos,
    'EDADES': totalEdades
    })

    print("\n")
    print(df)

    edadPromedio = df['EDADES'].mean()

    print("\nEDAD PROMEDIO DE LOS ENCUESTADOS: " + str(int(edadPromedio)))


    restart = input("\nIsertar mas datos? (y/n): ")
    

    if restart == "y":
        insertData()
    else:
        print("Programa finalizado")
        exit()

insertData()





#dh = df.iloc[[ 0 , 2 ],[ 0 , 1 ]]
#dh = pandas.read_csv('data/iris.data', header=None)
#print(totalApellidos)
