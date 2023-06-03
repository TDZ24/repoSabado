import pandas as pd
import matplotlib.pyplot as plt

def calcularPromedioSalariosPorEdad(dataframe, rangos, columnaInteres, columnaPromediar, nombreGrafica):
    plt.figure
    
    #Crear una columna nueva en rangos de edad 
    dataframe['rangosEdad']=pd.cut(dataframe[columnaInteres],bins=rangos)
    
    #Calcular la suma de los salarios por rango de edad
    
    salarioporRango=dataframe.groupby('rangosEdad')[columnaPromediar].sum()
    
    #Definir los datos a graficar
    salario=salarioporRango.values
    rangosEdad=salarioporRango.index
    
    plt.pie(salario, labels=rangosEdad, autopct='%1.1f%%')
    plt.title("Salarios por Rango de Edad")
    
    plt.savefig(f'./assets/img/{nombreGrafica}.png')
    