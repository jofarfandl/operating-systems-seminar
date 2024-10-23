from operator import mod
from os import system#, terminal_size
#import string
#import math
from time import time
import time
import msvcrt
import random

id = 0

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
        else:
            Bloqueados.insert(posicion,nuevo)
        posicion += 1


def clean(Bloqueados):
    print ("\033[A                                                                                                               \033[A")
    print ("\033[A                                                                                                               \033[A")
    for i in range(len(Bloqueados)):
        print ("\033[A                                                                                                           \033[A")
        print ("\033[A                                                                                                           \033[A")

#[ID][T_dur][num1][ope][num2][res][T llega][T LLEGADA][T FINALIZADO][T RETORNO][T RESPUESTA][T ESPERA][T SERVICIO][NOSEUTILIZA]
# 0     1     2     3    4     5      6        7            8            9           10         11          12         13
def term(Terminados):#muestra los procesos terminados
    print("---------------------------------------------")
    print("Terminados: ") 
    print("ID \tOP \tRes \tTME \tTL \tTF \tTS \tTE \tTR \tTRES")#tiempo maximo estimado
    lineas = 0
    for i in range(len(Terminados)):
        #resultado = mod(lineas,5)
        print(str(Terminados[i][0]) + "\t" + str(Terminados[i][2]) + str(Terminados[i][3]) + str(Terminados[i][4]) + "\t" + str(Terminados[i][5])+ "\t" + str(Terminados[i][1])  + "\t" + str(Terminados[i][7])+ "\t" + str(Terminados[i][8])+ "\t" + str(Terminados[i][12])+ "\t" + str(Terminados[i][11]) + "\t" + str(Terminados[i][9])+ "\t" + str(Terminados[i][10]))
        lineas = lineas + 1

def borrado(Terminados):
    print ("\033[A                                                                                                                                    \033[A")
    print ("\033[A                                                                                                                                  \033[A")
    print ("\033[A                                                                                                                                       \033[A")
    for i in range(len(Terminados)):
        print ("\033[A                                                                                                          \033[A")

def llenado(lista, num):
    operadores = ['+','-','*','/','%']
    
    for i in range(num):

        global id 
        id = id + 1#Definimos el id
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
        lista.append((id,tiempo,num1,operador,num2,Resultado,0,0,0,0,0,0,0,0))
    return num

def actuales(lista_aux,lista):#aqui mostramos los procesos pendientes en lista pequeña
    longitud= len(lista_aux)
    contador = 0
    system('cls')
    print("Numero de procesos pendiente: " + str(len(lista)))
    print("ID \tTME \tLlegada")
    while (contador < longitud ):
        print(str(lista_aux[contador][0]) + "\t" + str(lista_aux[contador][1]) + "\t" + str(lista_aux[contador][7]))
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
    while (contador < longitud ):
        print ("\033[A                                                                                                           \033[A")
        contador = contador + 1

def main():
    lista = []#lista la cual contiene todos los procesos
    lista_aux = []#procesos activos (5)
    Terminados = []#lista de procesos que ya se terminarion
    Bloqueados = []#lista de procesos que estan bloqueados
    correcto = False
    Global = 0

    while(not correcto):
        try:
            num = int(input("Introduce el numero de actividades: "))
            correcto = True
        except ValueError:
            print("Error, el numero debe de ser entero")
    llenado(lista,num)
    ##cont_lotes = 1
    pendientes = len(lista)
    
    cont = 0
    system('cls')
    longitud= len(lista)
    while (cont < 5 and cont < longitud):#agrega las primeras 5 llegadas de proceso
        print(str(lista[cont][0]) + "\t" + str(lista[cont][1]))
        nueva = list(lista[cont])
        nueva[7] = Global##Tiempo de llegada 
        lista_aux.append(nueva)
        cont= cont + 1
    for i in range(cont):
        lista.pop(0)
        pendientes = pendientes - 1
            
    print("Numero de procesos pendiente: " + str(len(lista)))#mostramos los procesos pendientes
    print("ID \tTME")
    print("---------------------------------------------")
    print("***\nNombre:\n Op: \nId: \nTME: \nTT: \nTR: ")
    print("---------------------------------------------")
    print("Terminados: ") 
    print("ID \tOP \tRes")
    print("---------------------------------------------")
    banBloqueo = False

    while(len(lista_aux) != 0 or banBloqueo == True):#a partir de aqui ejecuta los procesos
        memoria = 0
        proceso = lista_aux.pop(0)
        longitud= len(lista_aux)
        contador = 0
        system('cls')
            
        print("Numero de procesos pendiente: " + str(len(lista)))#muestra la primera parte de los procesos
        print("ID \tTME \tLlegada")
        while (contador < longitud ):
            print(str(lista_aux[contador][0]) + "\t" + str(lista_aux[contador][1]) + "\t" + str(lista_aux[contador][7]))
            proceso1 = lista_aux.pop(contador)
            nuevo = list(proceso1)
            nuevo[11] += 1  #Tiempo de espera---------------------------------------------------------------------------aqui inicia con 1 esta mal eso
            lista_aux.insert(contador,proceso1) 
            contador = contador + 1
        print("---------------------------------------------")
            
        TR = proceso[1]-proceso[6]
        TT = proceso[6]
            
        memoria = len(lista_aux) + len(Bloqueados) + 1
        print("memoria: "+ str(memoria))
        
        if( memoria < 5 and len(lista) > 0 ):#si los procesos en ejecucion son menor a 5 y aun quedan procesos se agrega un nuevo proceso a los procesos en ejecucion
            nueva = list(lista[0])
            nueva[7] = Global
            lista_aux.append(nueva)
            cont= cont + 1
            lista.pop(0)
            pendientes = pendientes - 1 

        while TR != -1: #mientras el tiempo restante no sea igual a -1 el proceso no se ha terminado y se seguira ejecutando
            actuales(lista_aux,lista)
            tecla = msvcrt.kbhit() and (msvcrt.getwch())#implementamos las condiciones que validan las funciones de las teclas
                
            if (tecla == 'i'):#manda un proceso a bloqueados
                print("Bloqueados")
                time.sleep(1)
                nueva = list(proceso)
                nueva[6] = TT
                nueva[13] = 0
                Bloqueados.append(nueva)
                banBloqueo = True
                break
                
            elif (tecla == 'e'):#finaliza un proceso con un error
                if len(lista) != 0:
                    nueva = list(lista[0])
                    nueva[7] = Global
                    lista_aux.append(nueva)
                    cont= cont + 1
                    lista.pop(0)
                nueva = list(proceso)
                nueva[5] = 'Error'
                nueva[8] = Global -1  #Tiempo de finalizado para procesoque termino
                nueva[9] = nueva[8] + nueva[7]  #Tiempo de retorno
                nueva[12] = TT
                Terminados.append(nueva)
                cont = cont - 1
                break
            
            elif (tecla == 'n'):#Agrega un nuevo proceso a nuestra lista grande
                print("Nuevo")
                llenado(lista,1)
                memoria = len(lista_aux) + len(Bloqueados) + 1
                print("memoria: "+ str(memoria))
                
                if( memoria < 5 and len(lista) > 0 ):
                    nueva = list(lista[0])
                    nueva[7] = Global
                    lista_aux.append(nueva)
                    cont= cont + 1
                    lista.pop(0)
                    pendientes = pendientes - 1 
                
            print("Proceso en ejecucion")
            if(proceso[10] == 0):##tiempo de respuesta
                proceso[10] = Global - proceso[7]
                proceso[11] += proceso[10]  ##Tiempo de espera 
            print("Op: " + str(proceso[2]) + " " + str(proceso[3]) + " " + str(proceso[4])) 
            print("Id: " + str(proceso[0])) 
            print("TME: " + str(proceso[1])) 
            print("TT: " + str(TT)) 
            print("TR: " + str(TR))
            bloq(Bloqueados,lista_aux)
            term(Terminados)
                
            if (tecla == 'p'):#pausamos el programa
                siguiente = False
                print('Pausa')
                time.sleep(1)
                ##print ("\033[A                                                          \033[A")
                while(not siguiente):#validamos que mientras no se presione la c el programa no continua
                    try: 
                        if (msvcrt.kbhit() and (msvcrt.getwch() == 'c')):
                            siguiente = True
                        else:continue
                    except ValueError:
                        print('Pausa')
                        time.sleep(2)
                        print ("\033[A                                                                                                           \033[A")
                        
            if (tecla == 't'):#mostramos la tabla de los procesos
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
                ##print ("\033[A                                                          \033[A")
                while(not siguiente):
                    try: 
                        if (msvcrt.kbhit() and (msvcrt.getwch() == 'c')):#ocupamos presionar c para dejar de ver la tabla
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
            #print ("\033[A                                                         \033[A")
            clean(Bloqueados)
            borrado(Terminados)

            Global = Global +1 
            TT = TT + 1
            TR = TR - 1
        if(TR == -1):#si el proceso termino se agrega un nuevo proceso a los procesos en ejecucion
            if len(lista) != 0:
                proceso3 = lista.pop(0)
                nueva = list(proceso3)
                nueva[7] = Global       #Tiempo de llegada para nuevo proceso
                print(nueva)
                lista_aux.append(nueva)
                cont= cont + 1

            nueva = list(proceso)
            nueva[8] = Global  - 1 #Tiempo de finalizado para procesoque termino
            nueva[9] = nueva[8] - nueva[7]  #Tiempo de retorno
            nueva[12] = nueva[1] #Tiempo de servicio
            Terminados.append(nueva)
            
            cont = cont - 1
        
        if(len(Bloqueados) == 0 and len(lista_aux) == 0):#si ya no tenemos procesos el programa termina
            banBloqueo = False
            if proceso[0] == num:
                term(Terminados)
                system("pause")
                break
        else:#en caso contrario verificamos si tenemos procesos en bloqueados y los mandamos a ejecutar
            banBloqueo = True
            if len(lista_aux) == 0 and len(Bloqueados) > 0:
                restante = 8 - Bloqueados[0][13]
                lista_aux.append((Global,restante,0,'+',0,0,0,0,0,0,0,0,0,0))
        
    print("Tiempo total de ejecucion: " + str(Global))
    for i in range(len(Terminados)):#mostramos todos los procesos
        print(Terminados[i])
main()