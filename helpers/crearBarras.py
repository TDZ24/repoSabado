import matplotlib.pyplot as plt 

def graficapromedioSalarial(dataFrame, campoX, campoY, nombreGrafica):
    colores=['green', 'red', 'blue']
    salarioPromedio=dataFrame.groupby(campoX)[campoY].mean()
    
    #Generar la grafica
    
    plt.bar( salarioPromedio.index, salarioPromedio, color=colores)
    
    plt.title("Promedio Salarial")
    plt.xlabel("Cargos")
    plt.ylabel("salario Mensual")
    
    plt.savefig(f'./assets/img/{nombreGrafica}.png')
        