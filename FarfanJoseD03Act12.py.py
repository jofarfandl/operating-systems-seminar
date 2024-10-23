import msvcrt
from operator import mod
import time
import random
posicionP = 0
posicionC = 0
lista = []

def imprimir():
	for i in range(len(lista)):
		print(lista[i], end="\t")
	print("\n1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20")
	time.sleep(2)
	print ("\033[A                                                                                                                                                            \033[A")
	print ("\033[A                                                                                                                                                            \033[A")
	print ("\033[A                                                                                                                                                            \033[A")
	print ("\033[A                                                                                                                                                            \033[A")

def disponibilidad(disponible):
	for i in range(len(lista)):
		if(lista[i] != '-'):
			disponible = disponible + 1
	return disponible

def productor():
	print("Consumidor: Dormido")
	print("Productor: Despierto")
	global posicionP
	disponible = 0
	dis = disponibilidad(disponible)
	if(dis < 20):
		if(posicionP == 20):
			posicionP = 0
		num = genCon()
		if(dis+num < 20):
			print ("\033[A                                                                                                                                \033[A")
			print("Productor: Produciendo")
			for i in range(num):
				if(posicionP == 20):
					posicionP = 0
				lista[posicionP] = posicionP
				posicionP = posicionP + 1
		else:
			restante = 20 - dis
			print ("\033[A                                                                                                                                \033[A")
			print("Productor: Produciendo")
			for i in range(restante):
				if(posicionP == 20):
					posicionP = 0
				lista[posicionP] = posicionP
				posicionP = posicionP + 1
	imprimir()

def consumidor():
	print("Productor: Dormido")
	print("Consumidor: Despierto")
	time.sleep(1)
	global posicionC
	disponible = 0
	dis = disponibilidad(disponible)
	if(dis > 0):
		if(posicionC == 20):
			posicionC = 0
		num = genCon()
		if(dis-num > 0):
			print ("\033[A                                                                                                                                \033[A")
			print("Consumidor: Consumiendo")
			for i in range(num):
				if(posicionC == 20):
					posicionC = 0
				lista[posicionC] = '-'
				##lista.remove(posicionC)
				posicionC = posicionC + 1
		else:
			restante = dis
			print ("\033[A                                                                                                                                \033[A")
			print("Consumidor: Consumiendo")
			for i in range(restante):
				if(posicionC == 20):
					posicionC = 0
				lista[posicionC] = '-'
				##lista.remove(posicionC)
				posicionC = posicionC + 1
	imprimir()

def genNumero():
	numero = random.randint(1, 20)
	return numero
def genCon():
	numero = random.randint(2, 5)
	return numero

def main():
	global lista
	lista = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
	tecla = 'a'
	while(tecla != b'\x1b'):
		tecla = msvcrt.kbhit() and (msvcrt.getch())
		azar = genNumero()
		decision = mod(azar,2)
		##print(decision)
		time.sleep(1)

		if(decision == 0):
			productor()
		else:
			consumidor()
	if(tecla == b'\x1b'):
		print("Terminado.....")
main()