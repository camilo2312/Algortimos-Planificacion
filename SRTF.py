# Función para encontrar el tiempo de espera
# para todos los procesos
def findWaitingTime(processes, n, wt): 
    rt = [0] * n
  
    # Copia el tiempo quemado en el arreglo rt[]
    for i in range(n): 
        rt[i] = processes[i][1]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
  
    # Se ejecuta hasta que todos los procesos 
    # se completen
    while (complete != n):
          
        # Encuentra los procesos con el tiempo mínimo restante 
        # entre los procesos que llegan hasta el tiempo actual
        for j in range(n):
            if ((processes[j][2] <= t) and 
                (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if (check == False):
            t += 1
            continue
              
        # Reduce el tiempo de 1 en 1
        rt[short] -= 1
  
        # Actualiza el minimo
        minm = rt[short] 
        if (minm == 0): 
            minm = 999999999

        if (rt[short] == 0): 
  
            # Incrementa el contador de completado
            complete += 1
            check = False
  
            # Encuentra el tiempo de finalización del 
            # proceso actual
            fint = t + 1
  
            # Calcula el tiempo de espera
            wt[short] = (fint - processes[short][1] -    
                                processes[short][2])
  
            if (wt[short] < 0):
                wt[short] = 0
          
        # Incremente el contador de tiempo
        t += 1
  
# Función que calcula el tiempo de respuesta
def findTurnAroundTime(processes, n, wt, tat): 
      
    # Calcula el tiempo de respuesta
    for i in range(n):
        tat[i] = processes[i][1] + wt[i] 
  
# Función que calcula el tiempo promedio de espera y de respuesta
def findavgTime(processes, n): 
    wt = [0] * n
    tat = [0] * n 
  
    # Función que busca el tiempo de espera de todos
    # los procesos
    findWaitingTime(processes, n, wt) 
  
    # Función que encuentra el tiempo de respuesta
    # de todos los procesos
    findTurnAroundTime(processes, n, wt, tat) 
  
    # Imprime los procesos con los detalles 
    print("Proceso    Tiempo quemado     Tiempo", 
                    "espera     Tiempo de respuesta")
    total_wt = 0
    total_tat = 0
    for i in range(n):
  
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print(" ", processes[i][0], "\t\t", 
                   processes[i][1], "\t\t", 
                   wt[i], "\t\t", tat[i])
  
    print("\nTiempo promedio de espera = %.5f "%(total_wt /n) )
    print("Tiempo promedio de respuesta = %.5f"%(total_tat / n)) 
      
if __name__ =="__main__":
    
    # n = int(input('Ingrese la cantidad de procesos: '))
    # proc = [[ 0 for i in range(3) ] for j in range(n)]

    # for i in range(0, n):
    #     proc[i][0] = i + 1
    #     proc[i][1] = int(input('Ingrese el tiempo quemado del proceso #' + str(i + 1) + ': '))
    #     proc[i][2] = int(input('Ingrese el tiempo llegada del proceso #' + str(i + 1) + ': '))

    proc = [[1, 6, 1], [2, 8, 1],
            [3, 7, 2], [4, 3, 3]]
    n = 4
    findavgTime(proc, n)