from asyncio.windows_events import NULL
from math import ceil
from operator import mod
from os import system
from re import X
import time
import msvcrt
import random

from joblib import PrintTime
from psycopg2 import Time

paginas = []
id = 0

for i in range(50):
	if i >= 46:
		paginas.append((i,0,0,"S.O"))
	else:
		paginas.append((i,4,0,"libre"))


def suma(num1,num2):
	Resultado = num1 + num2
	return Resultado

def resta(num1,num2):
	Resultado = num1 - num2
	return Resultado

def multiplicacion(num1,num2):
	Resultado = num1 * num2
	return Resultado

def division(num1,num2):
	Resultado = num1 / num2
	return Resultado

def Residuo(num1,num2):
	Resultado = mod(num1,num2)
	return Resultado

def bloq(Bloqueados,lista_aux):#funcion que muestra los procesos bloqueados
	posicion = 0
	print("---------------------------------------------")
	print("Bloqueados")   
	for i in Bloqueados:
		print("Id: " + str(i[0]))
		print("Tiempo: " + str(i[13]))
		proceso2 = Bloqueados.pop(posicion)
		nuevo = list(proceso2)
		nuevo[13] += 1  #Tiempo de bloqueo
		nuevo[11] += 1  #Tiempo de espera
		if(nuevo[13] == 8):#si el proceso ya cumplio la espera de 8 lo sacamos
			nuevo[13] == 0 ## en caso de que el proceso vuelva a entrar a bloqueados
			lista_aux.append(nuevo)#lo regresamos a la lista de procesos en ejecucion
			for i in paginas:
				if i[2] == nuevo[0]:
					numpag = i[0]
					del paginas[i[0]]
					paginas.insert(numpag,(numpag,i[1],i[2],"Listo"))
		else:
			Bloqueados.insert(posicion,nuevo)
		posicion += 1


def clean(Bloqueados):
	print ("\033[A                                                                                                               \033[A")
	print ("\033[A                                                                                                               \033[A")
	for i in range(len(Bloqueados)):
		print ("\033[A                                                                                                           \033[A")
		print ("\033[A                                                                                                           \033[A")

#[ID][T_dur][num1][ope][num2][res][T llega][T LLEGADA][T FINALIZADO][T RETORNO][T RESPUESTA][T ESPERA][T SERVICIO][NOSEUTILIZA][Quantum][Tamaño]
# 0     1     2     3    4     5      6        7            8            9           10         11          12         13         14       15
def term(Terminados):#muestra los procesos terminados
	print("---------------------------------------------")
	print("Terminados: ") 
	print("ID \tOP \tRes \tTME \tTL \tTF \tTS \tTE \tTR \tTRES \tTamaño")#tiempo maximo estimado
	lineas = 0
	for i in range(len(Terminados)):
		#resultado = mod(lineas,5)
		print(str(Terminados[i][0]) + "\t" + str(Terminados[i][2]) + str(Terminados[i][3]) + str(Terminados[i][4]) + "\t" + str(Terminados[i][5])+ "\t" + str(Terminados[i][1])  + "\t" + str(Terminados[i][7])+ "\t" + str(Terminados[i][8])+ "\t" + str(Terminados[i][12])+ "\t" + str(Terminados[i][11]) + "\t" + str(Terminados[i][9])+ "\t" + str(Terminados[i][10]) + "\t" + str(Terminados[i][15]))
		lineas = lineas + 1

def borrado(Terminados):
	print ("\033[A                                                                                                           \033[A")
	print ("\033[A                                                                                                           \033[A")
	print ("\033[A                                                                                                           \033[A")
	for i in range(len(Terminados)):
		print ("\033[A                                                                                                          \033[A")

def pag(paginas):
	print("---------------------------------------------")
	print("Paginas: ") 
	print("Marco \tTam \tID \tEstado")
	lineas = 0
	for i in range(len(paginas)):
		print(str(paginas[i][0]) + "\t" + str(paginas[i][1]) + "\t" + str(paginas[i][2]) + "\t" + str(paginas[i][3]))
		lineas = lineas + 1

def pag_borrado(paginas):
	print ("\033[A                                                                                                           \033[A")
	print ("\033[A                                                                                                           \033[A")
	print ("\033[A                                                                                                           \033[A")
	for i in range(len(paginas)):
		print ("\033[A                                                                                                          \033[A")

def llenado(lista, num):
	operadores = ['+','-','*','/','%']
	
	for i in range(num):

		global id 
		id = id + 1	#Definimos el id
		tiempo = random.randint(6, 16)	#generamos un tiempo random del 6 al 16este cambiar este cambiar este cambiar este ca,biaradvcdfsvcsdcvsdcsdcdsc
		num1 = random.randint(1, 10)	#generamos el primer numero
		operador = random.choice(operadores)	#seleccionamos un operador random
		if(operador == '+'):
			num2 = random.randint(0, 10)	#generamos el segundo numero random
			Resultado = suma(num1,num2)
		if(operador == '-'):
			num2 = random.randint(0, 10)	#generamos el segundo numero random
			Resultado = resta(num1,num2)
		if(operador == '*'):
			num2 = random.randint(0, 10)	#generamos el segundo numero random
			Resultado = multiplicacion(num1,num2)
		if(operador == '/'):
			num2 = random.randint(1, 10)	#generamos el segundo numero random
			Resultado = division(num1,num2)
		if(operador == '%'):
			num2 = random.randint(1, 10)	#generamos el segundo numero random
			Resultado = Residuo(num1,num2)
		tamanio = random.randint(5, 26)	#generamos el primer numero
		lista.append((id,tiempo,num1,operador,num2,Resultado,0,0,0,0,0,0,0,0,0,tamanio))
	return num

def actuales(lista_aux,lista):	#aqui mostramos los procesos pendientes en lista pequeña
	longitud= len(lista_aux)
	contador = 0
	system('cls')
	print("Numero de procesos Nuevos: " + str(len(lista)))
	print("Sig.proceso: ID:" + str(lista[0][0]) + "\tTam:" + str(lista[0][15]))
	print("ID \tTME \tTT \tTamaño")
	while (contador < longitud ):
		print(str(lista_aux[contador][0]) + "\t" + str(lista_aux[contador][1]) + "\t" + str(lista_aux[contador][6]) + "\t" + str(lista_aux[contador][15]) )
		proceso1 = lista_aux.pop(contador)
		nuevo = list(proceso1)
		nuevo[11] += 1  #Tiempo de espera
		lista_aux.insert(contador,proceso1) 
		contador = contador + 1
		
def borrAct(lista_aux):
	longitud= len(lista_aux)
	contador = 0
	print ("\033[A                                                                                                           \033[A")
	print ("\033[A                                                                                                           \033[A")
	print ("\033[A                                                                                                           \033[A")
	while (contador < longitud ):
		print ("\033[A                                                                                                           \033[A")
		contador = contador + 1

def main():
	global paginas
	marcos = 46
	lista = []
	lista_aux = []
	Terminados = []
	Bloqueados = []
	correcto = False
	Global = 0
	quantum = 0

	while(not correcto):
		try:
			num = int(input("Introduce el numero de actividades: "))
			correcto = True
		except ValueError:
			print("Error, el numero debe de ser entero")
	correcto = False
	while(not correcto):
		try:
			quantum = int(input("Introduce el Quantum: "))
			correcto = True
		except ValueError:
			print("Error, el numero debe de ser entero")
	llenado(lista,num)
	pendientes = len(lista)
	
	cont = 0
	system('cls')
	longitud= len(lista)
	while (marcos > 0 and cont < longitud):	#agrega las primeras 5 llegadas de proceso
		operacion = ceil(lista[cont][15] / 4)
		tamaux = lista[cont][15]
		if operacion <= marcos:
			while(tamaux != 0):
				for i in paginas:
					if i[3] == "libre":
						num = i[0]
						del paginas[i[0]]
						if tamaux >= 4:
							paginas.insert(i[0],(num,0,lista[cont][0],"listo"))
							tamaux = tamaux - 4
							if(tamaux == 0):
								marcos -= 1
								break
							marcos -= 1
						else:
							tamaux = 4 - tamaux
							paginas.insert(i[0],(num,tamaux,lista[cont][0],"listo"))
							tamaux = 0
							marcos -= 1
							break
			nueva = list(lista[cont])
			nueva[7] = Global                ##Tiempo de llegada 
			lista_aux.append(nueva)
			cont= cont + 1
		else:
			break
	for i in range(cont):
		lista.pop(0)
		pendientes = pendientes - 1
			
	print("Numero de procesos Nuevos: " + str(len(lista)))
	print("ID \tTME")
	print("---------------------------------------------")
	print("***\nNombre:\n Op: \nId: \nTME: \nTT: \nTR: ")
	print("---------------------------------------------")
	print("Terminados: ") 
	print("ID \tOP \tRes")
	print("---------------------------------------------")
	banBloqueo = False

	while(len(lista_aux) != 0 or banBloqueo == True):	#a partir de aqui ejecuta los procesos
		proceso = lista_aux.pop(0)
		longitud= len(lista_aux)
		contador = 0
		system('cls')
		print("Numero de procesos Nuevos: " + str(len(lista)))
		print(lista[0])
		print("ID \tTME \tLlegada")
		while (contador < longitud ):
			print(str(lista_aux[contador][0]) + "\t" + str(lista_aux[contador][1]) + "\t" + str(lista_aux[contador][7]))
			proceso1 = lista_aux.pop(contador)
			nuevo = list(proceso1)
			nuevo[11] += 1 
			lista_aux.insert(contador,proceso1) 
			contador = contador + 1
		print("---------------------------------------------")
			
		TR = proceso[1]-proceso[6]
		TT = proceso[6]
			
		if( marcos > 0 and len(lista) > 0 ):
			operacion = ceil(lista[0][15] / 4)
			tamaux = lista[0][15]
			if operacion <= marcos:	
				while(tamaux != 0):
					for i in paginas:
						if i[3] == "libre":
							num = i[0]
							del paginas[i[0]]
							if tamaux >= 4:
								paginas.insert(i[0],(num,0,lista[0][0],"listo"))
								tamaux = tamaux - 4
								if(tamaux == 0):
									marcos -= 1
									break
								marcos -= 1
							else:
								tamaux = 4 - tamaux
								paginas.insert(i[0],(num,tamaux,lista[0][0],"listo"))
								tamaux = 0
								marcos -= 1
								break
				nueva = list(lista[0])
				nueva[7] = Global
				lista_aux.append(nueva)
				cont= cont + 1
				lista.pop(0)
				pendientes = pendientes - 1 

		while TR != -1:
			actuales(lista_aux,lista)
			tecla = msvcrt.kbhit() and (msvcrt.getwch())
				
			if (tecla == 'i'):
				print("Bloqueados")
				time.sleep(1)
				nueva = list(proceso)
				nueva[6] = TT
				nueva[13] = 0
				Bloqueados.append(nueva)
				banBloqueo = True
				if len(lista_aux) == 0 and len(Bloqueados) > 0:
					print("Proceso Nulo")
					llenado(lista,1)
					nueva = list(lista[0])
					nueva[7] = Global
					nueva[1] = 8 - Bloqueados[0][13]
					nueva[0] = 0
					lista_aux.append(nueva)
					cont= cont + 1
					lista.pop(0)
					pendientes = pendientes - 1
					time.sleep(1)
				for i in paginas:
					if i[2] == nueva[0]:
						numpag = i[0]
						del paginas[i[0]]
						paginas.insert(numpag,(numpag,i[1],i[2],"Bloq."))
				break
				
			elif (tecla == 'e'):
				if( marcos > 0 and len(lista) > 0 ):
					operacion = ceil(lista[0][15] / 4)
					tamaux = lista[0][15]
					if operacion <= marcos:	
						while(tamaux != 0):
							for i in paginas:
								if i[3] == "libre":
									num = i[0]
									del paginas[i[0]]
									if tamaux >= 4:
										paginas.insert(i[0],(num,0,lista[0][0],"listo"))
										tamaux = tamaux - 4
										if(tamaux == 0):
											marcos -= 1
											break
										marcos -= 1
									else:
										tamaux = 4 - tamaux
										paginas.insert(i[0],(num,tamaux,lista[0][0],"listo"))
										tamaux = 0
										marcos -= 1
										break
						nueva = list(lista[0])
						nueva[7] = Global
						lista_aux.append(nueva)
						cont= cont + 1
						lista.pop(0)
						pendientes = pendientes - 1 
				nueva = list(proceso)
				nueva[5] = 'Error'
				nueva[8] = Global -1  #Tiempo de finalizado para procesoque termino
				nueva[9] = nueva[8] + nueva[7]  #Tiempo de retorno
				nueva[12] = TT
				Terminados.append(nueva)
				for i in paginas:
					if i[2] == nueva[0]:
						numpag = i[0]
						del paginas[i[0]]
						paginas.insert(numpag,(numpag,4,0,"libre"))
						marcos += 1
				cont = cont - 1
				break
			
			elif (tecla == 'n'):
				print("Nuevo")
				llenado(lista,1)
				
				if( marcos > 0 and len(lista) > 0 ):
					operacion = ceil(lista[0][15] / 4)
					tamaux = lista[0][15]
					if operacion <= marcos:
						while(tamaux != 0):
							for i in paginas:
								if i[3] == "libre":
									num = i[0]
									del paginas[i[0]]
									if tamaux >= 4:
										paginas.insert(i[0],(num,0,lista[0][0],"listo"))
										tamaux = tamaux - 4
										if(tamaux == 0):
											marcos -= 1
											break
										marcos -= 1
									else:
										tamaux = 4 - tamaux
										paginas.insert(i[0],(num,tamaux,lista[0][0],"listo"))
										tamaux = 0
										break
									marcos -= 1
						nueva = list(lista[0])
						nueva[7] = Global
						lista_aux.append(nueva)
						cont= cont + 1
						lista.pop(0)
						pendientes = pendientes - 1 
				
			print("Proceso en ejecucion")
			if(proceso[10] == 0):	##tiempo de respuesta
				proceso[10] = Global - proceso[7]
				proceso[11] += proceso[10]  ##Tiempo de espera 
				
			print("Op: " + str(proceso[2]) + " " + str(proceso[3]) + " " + str(proceso[4])) 
			print("Id: " + str(proceso[0])) 
			print("TME: " + str(proceso[1])) 
			print("TT: " + str(TT)) 
			print("TR: " + str(TR))
			for i in paginas:
				if i[2] == proceso[0]:
					numpag = i[0]
					del paginas[i[0]]
					paginas.insert(numpag,(numpag,i[1],i[2],"Ejec."))
			bloq(Bloqueados,lista_aux)
			term(Terminados)
			pag(paginas)
				
			if (tecla == 'p' or tecla == 'a'):
				siguiente = False
				print('Pausa')
				time.sleep(1)
				while(not siguiente):
					try: 
						if (msvcrt.kbhit() and (msvcrt.getwch() == 'c')):
							siguiente = True
						else:continue
					except ValueError:
						print('Pausa')
						time.sleep(2)
						print ("\033[A                                                                                                           \033[A")
						
			if (tecla == 't'):
				system('cls')
				siguiente = False
				print('BCP')
				print("Tabla de Procesos")
				print("----------------------------------------------------------------------------------------------------------------------")
				print("Id"+"\tOper"+"\tResp"+"\tTME"+"\tT.Lleg"+"\tT.Fin"+ "\tT.Ret"+"\tT.Esp" +"\tT.Serv" +"\tTR" +"\tT.Res" +"\tT.Bloq")
				print("----------------------------------------------------------------------------------------------------------------------")
				print("Nuevos")
				print("----------------------------------------------------------------------------------------------------------------------")
				for i in lista:
					print(str(i[0])+"\t "+str(i[2])+str(i[3])+str(i[4])+"\t --"+"\t "+str(i[1])+"\t --" +"\t --"+"\t --"+"\t --"+"\t --" +"\t --"+"\t --"+"\t --")
				print("----------------------------------------------------------------------------------------------------------------------")
				print("Listos")
				print("----------------------------------------------------------------------------------------------------------------------")
				for i in lista_aux:
					print(str(i[0])+"\t "+str(i[2])+str(i[3])+str(i[4])+"\t --"+"\t "+str(i[1])+"\t "+str(i[7])+"\t --"+"\t --"+"\t "+str(Global-i[7]-i[6])+"\t "+str(i[6])+"\t "+str(i[1]-i[6])+"\t "+str(i[10])+"\t --")
				print("----------------------------------------------------------------------------------------------------------------------")
				print("Ejecucion")
				print("----------------------------------------------------------------------------------------------------------------------")
				print(str(proceso[0])+"\t "+str(proceso[2])+str(proceso[3])+str(proceso[4])+"\t --"+"\t "+str(proceso[1])+"\t "+str(proceso[7])+"\t --"+"\t --"+"\t "+str(proceso[11])+"\t "+str(proceso[6]) +"\t "+str(proceso[1]-proceso[6])+"\t "+str(proceso[10])+"\t --")
				print("----------------------------------------------------------------------------------------------------------------------")
				print("Bloqueados")
				print("----------------------------------------------------------------------------------------------------------------------")
				for i in Bloqueados:
					print(str(i[0])+"\t "+str(i[2])+str(i[3])+str(i[4])+"\t --"+"\t "+str(i[1])+"\t "+str(i[7])+"\t --"+"\t --"+"\t "+str(Global-i[7]-i[6])+"\t "+str(i[6]) +"\t "+str(i[1]-i[6])+"\t "+str(i[10])+"\t "+str(i[13]))
				print("----------------------------------------------------------------------------------------------------------------------")
				print("Terminados")
				print("----------------------------------------------------------------------------------------------------------------------")
				for i in Terminados:
					print(str(i[0])+"\t "+str(i[2])+str(i[3])+str(i[4])+"\t "+str(i[5])+"\t "+str(i[1])+"\t "+str(i[7])+"\t "+str(i[8])+"\t "+str(i[9])+"\t "+str(i[11])+"\t "+str(i[12]) +"\t "+str(i[1]-i[6])+"\t "+str(i[10])+"\t --")
				
				time.sleep(1)
				while(not siguiente):
					try: 
						if (msvcrt.kbhit() and (msvcrt.getwch() == 'c')):
							siguiente = True
						else:continue
					except ValueError:
						print('Pausa')
						time.sleep(2)
						print ("\033[A                                                                                                           \033[A")
				
			time.sleep(2)
			borrAct(lista_aux)
			print ("\033[A                                                                                                           \033[A")
			print ("\033[A                                                                                                           \033[A")
			print ("\033[A                                                                                                           \033[A") 
			print ("\033[A                                                                                                           \033[A")
			print ("\033[A                                                                                                           \033[A")
			print ("\033[A                                                                                                           \033[A")
			clean(Bloqueados)
			borrado(Terminados)
			pag_borrado(paginas)

			Global = Global +1 
			TT = TT + 1
			TR = TR - 1
			proceso[14] = proceso[14] + 1
			if(proceso[14] == quantum):
				for i in paginas:
					if i[2] == proceso[0]:
						numpag = i[0]
						del paginas[i[0]]
						paginas.insert(numpag,(numpag,i[1],i[2],"Listo"))
				proceso[14] = 0
				proceso[6] = TT
				lista_aux.append(proceso);
				break
				
		if(TR == -1):
			if( marcos > 0 and len(lista) > 0 ):
				operacion = ceil(lista[0][15] / 4)
				tamaux = lista[0][15]
				print("operacion: ",operacion)
				print("marcos: ",marcos)
				print("proceso: ",lista[0][0])
				if operacion <= marcos:	
					while(tamaux != 0):
						for i in paginas:
							if i[3] == "libre":
								num = i[0]
								del paginas[i[0]]
								if tamaux >= 4:
									paginas.insert(i[0],(num,0,lista[0][0],"listo"))
									tamaux = tamaux - 4
									if(tamaux == 0):
										marcos -= 1
										break
									marcos -= 1
								else:
									tamaux = 4 - tamaux
									paginas.insert(i[0],(num,tamaux,lista[0][0],"listo"))
									tamaux = 0
									marcos -= 1
									break
					proceso3 = lista.pop(0)
					nueva = list(proceso3)
					nueva[7] = Global       #Tiempo de llegada para nuevo proceso
					lista_aux.append(nueva)
					cont= cont + 1
					pendientes -= 1
					print(lista[0])
					system('pause')
					print ("\033[A                                                                                                           \033[A")
					print ("\033[A                                                                                                           \033[A")
					print ("\033[A                                                                                                           \033[A")
					print ("\033[A                                                                                                           \033[A")

	
			nueva = list(proceso)
			nueva[8] = Global  - 1	 #Tiempo de finalizado para procesoque termino---------------------aqui
			nueva[9] = nueva[8] - nueva[7] 	 #Tiempo de retorno                            -   aqui
			nueva[12] = nueva[1] 	#Tiempo de servicio
			Terminados.append(nueva)

			for i in paginas:
				if i[2] == nueva[0]:
					numpag = i[0]
					del paginas[i[0]]
					paginas.insert(numpag,(numpag,4,0,"libre"))
					marcos += 1
			cont = cont - 1
		
		if(len(Bloqueados) == 0 and len(lista_aux) == 0):
			banBloqueo = False
			if proceso[0] == num:
				term(Terminados)
				system("pause")
				break
		else:
			banBloqueo = True
			if len(lista_aux) == 0 and len(Bloqueados) > 0:
				print("Proceso Nulo")
				llenado(lista,1)
				nueva = list(lista[0])
				nueva[7] = Global
				nueva[1] = 8 - Bloqueados[0][13]
				nueva[0] = 0
				lista_aux.append(nueva)
				cont= cont + 1
				lista.pop(0)
				pendientes = pendientes - 1
				time.sleep(1)
		
	print("Tiempo total de ejecucion: " + str(Global))
	for i in range(len(Terminados)):
		print(Terminados[i])
main()