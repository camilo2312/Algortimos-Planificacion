# Función que ordena los procesos por tiempo de llegada
def sortByArrival(at, n):
	
	for i in range(0, n - 1):
		for j in range(i + 1, n):
			if at[i] > at[j]:
				at[i], at[j] = at[j], at[i]

if __name__ == '__main__':
	
	sum_bt = 0
	avgwt = 0
	avgTT = 0
	n = int(input("Cantidad de procesos  "))
	# Tiempo quemado
	burst_time = [0]*n
	# Tiempo de llegada
	arrival_time = [0]*n

	for i in range(0,n):
		arrival_time[i]=int(input("Ingrese el tiempo de llegada #"+str(i+1)+" : "))
		

	for i in range(0,n):
		burst_time[i]=int(input("Ingrese el tiempo quemado del proceso #"+str(i+1)+" : "))

	completed =[0] * n
	waiting_time = [0] * n
	turnaround_time = [0] * n
	normalised_TT = [0] * n
	
	
	process = []
	
	# Inicializa las variables de estructura
	for i in range(0, n):
		process.append(chr(65 + i))
		sum_bt += burst_time[i]
		
	# Ordena los procesos por tiempo de llegada
	sortByArrival(arrival_time, n)
	print("Nombre", "Tiempo de llegada",
		"Tiempo quemado", "Tiempo de espera",
		"Giro de vuelta", "Tiempos normalizados")
	t = arrival_time[0]
	
	while(t < sum_bt):
		
		# Setea el limite inferior para la relación de la respuesta
		hrr = -9999
		temp, loc = 0, 0
		
		for i in range(0, n):
			
				# Chequea si el proceso que ha llegado esta incompleto
			if arrival_time[i] <= t and completed[i] != 1:
				
				# Calcula la respuesta
				temp = ((burst_time[i] +
						(t - arrival_time[i])) /
						burst_time[i])
						
				if hrr < temp:
					
					# Respuesta de almacenamiento
					hrr = temp
					
					# Ubicación del almacenamiento
					loc = i
					
		# Actualiza el valor del tiempo
		t += burst_time[loc]
		
		# Calcula el tiempo de espera
		waiting_time[loc] = (t - arrival_time[loc] -
								burst_time[loc])
		
		# Calcula el tiempo de respuesta
		turnaround_time[loc] = t - arrival_time[loc]
		
		# Suma el total de tiempos de respuesta
		avgTT += turnaround_time[loc]
		
		# Calcula el tiempo de respuesta normalizado
		normalised_TT = float(turnaround_time[loc] /
							burst_time[loc])
		
		# Actualiza el estado de finalización
		completed[loc] = 1
		
		# Suma los tiempos de espera
		avgwt += waiting_time[loc]
		
		print(process[loc], "\t\t", arrival_time[loc],
			"\t\t", burst_time[loc], "\t\t",
			waiting_time[loc], "\t\t",
			turnaround_time[loc], "\t\t",
			"{0:.6f}".format(normalised_TT))

	print("Promedio tiempo de espera: {0:.6f}".format(avgwt / n))
	print("Promedio tiempo de respuesta: {0:.6f}".format(avgTT / n))
