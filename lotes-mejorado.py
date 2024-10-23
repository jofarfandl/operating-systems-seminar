from operator import mod
from os import system
import string
import math
import sys
from time import time
import time
from turtle import Terminator

def menu():
    print("1.-Suma")
    print("2.-Resta")
    print("3.-Multiplicacion")
    print("4.-Division")
    print("5.-Residuo")
    print("6.-Salida")
    op = 0
    while(op == 0):
        op = int(input("Introduce la opcion: "))
        if op < 7 and op > 0:
            return op #retornamos la operacion seleccionada
        else: 
            op = 0
            
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

def actual():
    print("Proceso en ejecucion")
    print("Nombre: ")  
    print("Op: ") 
    print("Id: ") 
    print("TME: ")
    print("TT: ") 
    print("TR: ") 

def term(Terminados):
    actual()
    print("---------------------------------------------")
    print("Terminados: ") 
    print("ID \tOP \tRes")
    for i in range(len(Terminados)):
                print(str(Terminados[i][1]) + "\t" + str(Terminados[i][3]) + str(Terminados[i][4]) +str(Terminados[i][5]) + "\t" + str(Terminados[i][6]))

def main():
    cont_global = 0 #variable que contendra el tiempo total
    lista = []
    lista_aux = []
    ids = set()
    correcto = False
    while(not correcto):
        try:
            num = int(input("Introduce el numero de actividades: "))#Ingresamos la cantidad de entradas totales
            correcto = True
        except ValueError:#solo numeros enteros
            print("Error, el numero debe de ser entero")
    for i in range(num):#repetimos para ingresar todos los datos
        correcto = False
        nombre = str(input("Ingrese Nombre: "))
        while(not correcto):#funcion para verificar que lso ids no se repitan
                id = int(input("Introduce el ID: "))
                if id not in ids:
                    ids.add(id)
                    correcto = True
                else:
                    print("Error, el id ya existe")
        tiempo = 0
        while(tiempo == 0):
            tiempo = int(input("Introduce el tiempo: "))
            if tiempo > 0:#Verificamos que el tiempo sea valido
                #cont_global = cont_global + tiempo#Incrementamos el total del timepo--
                continue 
            else:
                print("Error, no puede ser menor o igual a 0")
                tiempo = 0

        op = menu() #guardamos el tipo de operacion
        if op == 1:#seleccionamos la operacion correspondiente
            num1 = int(input("Numero1: "))
            num2 = int(input("Numero2: "))
            operador = '+'
            Resultado  = suma(num1,num2)
        elif op == 2:
            num1 = int(input("Numero1: "))
            num2 = int(input("Numero2: "))
            operador = '-'
            Resultado  = resta(num1,num2)
        elif op == 3:
            num1 = int(input("Numero1: "))
            num2 = int(input("Numero2: "))  
            operador = '*' 
            Resultado  = multiplicacion(num1,num2)
        elif op == 4:
            num1 = int(input("Numero1: "))
            num2 = 0
            while(num2 == 0):
                num2 = int(input("Numero2: ")) 
                if num2 == 0:#verificamos que no se ingrese un numero 0
                    print("No se puede dividir 0")
            operador = '/'
            Resultado  = division(num1,num2)
        elif op == 5:
            num1 = int(input("Numero1: "))
            num2 = 0
            while(num2 == 0):
                num2 = int(input("Numero2: ")) 
                if num2 == 0:#verificamos que no se ingrese un numero 0
                    print("No se puede dividir 0")
            operador = '%'
            Resultado  = Residuo(num1,num2)
        lista.append((nombre,id,tiempo,num1,operador,num2,Resultado))#agregamos los datos a nuestra lista
    
    cont_lotes = 1
    pendientes = math.ceil((num/5) - cont_lotes) #redondeamos para crear la cantidad total de lotes
    van = 1
    #-----------------------------------------------------------------------------
    while pendientes >= 0:#bucle que recorrera los lotes uno por uno
        Terminados = [] #aqui guardaremos los datos de las operaciones ya realizadas
        cont = 0
        system('cls')
        print("Numero de lotes pendiente: " + str(pendientes))
        print("\nLote en ejecucion: ",van)#mostramos el numero de lote en el ue va
        print("ID \tTME")
        longitud= len(lista)
        while (cont < 5 and cont < longitud):
            print(str(lista[cont][1]) + "\t" + str(lista[cont][2]))#mostramos el id y el tiempo de cada proceso
            lista_aux.append(lista[cont])#guardamos los datos de reconocimiento en una nueva lista
            cont= cont + 1
        for i in range(cont):
            lista.pop(0)#quitamos datos que ya no ocupamos
        #print("---------------------------------------------")
        actual()#mostramos el lote actual en ejecucion
        print("---------------------------------------------")
        print("Procesos Terminados: ") 
        print("ID \tOP \tRes")
        print("---------------------------------------------")
        system('pause')
        for i in range(len(lista_aux)):
            proceso = lista_aux.pop(0)#guardamos los datos de la operacion que se empezara a ejecutar
            longitud= len(lista_aux)
            contador = 0
            system('cls')
            
            print("Lote Actual: ",van)
            print("ID \tTME")
            while (contador < longitud ):#mostramos las operaciones restantes
                print(str(lista_aux[contador][1]) + "\t" + str(lista_aux[contador][2]))
                contador = contador + 1
            print("---------------------------------------------")
            longitud = longitud - 1 #disminuimos un proceso
            TR = proceso[2] # extraemos el timempo de la operacion
            TT = 0 #definimos el tiempo que ha avanzado
            while TR != -1:#ciclo para cuenta regresiva de proceso
                print("Contador global: ",cont_global)
                print("Proceso en ejecucion")   #mostramos los datos del procesos
                print("Nombre: " + str(proceso[0]))  
                print("Op: " + str(proceso[3]) + " " + str(proceso[4]) + " " + str(proceso[5])) 
                print("Id: " + str(proceso[1])) 
                print("TME: " + str(proceso[2])) 
                print("TT: " + str(TT)) 
                print("TR: " + str(TR))
                time.sleep(1)
                print ("\033[A                             \033[A")
                print ("\033[A                             \033[A")
                print ("\033[A                             \033[A") #para despistar al enemigo
                print ("\033[A                             \033[A")
                print ("\033[A                             \033[A")
                print ("\033[A                             \033[A")
                print ("\033[A                             \033[A")
                print ("\033[A                             \033[A")
                TT = TT + 1#incrementamos el timepo transucrrido
                TR = TR - 1#decrementamos 1 al tiempo restante
                cont_global = cont_global + 1
            Terminados.append(proceso)#agregamos el proceso a los terminados
            term(Terminados)#imprimimos los procesos terminados
            print("contador global: ",cont_global)
            system('pause')
        pendientes = pendientes - 1 #dsminuimos a pendientes un proceso
        van = van + 1
main()