import pandas as pd
from data.data1 import apartamento1,apartamento2
from helpers.crearTablaHTML import crearTabla
from helpers.crearBarras import graficapromedioSalarial
from helpers.crearTorta import calcularPromedioSalariosPorEdad


tabla1=pd.DataFrame(apartamento1,columns=['edad'])
tabla2=pd.DataFrame(apartamento2,columns=['edad'])
tabla3=pd.read_csv("./data/empleados.csv")


#Efectuando filtros con python

#1. Definir una condicion logica 
empleadosJovenesAnalistas1 = tabla3.query('cargo == "analista1"')
empleadosPobres = tabla3.query('salario < 5000000 and cargo == "analista2"')
jubilados = tabla3.query('edad > 50')

#2. Importamos la tabla con el HTML conjunto al dataframe
crearTabla(empleadosJovenesAnalistas1,"tablaJovenes")
crearTabla(empleadosPobres,"tablaPobre")
crearTabla(jubilados,"tablascendidoacliente")

#- Generar promedio salarial 
graficapromedioSalarial(jubilados,'cargo','salario','jubilados')
calcularPromedioSalariosPorEdad(empleadosJovenesAnalistas1,[20,30,40,50,60],'edad','salario','GraficaPieAnalistas')



