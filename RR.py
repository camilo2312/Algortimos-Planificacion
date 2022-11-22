# Función para encontrar los tiempos de espera
# de todos los procesos
def findWaitingTime(processes, n, bt,
                         wt, quantum):
    rem_bt = [0] * n
 
    # Copia el tiempo quemado en rem_bt[]
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0 # Tiempo actual
 
    # Recorre todos los procesos en redondo esa es
    # la manera robin hasta que todos no estén hechos
    while(1):
        done = True
 
        # Atraviesa todos los procesos 1 a 1 muchas veces
        for i in range(n):
             
            # Si el tiempo de rafaga de un proceso es mayo a 0
            # entonces este necesita más tiempo de procesamiento
            if (rem_bt[i] > 0) :
                done = False # Señala un proceso pendiente
                 
                if (rem_bt[i] > quantum) :
                 
                    # Aumenta el valor de T y muestra el tiempo ha consumido
                    # el proceso
                    t += quantum
 
                    # Disminuye el proceso por la cantidad de tiempo
                    # invertido
                    rem_bt[i] -= quantum
                 
                # Si el tiempo de rafaga es menor o igual a quantum
                # es el ultimo ciclo del proceso
                else:
                 
                    # Aumenta el valor de T y muestra el tiempo ha consumido
                    # el proceso
                    t = t + rem_bt[i]
 
                    # El tiempo de espera es el tiempo actual menos el invertido 
                    # en este proceso
                    wt[i] = t - bt[i]
 
                    # A medida que el tiempo se ejecuta su tiempo de refaga se
                    # vuelve 0
                    rem_bt[i] = 0
                 
        # Si todos los procesos están completados
        # termina el ciclo
        if (done == True):
            break
             
# Función que calcula el tiempo de respuesta
def findTurnAroundTime(processes, n, bt, wt, tat):
     
    # Calcula el tiempo de respuesta
    for i in range(n):
        tat[i] = bt[i] + wt[i]
 
 
# Función que calcula el tiempo promedio
# del tiempo de espera y de respuesta
def findavgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n
 
    # Función que encuentra los tiempos de espera
    # de todos los procesos
    findWaitingTime(processes, n, bt,
                         wt, quantum)
 
    # Función que encuentra los tiempos 
    # de respuesta de todos los procesos
    findTurnAroundTime(processes, n, bt,
                                wt, tat)
 
    # Imprime los procesos con sus detalles
    print("Proceso    Tiempo quemado     Tiempo de",
                     "Espera    Tiempo de respuesta")
    total_wt = 0
    total_tat = 0
    for i in range(n):
 
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i],
              "\t\t", wt[i], "\t\t", tat[i])
 
    print("\nTiempo promedio de espera = %.5f "%(total_wt /n) )
    print("Tiempo promedio de respuesta = %.5f "% (total_tat / n))
     
# Driver code
if __name__ =="__main__":
     
    n = int(input('Ingrese la cantidad de procesos: '))
    proc = [0] * n
    burst_time = [0] * n
    # Process id's
    for i in range(0, n):
        proc[i] = i + 1
        burst_time[i] = int(input('Ingrese el tiempo quemado del proceso #' + str(i + 1) + ': '))
    quantum = int(input('Ingrese el preíodo cuántico de tiempo: '))
 
    findavgTime(proc, n, burst_time, quantum)
 
# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)