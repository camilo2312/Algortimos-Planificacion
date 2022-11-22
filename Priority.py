# Función que permite encontrar el tiempo de espera para
# cada proceso
def findWaitingTime(processes, n, wt):
    wt[0] = 0
 
    # Calcula el tiempo de espera
    for i in range(1, n):
        wt[i] = processes[i - 1][1] + wt[i - 1]
# Function to calculate turn around time
def findTurnAroundTime(processes, n, wt, tat):
     
    # Calcula el tiempo de respuesta
    # adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]
 
# Función que calcula el tiempo promedio de espera y los tiempos de respuesta
def findavgTime(processes, n):
    wt = [0] * n
    tat = [0] * n
 
    # Función que encuentra el tiempo de espera de cada proceso
    findWaitingTime(processes, n, wt)
 
    # Función que encuentra los tiempos de respuesta de todos los procesos
    findTurnAroundTime(processes, n, wt, tat)
 
    # Imprime los procesos con sus respectivos tiempos
    print("\nProceso    Tiempo quemado    Tiempo Espera",
          "   Tiempo de respuesta")
    total_wt = 0
    total_tat = 0
    for i in range(n):
 
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", processes[i][0], "\t\t",
                   processes[i][1], "\t\t",
                   wt[i], "\t\t", tat[i])
 
    print("\nTiempo promedio de espera = %.5f "%(total_wt /n))
    print("Tiempo promedio de respuesta = ", total_tat / n)
 
def priorityScheduling(proc, n):
     
    # Ordena los procesos por prioridad
    proc = sorted(proc, key = lambda proc:proc[2],
                                  reverse = True)
 
    print("Orden en que se ejecutan los procesos")
    for i in proc:
        print(i[0], end = " ")
    findavgTime(proc, n)
     
if __name__ =="__main__":
     
    n = int(input("Ingrese la cantidad de procesos: "))
    proc = [[ 0 for i in range(3) ] for j in range(n)]
    
    for i in range(0, n):
        proc[i][0] = i + 1
        proc[i][1] = int(input('Ingrese el tiempo quemado del proceso #' + str(i + 1) + ': '))
        proc[i][2] = int(input('Ingrese la prioridad del proceso entre (1 y 10) #' + str(i + 1) + ': '))
    priorityScheduling(proc, n)
