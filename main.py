import colorama.ansi
import obj_set
import readFile
import leeraon
import var_global
from colorama import Fore, Back, Style


salir = False
set_work = ""




def main():
    while not salir:
        entrada = input(">>")
        cadena_Entrada(entrada)



def cadena_Entrada(cadenita):
    estado = 0
    texto = ""
    for pos in range(len(cadenita)):
        if estado == 0:
            if cadenita[pos].isspace():
                if texto.upper() == "CREATE":
                    estado = 1                      #terminado falta validar duplicados
                    texto = ""
                elif texto.upper() == "LOAD":       #terminado ajustes, validaciones
                    estado = 3
                    texto = ""
                elif texto.upper() =="USE":         #terminado
                    estado = 7
                    texto = ""
                elif texto.upper() == "SELECT":
                    estado = 1                      #falta aun
                elif texto.upper() == "LIST":
                    estado = 9
                    texto = ""
                elif texto.upper() == "PRINT":      #terminado
                    estado = 10
                    texto = ""
                elif texto.upper() == "MAX":    #terminado
                    estado = 12
                    texto = ""
                elif texto.upper() == "MIN":    #terminado
                    estado = 13
                    texto = ""
                elif texto.upper() == "SUM":    #terminado
                    estado = 15
                    texto = ""
                elif texto.upper() == "COUNT":
                    estado = 16
                    texto = ""
                elif texto.upper() == "REPORT":
                    estado = 1
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
                    verqeupaso = readFile.openFile(texto)
                    leeraon.leercontenido(readFile.openFile(texto),set_work)
                    print("Archivo -> " + texto + "cargado a memoria")

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
                    print(Fore.BLUE)
                elif texto.upper() ==  "RED":
                    print(Fore.RED)
                elif texto.upper() ==  "GREEN":
                    print(Fore.GREEN)
                elif texto.upper() ==  "YELLOW":
                    print(Fore.YELLOW)
                elif texto.upper() ==  "ORANGE":
                    print(Fore.RED)
                elif texto.upper() ==  "PINK":
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
#--------------------------------------------COMANDO SUM------------------------------------------------
        elif estado == 15:
            if cadenita[pos].isspace():
                continue
            else:   
                if cadenita[pos] == ",":
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
#----------------------------------------COMANDO COUNT--------------------------------------------
        elif estado == 16:
            if cadenita[pos].isspace():
                continue
            else:   
                if cadenita[pos] == ",":
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
#------------------------------------------COMANDO REPORT TO-----------------------------------------
        elif estado == 17:
            pass
        elif estado == 18:
            pass
        elif estado == 19:
            pass
        elif estado == 20:
            pass
        elif estado == 21:
            pass
        elif estado == 22:
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
                    script_comando = ""
                else:
                    script_comando = script_comando + scrit_contenido[po]
    except:
        print("Error al intentar leer el archivo")

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
                        if float(value_atrib).as_integer_ratio():
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
                    

main()
