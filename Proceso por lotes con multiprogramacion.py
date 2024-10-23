from operator import mod
from os import system, terminal_size
import string
import math
from time import time
import time
import msvcrt
import random

            
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

def term(Terminados):
    print("---------------------------------------------")
    print("Terminados: ") 
    print("ID \tOP \tRes \tLote")
    lineas = 0
    for i in range(len(Terminados)):
        print(str(Terminados[i][0]) + "\t" + str(Terminados[i][2]) + str(Terminados[i][3]) +str(Terminados[i][4]) + "\t" + str(Terminados[i][5]) + "\t" + str(Terminados[i][7]))
        lineas = lineas + 1

def borrado(Terminados):
    print ("\033[A                                                         \033[A")
    print ("\033[A                                                         \033[A")
    print ("\033[A                                                         \033[A")
    for i in range(len(Terminados)):
        print ("\033[A                                                        \033[A")

def llenado(lista, num):
    operadores = ['+','-','*','/','%']
    for i in range(num):
        id = int(i+1)#Definimos el id
        tiempo = random.randint(6, 16)#generamos un tiempo random del 6 al 16este cambiar este cambiar este cambiar este ca,biaradvcdfsvcsdcvsdcsdcdsc
        num1 = random.randint(1, 10)#generamos el primer numero
        operador = random.choice(operadores)#seleccionamos un operador random
        if(operador == '+'):
            num2 = random.randint(0, 10)#generamos el segundo numero random
            Resultado = suma(num1,num2)
        if(operador == '-'):
            num2 = random.randint(0, 10)#generamos el segundo numero random
            Resultado = resta(num1,num2)
        if(operador == '*'):
            num2 = random.randint(0, 10)#generamos el segundo numero random
            Resultado = multiplicacion(num1,num2)
        if(operador == '/'):
            num2 = random.randint(1, 10)#generamos el segundo numero random
            Resultado = division(num1,num2)
        if(operador == '%'):
            num2 = random.randint(1, 10)#generamos el segundo numero random
            Resultado = Residuo(num1,num2)
        lista.append((id,tiempo,num1,operador,num2,Resultado,0))
    return num


def main():
    lista = []
    lista_aux = []
    Terminados = []
    correcto = False
    Global = 0

    while(not correcto):
        try:
            num = int(input("Introduce el numero de actividades: "))
            correcto = True
        except ValueError:
            print("Error, el numero debe de ser entero")
    llenado(lista,num)
    cont_lotes = 1
    pendientes = math.ceil((num/5) - cont_lotes)
    van = 1

    while pendientes >= 0:
        cont = 0
        system('cls')
        print("Numero de lotes pendiente: " + str(pendientes))
        print("Lote Actual" + str(van))
        print("ID \tTME")
        longitud= len(lista)
        while (cont < 5 and cont < longitud):
            print(str(lista[cont][0]) + "\t" + str(lista[cont][1]))
            lista_aux.append(lista[cont])
            cont= cont + 1
        for i in range(cont):
            lista.pop(0)
        print("---------------------------------------------")
        print("***\nNombre:\n Op: \nId: \nTME: \nTT: \nTR: ")
        print("---------------------------------------------")
        print("Terminados: ") 
        print("ID \tOP \tRes")
        print("---------------------------------------------")

        for i in range(len(lista_aux)):#a partir de aqui ejecuta los lotes
            proceso = lista_aux.pop(0)
            longitud= len(lista_aux)
            contador = 0
            system('cls')
            print("Lote Actual: " + str(van))
            print("ID \tTME")
            while (contador < longitud ):
                print(str(lista_aux[contador][0]) + "\t" + str(lista_aux[contador][1]))
                contador = contador + 1
            print("---------------------------------------------")
            longitud = longitud - 1
            TR = proceso[1]-proceso[6]
            TT = proceso[6]

            while TR != -1:
                tecla = msvcrt.kbhit() and (msvcrt.getwch())
                if (tecla == 'i'):
                    print("interrupcion")
                    time.sleep(2)
                    nueva = list(proceso)
                    nueva[6] = TT
                    print(nueva[6])
                    lista_aux.append(nueva)
                    longitud = longitud + 1
                    break
                elif (tecla == 'e'):
                    nueva = list(proceso)
                    nueva[5] = 'Error'
                    print(nueva[5])
                    nueva.append(van)
                    Terminados.append(nueva)
                    break
                elif (tecla == 'p'):
                    siguiente = False
                    print('Pausa')
                    time.sleep(2)
                    print ("\033[A                                                          \033[A")
                    while(not siguiente):
                        try: 
                            if (msvcrt.kbhit() and (msvcrt.getwch() == 'c')):
                                siguiente = True
                            else:continue
                        except ValueError:
                            print('Pausa')
                            time.sleep(2)
                            print ("\033[A                                                         \033[A")
                print("Proceso en ejecucion")    
                print("Op: " + str(proceso[2]) + " " + str(proceso[3]) + " " + str(proceso[4])) 
                print("Id: " + str(proceso[0])) 
                print("TME: " + str(proceso[1])) 
                print("TT: " + str(TT)) 
                print("TR: " + str(TR))
                term(Terminados)
                time.sleep(2)
                print ("\033[A                                                         \033[A")
                print ("\033[A                                                         \033[A")
                print ("\033[A                                                         \033[A") 
                print ("\033[A                                                         \033[A")
                print ("\033[A                                                         \033[A")
                print ("\033[A                                                         \033[A")
                borrado(Terminados)
                Global = Global +1 
                TT = TT + 1
                TR = TR - 1
            if(TR == -1):
                nueva = list(proceso)
                nueva.append(van)
                Terminados.append(nueva)
            if proceso[0] == num:
                term(Terminados)
                system("pause")
                break
        pendientes = pendientes - 1
        van = van + 1
    print("Tiempo total de ejecucion: " + str(Global))
main()