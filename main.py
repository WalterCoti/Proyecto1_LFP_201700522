import colorama.ansi
import obj_set
import readFile
import leeraon
import var_global
import report
import seleccionar
from colorama import Fore, Back, Style


salir = False
set_work = ""




def main():
    while not salir:
        entrada = input(">>")
        cadena_Entrada(entrada)



def cadena_Entrada(cadenita):
    condicion_dos = False
    estado = 0
    texto = ""
    for pos in range(len(cadenita)):
        if estado == 0:
            if cadenita[pos].isspace():
                if texto.upper() == "CREATE":
                    estado = 1                      #terminado falta validar duplicados
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() == "LOAD":       #terminado ajustes, validaciones
                    estado = 3
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() =="USE":         #terminado
                    estado = 7
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() == "SELECT":
                    estado = 20
                    var_global.lst_tokens.append(texto)
                    texto = ""                      #falta aun
                elif texto.upper() == "LIST":
                    estado = 9
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() == "PRINT":      #terminado
                    estado = 10
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() == "MAX":    #terminado
                    estado = 12
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() == "MIN":    #terminado
                    estado = 13
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() == "SUM":    #terminado
                    estado = 15
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() == "COUNT":
                    estado = 16
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() == "REPORT":
                    estado = 17
                    var_global.lst_tokens.append(texto)
                    texto = ""
                elif texto.upper() == "SCRIPT": #terminado
                    estado = 14
                    texto = ""
                else:
                    print("ERROR, " + texto + " no es un comando valido")
            else:
                texto = texto + cadenita[pos]
#-----------------------------------------COMANDO CREATE SET----------------------------------------
        elif estado == 1:
            if  cadenita[pos].isspace():
                if texto.upper() == "SET":
                    estado = 2
                    var_global.lst_tokens.append(texto)
                    texto = ""
                else:
                    texto = ""
                    continue
            else:
                texto = texto + cadenita[pos]
                
        elif estado == 2:
            num = len(cadenita)
            if pos == (len(cadenita)-1):
                texto = texto + cadenita[pos]
                nuevoSet = obj_set.Objeto_Set(texto)        #corregir guardadado
                var_global.arregloSEts.append(nuevoSet)     #corregir guardado
                print("Set -> "+ texto +" <-creado con exito")
                print("---------------------------------------------------")
                #for i in range(len(var_global.arregloSEts)): #para ver el contenido de el arreglo
                    #averlosnombres = var_global.arregloSEts[i]
                    #print(averlosnombres.getnombre())
            else:
                texto = texto + cadenita[pos]
#-----------------------------------------COMANDO LOAD INTO -------------------------------------
        elif estado == 3:
            if  cadenita[pos].isspace():
                if texto.upper() == "INTO":
                    estado = 4
                    var_global.lst_tokens.append(texto)
                    texto = ""
                else:
                    texto = ""
                    continue
            else:
                texto = texto + cadenita[pos]
            
        elif estado == 4:
            if  cadenita[pos].isspace():
                set_work = texto
                estado = 5
                texto = ""
            else:
                texto = texto + cadenita[pos]

        elif estado == 5:
            if  cadenita[pos].isspace():
                if texto.upper() == "FILES":
                    estado = 6
                    texto = ""
                else:
                    texto = ""
                    continue
            else:
                texto = texto + cadenita[pos]
            
        elif estado == 6:
            if cadenita[pos].isspace():
                continue
            else:   
                if cadenita[pos] == ",":
                    var_global.lst_tokens.append(",")
                    verqeupaso = readFile.openFile(texto)
                    leeraon.leercontenido(readFile.openFile(texto),set_work)
                    print("Archivo -> " + texto + " <-  cargado a memoria")

                    texto = ""
                  
                elif pos == (len(cadenita)-1):
                    texto = texto + cadenita[pos]
                    verpaso = readFile.openFile(texto)
                    leeraon.leercontenido(readFile.openFile(texto),set_work)
                    print("Archivo -> " + texto + " <-  cargado a memoria")
                    print("---------------------------------------------------")
                    texto = ""
                    
                else:
                    texto = texto + cadenita[pos]
#-----------------------------------------COMANDO USE SET----------------------------------------
        elif estado == 7:
            if  cadenita[pos].isspace():
                if texto.upper() == "SET":
                    estado = 8
                    var_global.lst_tokens.append(texto)
                    texto = ""
                else:
                    texto = ""
                    continue
            else:
                texto = texto + cadenita[pos]
            
        elif estado == 8:
            datoExiste = False
           # posicion = (len(cadenita)-1)
            if  pos == (len(cadenita)-1):
                texto = texto + cadenita[pos]
                for i in range(len(var_global.arregloSEts)): #crear metodos que retornen boleano
                    com_name = var_global.arregloSEts[i]
                    if com_name.getnombre() == texto:
                        datoExiste = True
                        break
                    else:
                        continue
                
                if datoExiste:
                    var_global.trabajar_set = texto
                    print("El set de memoria a utilizar ahora es -> " + var_global.trabajar_set)
                    print("---------------------------------------------------")
                else:
                    print("Set " + var_global.trabajar_set + " no existe")
                        
            else:
                texto = texto + cadenita[pos]
#-----------------------------------------COMANDO LIST ATTRIBUTES ----------------------------------------
        elif estado == 9:
            if  pos == (len(cadenita)-1):
                texto = texto + cadenita[pos]
                if texto.upper() == "ATTRIBUTES":
                    var_global.lst_tokens.append(texto)
                    for i in range(len(var_global.arregloSEts)):
                        objeto_set = var_global.arregloSEts[i]
                        if objeto_set.getnombre() == var_global.trabajar_set:
                            lista_elementos = objeto_set.getlist()
                            elemento_ver = lista_elementos[0]
                            for atrib in elemento_ver.keys():
                                print("- " + atrib)    
                            print("---------------------------------------------------") 
                        else:
                            continue
                else:
                    texto = ""
                    continue
            else:
                texto = texto + cadenita[pos]
#-----------------------------------------COMANDO PRINT IN COLOR-----------------------------
        elif estado == 10:
            if  cadenita[pos].isspace():
                if texto.upper() == "IN":
                    estado = 11
                    var_global.lst_tokens.append(texto)
                    texto = ""
                else:
                    texto = ""
                    continue
            else:
                texto = texto + cadenita[pos]
            
        elif estado == 11:
            if  pos == (len(cadenita)-1):
                texto = texto + cadenita[pos]
                if texto.upper() ==  "BLUE":
                    var_global.lst_tokens.append(texto.upper())
                    print(Fore.BLUE)
                elif texto.upper() ==  "RED":
                    var_global.lst_tokens.append(texto.upper())
                    print(Fore.RED)
                elif texto.upper() ==  "GREEN":
                    var_global.lst_tokens.append(texto.upper())
                    print(Fore.GREEN)
                elif texto.upper() ==  "YELLOW":
                    var_global.lst_tokens.append(texto.upper())
                    print(Fore.YELLOW)
                elif texto.upper() ==  "ORANGE":
                    var_global.lst_tokens.append(texto.upper())
                    print(Fore.RED)
                elif texto.upper() ==  "PINK":
                    var_global.lst_tokens.append(texto.upper())
                    print(Fore.MAGENTA)
                else:
                    print("El color que se a seleccionado no existe")
            else:
                texto = texto + cadenita[pos]
#-----------------------------------------COMANDO MAX ATRIBUTO-----------------------------------------
        elif estado == 12:
            if  pos == (len(cadenita)-1):
                texto = texto + cadenita[pos]
                for i in range(len(var_global.arregloSEts)):
                        objeto_set = var_global.arregloSEts[i]
                        if objeto_set.getnombre() == var_global.trabajar_set:
                            lista_elementos = objeto_set.getlist()
                            for cel in range(len(lista_elementos)):
                                datos = lista_elementos[cel]
                                prueba_result = datos.get(texto)
                                try:
                                    if float(prueba_result).as_integer_ratio():
                                        var_global.lst_max.append(prueba_result)

                                except:
                                    var_global.lst_max.append(prueba_result)

                            try:
                                print(texto + " maximo es: " + str(max(var_global.lst_max,key=float)))
                                var_global.lst_max.clear()
                            except:
                                print(texto + " maximo es: " + str(max(var_global.lst_max,key=ascii)))
                                var_global.lst_max.clear()
                print("---------------------------------------------------")
                            
            else:
                texto = texto + cadenita[pos]
#-----------------------------------------COMANDO MIN ATRIBUTO-----------------------------------------
        elif estado == 13:
            if  pos == (len(cadenita)-1):
                texto = texto + cadenita[pos]
                for i in range(len(var_global.arregloSEts)):
                        objeto_set = var_global.arregloSEts[i]
                        if objeto_set.getnombre() == var_global.trabajar_set:
                            lista_elementos = objeto_set.getlist()
                            for cel in range(len(lista_elementos)):
                                datos = lista_elementos[cel]
                                prueba_result = datos.get(texto)
                                try:
                                    if float(prueba_result).as_integer_ratio():
                                        var_global.lst_min.append(prueba_result)
                                except:
                                    var_global.lst_min.append(prueba_result)
                            try:
                                print(texto + " minimo es: " + str(min(var_global.lst_min,key=float)))
                                var_global.lst_min.clear()
                            except:
                                print(texto + " minimo es: " + str(min(var_global.lst_min,key=ascii)))
                                var_global.lst_min.clear() 
                print("---------------------------------------------------")   
            else:
                texto = texto + cadenita[pos]
#-----------------------------------------COMANDO SCRIPT ----------------------------------------
        elif estado == 14:
            if cadenita[pos].isspace():
                continue
            else:   
                if cadenita[pos] == ",":
                    script_go(texto)
                    texto = ""
                    #set_work = ""
                elif pos == (len(cadenita)-1):
                    texto = texto + cadenita[pos]
                    script_go(texto)
                    texto = ""
                else:
                    texto = texto + cadenita[pos]
#-----------------------------------------COMANDO SUM------------------------------------------------
        elif estado == 15:
            if cadenita[pos].isspace():
                continue
            else:   
                if cadenita[pos] == ",":
                    var_global.lst_tokens.append(",")
                    var_global.lst_atributos.append(texto)
                    texto = ""
                elif cadenita[pos] == "*":
                    for i in range(len(var_global.arregloSEts)):
                        objeto_set = var_global.arregloSEts[i]
                        if objeto_set.getnombre() == var_global.trabajar_set:
                            lista_elementos = objeto_set.getlist()
                            elemento_ver = lista_elementos[0]
                            for atrib in elemento_ver.keys():
                                var_global.lst_atributos.append(atrib)  
                        else:
                            continue
                    suma()
                    
                elif pos == (len(cadenita)-1):
                    texto = texto + cadenita[pos]
                    var_global.lst_atributos.append(texto)
                    texto = ""
                    suma()
                else:
                    texto = texto + cadenita[pos]
#-----------------------------------------COMANDO COUNT--------------------------------------------
        elif estado == 16:
            if cadenita[pos].isspace():
                continue
            else:   
                if cadenita[pos] == ",":
                    var_global.lst_tokens.append(",")
                    var_global.lst_atributos.append(texto)
                    texto = ""
                elif cadenita[pos] == "*":
                    for i in range(len(var_global.arregloSEts)):
                        objeto_set = var_global.arregloSEts[i]
                        if objeto_set.getnombre() == var_global.trabajar_set:
                            lista_elementos = objeto_set.getlist()
                            elemento_ver = lista_elementos[0]
                            for atrib in elemento_ver.keys():
                                var_global.lst_atributos.append(atrib)  
                        else:
                            continue
                    contar()
                    
                elif pos == (len(cadenita)-1):
                    texto = texto + cadenita[pos]
                    var_global.lst_atributos.append(texto)
                    texto = ""
                    contar()
                else:
                    texto = texto + cadenita[pos]
#-----------------------------------------COMANDO REPORT TOKENS/TO-----------------------------------------
        elif estado == 17:
            if  pos == (len(cadenita)-1):
                texto = texto + cadenita[pos]
                if texto.upper() == "TOKENS":
                    var_global.lst_tokens.append(texto)
                    report.reportTokens(var_global.trabajar_set)
                    texto = ""
            elif cadenita[pos].isspace():
                if texto.upper() == "TO":
                    var_global.lst_tokens.append(texto)
                    estado = 18
                    texto = ""
            else:
                texto = texto + cadenita[pos]

        elif estado == 18:
            if  cadenita[pos].isspace():
                var_global.trabajar_set = texto
                estado = 19
                texto = ""
            else:
                texto = texto + cadenita[pos]
        elif estado == 19:
            if  pos == (len(cadenita)-1):
                texto = texto + cadenita[pos]
                cadena_Entrada(texto)
                texto = ""
            else:
                texto = texto + cadenita[pos]
#-----------------------------------------COMANDO SELECT------------------------------------------
        #SELECT * WHERE COND1 AND/OR/XOR COND2
        #SELECT * WHERE COND1
        #SELECT * WHERE *
        #SELECT *
        #SELECT atrib1, atrib2 WHERE COND1 AND/OR/XOR COND2
        #SELECT atrib1, atrib2 WHERE COND1
        #SELECT atrib1, atrib2 WHERE *

        #condiciones
        # nameatrib  =|!=|<|>|<=|>=  xxxxxxxx
        elif estado == 20:
            if  pos == (len(cadenita)-1):
                if cadenita[pos] == "*":
                    select_all_atrib()
            elif cadenita[pos].isspace():
                if cadenita[pos-1] == ",":
                    continue
                elif texto == "*":
                    select_all_atrib()
                    texto = ""
                    estado = 21
                else:
                    var_global.lst_atributos.append(texto)
                    texto = ""
                    estado = 21
            else:
                if cadenita[pos] == ",":
                    var_global.lst_atributos.append(texto)
                    var_global.lst_tokens.append(",")
                    texto = ""
                else:
                    texto = texto + cadenita[pos]
        elif estado == 21:
            if cadenita[pos].isspace():
                if texto.upper() == "WHERE":
                    estado = 22
                    var_global.lst_tokens.append(texto.upper())
                    texto = ""
            else:
                texto = texto + cadenita[pos]
        elif estado == 22:
            if  pos == (len(cadenita)-1):
                if cadenita[pos] == "*":
                    for set_memoria in var_global.arregloSEts:
                        if set_memoria.getnombre() == var_global.trabajar_set:
                            for elemento in set_memoria.getlist():
                                var_global.lista_res_final.append(elemento)  
                                          #si es * son todos los elementos del set
                    seleccionar.imprimir_resultado()
            elif cadenita[pos].isspace():
                var_global.key_atributo.append(texto)
                estado = 23
                texto =""
            else:
                texto = texto + cadenita[pos]
        elif estado == 23:
            if cadenita[pos].isspace():
                estado = 24
                var_global.operator_cond.append(texto)
                var_global.lst_tokens.append(texto.upper())
                texto = ""
            else:
                texto = texto + cadenita[pos]    
        elif estado == 24:
            if  pos == (len(cadenita)-1):
                texto = texto + cadenita[pos]
                var_global.value_atributo.append(texto)
                if condicion_dos:
                    seleccionar.buscarCondicion(var_global.key_atributo[0],var_global.operator_cond[0],var_global.value_atributo[0],var_global.lst_primeraCond)
                    seleccionar.buscarCondicion(var_global.key_atributo[1],var_global.operator_cond[1],var_global.value_atributo[1],var_global.lst_segundaCond)
                    seleccionar.buscarOperador();
                else:
                    seleccionar.buscarCondicion(var_global.key_atributo[0],var_global.operator_cond[0],var_global.value_atributo[0],var_global.lst_primeraCond)
                    seleccionar.buscarOperador();
                texto =""
            elif cadenita[pos].isspace():
                var_global.value_atributo.append(texto)
                condicion_dos = True
                texto =""
                estado = 27
            elif cadenita[pos]== "\"":
                var_global.lst_tokens.append("\"")
                estado = 25
            else:
                texto = texto + cadenita[pos]
        elif estado == 25:
            if  pos == (len(cadenita)-1):
                X = cadenita[pos]
                if  cadenita[pos]=="\"":
                    var_global.value_atributo.append(texto)
                    var_global.lst_tokens.append("\"")
                    texto =""
                    if condicion_dos:
                        seleccionar.buscarCondicion(var_global.key_atributo[0],var_global.operator_cond[0],var_global.value_atributo[0],var_global.lst_primeraCond)
                        seleccionar.buscarCondicion(var_global.key_atributo[1],var_global.operator_cond[1],var_global.value_atributo[1],var_global.lst_segundaCond)
                        seleccionar.buscarOperador();
                    else:
                        seleccionar.buscarCondicion(var_global.key_atributo[0],var_global.operator_cond[0],var_global.value_atributo[0],var_global.lst_primeraCond)
                        seleccionar.buscarOperador();
            elif cadenita[pos]=="\"":
                    var_global.value_atributo.append(texto)
                    var_global.lst_tokens.append("\"")
                    texto =""
                    condicion_dos = True
                    estado = 26
            else:
                texto = texto + cadenita[pos]
        elif estado == 26:
            if cadenita[pos].isspace():
                estado = 27
        elif estado == 27:
            if cadenita[pos].isspace():
                var_global.operator = texto
                var_global.lst_tokens.append(texto)
                texto=""         
                estado = 22
            else:
                texto = texto + cadenita[pos]
#-----------------------------------------COMANDO REGEX------------------------------
        elif estado == 28:
            pass


    
def script_go(direccion):
    script_comando = ""
    scrit_contenido = readFile.openFile(direccion)
    try:
        for po in range(len(scrit_contenido)):
            if scrit_contenido[po] == "\n":   
                continue
            else:
                if scrit_contenido[po] == ";":
                    cadena_Entrada(script_comando)
                    var_global.lst_tokens.append(";")
                    script_comando = ""
                else:
                    script_comando = script_comando + scrit_contenido[po]
    except:
        print("Error al intentar leer el archivo")  # aqui me da el errror no se porque

def contar():
    for atributo_bus in var_global.lst_atributos:
        value_atrib = ""
        for obj in var_global.arregloSEts:
            if obj.getnombre() == var_global.trabajar_set:
                lista_datos = obj.getlist()
                for datos_element in lista_datos:
                    value_atrib = datos_element.get(atributo_bus)
                    try:
                        var_global.lst_count.append(value_atrib)
                    except:
                        continue
        try:
            if var_global.lst_count:
                print("Datos registrados "+ atributo_bus + " = " + str(len(var_global.lst_count)))
                var_global.lst_count.clear()
            else:
                pass
        except:
           print("Atributo de tipo string")
    print("---------------------------------------------------")
    var_global.lst_atributos.clear()

def suma():
    for atributo_bus in var_global.lst_atributos:
        value_atrib = ""
        for obj in var_global.arregloSEts:
            if obj.getnombre() == var_global.trabajar_set:
                lista_datos = obj.getlist()
                for datos_element in lista_datos:
                    value_atrib = datos_element.get(atributo_bus)
                    try:
                        
                            var_global.lst_sum.append(value_atrib)
                    except:
                        continue
        try:
            if var_global.lst_sum:
                suma_Fin = list(map(float, var_global.lst_sum)) 
                print( "Suma total de " + atributo_bus + " = " + str(sum(suma_Fin)))
               
                var_global.lst_sum.clear()
                
            else:
                 print("Atributo "+ atributo_bus+ " de tipo string, no puede sumarse")
        except:
           print("Atributo de tipo string")
    print("---------------------------------------------------")
    var_global.lst_atributos.clear()

def select_all_atrib():
    for i in range(len(var_global.arregloSEts)):
        objeto_set = var_global.arregloSEts[i]
        if objeto_set.getnombre() == var_global.trabajar_set:
            lista_elementos = objeto_set.getlist()
            elemento_ver = lista_elementos[0]
            for atrib in elemento_ver.keys():
                var_global.lst_atributos.append(atrib)  
        else:
            continue


main()
