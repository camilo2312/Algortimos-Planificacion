# Función para calcular el tiempo de espera de todos
#  los procesos
def findWaitingTime(processes, n,
					bt, wt):

	# Tiempo de espera para el primer proceso es 0
	wt[0] = 0


	# Calcula el tiempo de espera
	for i in range(1, n ):
		wt[i] = bt[i - 1] + wt[i - 1]

# Función que calcula el giro alrededor del tiempo
def findTurnAroundTime(processes, n,
					bt, wt, tat):

	# calculating turnaround
	# time by adding bt[i] + wt[i]
	for i in range(n):
		tat[i] = bt[i] + wt[i]

# Función que calcula el tiempo promedio
def findavgTime( processes, n, bt):

	wt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_tat = 0

	# Función que encuentra el tiempo promedio de espera 
    # para todos los procesos
	findWaitingTime(processes, n, bt, wt)

	# Función que calcula el tiempo de respuesta
    # para todos los procesos
	findTurnAroundTime(processes, n,
					bt, wt, tat)

	# Imprime los procesos con sus detalles
	print( "Procesos Tiempo quemado " +
				" Tiempo de espera " +
				" Tiempo de respuesta")

	# Calcula el tiempo total de espera y de respuesta
	for i in range(n):
	
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" " + str(i + 1) + "\t\t" +
					str(bt[i]) + "\t " +
					str(wt[i]) + "\t\t " +
					str(tat[i]))

	print( "Tiempo promedio de espera = "+
				str(total_wt / n))
	print("Tiempo promedio de respuesta = "+
					str(total_tat / n))

if __name__ =="__main__":
	n = int(input("Cantidad de procesos  "))
	# process id's
	processes = [0]*n
	burst_time = [0]*n
	#n = len(processes)

	# Tiempo quemado de los procesos
	
	for i in range(0,n):
		processes[i]=i
		burst_time[i]=int(input("Ingrese el tiempo quemado del proceso #"+str(i+1)+" : "))

	findavgTime(processes, n, burst_time)
