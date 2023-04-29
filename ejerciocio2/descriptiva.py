import csv
from statistics import *





def apertura():
    edad= []
    with open('edad.csv') as file:
        reader = csv.reader(file)
        for row in reader:            
            edad.append(int(row[0]))
            
    return edad       

def promedio(date)-> float: 
    return mean(date)

def mediana(date)-> float:
    return median(date)

def moda(date)-> float:
    return mode(date)

def quartiles(date)-> float:
    return quantiles(date)

def varianza(date)-> float:
    return variance(date)

if __name__ =="__main__":
    muestra = apertura()
    
    print("Promedio de edades {}".format(promedio(muestra)))
    print("Mediana de edades {}".format(mediana(muestra)))
    print("Moda de edades {}".format(moda(muestra)))
    print("quartiles de edades {}".format(quartiles(muestra)))
    print("varianza de edades {}".format(varianza(muestra)))
    print("rango de la muestar [{}..{}]".format(min(muestra),max(muestra)))