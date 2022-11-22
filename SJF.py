def calculateWaitingTime(process, n): 
    for i in range(n):
        process[i][2] = 0
        for j in range(i):
            process[i][2] += process[j][1]

def calculateTurnAroundTime(process, n):
    for i in range(n):
        process[i][3] = process[i][1] + process[i][2]

def calculateAndPrintAvgTimes(process, n):
    avg_wt = 0
    avg_tat = 0
    totalWt = 0
    totalTat = 0

    print("Proceso   Tiempo quemado   Tiempo de espera   Tiempo de respuesta\n")

    for i in range(n):
        totalWt += process[i][2] 
        totalTat += process[i][3]

        print("P", process[i][0], "\t\t"
                 , process[i][1], "\t\t"
                 , process[i][2], "\t\t"
                 , process[i][3], "\t\t")
    avg_wt = totalWt/n
    avg_tat = totalTat/n

    print("\nTiempo promedio de espera= ", avg_wt)
    print("Tiempo promedio de respuesta= ", avg_tat)

def calculateAverageWaitingAndTatTime(process, n):
    # Calcula el tiempo de espera de todos los procesos
    calculateWaitingTime(process, n)

    # Calcula el tiempo de respuesta
    calculateTurnAroundTime(process, n)

    # Calcula el tiempo promedio de espera y de respuesta
    calculateAndPrintAvgTimes(process, n)

def sortingProcess(process, n):
    for i in range(n):
        index = i
        for j  in range(i+1, n):
            if process[j][1] < process[index][1]:
                index = j
        temp = process[i][1]
        process[i][1] = process[index][1]
        process[index][1] = temp
 
        temp = process[i][0]
        process[i][0] = process[index][0]
        process[index][0] = temp
    
    calculateAverageWaitingAndTatTime(process, n)

if __name__ =="__main__":

    n = int(input('Ingrese la cantidad de procesos: ')) 
    proc = [[ 0 for i in range(4) ] for j in range(n)] 
    
    for i in range(0, n):
        proc[i][0] = i + 1
        proc[i][1] = int(input('Ingrese el tiempo quemado del proceso #' + str(i + 1) + ': '))
        proc[i][2] = 0
        proc[i][3] = 0
    sortingProcess(proc, n)
