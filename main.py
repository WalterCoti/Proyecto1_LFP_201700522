import colorama.ansi
import obj_set
import readFile
import leeraon
import var_global

from colorama import Fore, Back, Style


salir = False





def main():
    while not salir:
        entrada = input("$")
        cadena_Entrada(entrada)



def cadena_Entrada(cadenita):
    estado = 0
    texto = ""
    set_work = ""
    for pos in range(len(cadenita)):
        if estado == 0:
            texto = texto + cadenita[pos]
            if texto.upper() == "CREATE":
                estado = 1
                texto = ""
            elif texto.upper() == "LOAD":
                estado = 3
                texto = ""
            elif texto.upper() =="USE":
                estado = 7
            elif texto.upper() == "SELECT":
                estado = 1
            elif texto.upper() == "LIST":
                 estado = 1
            elif texto.upper() == "PRINT":
                 estado = 1
            elif texto.upper() == "MAX":
                 estado = 1
            elif texto.upper() == "MIN":
                 estado = 1
            elif texto.upper() == "SUM":
                 estado = 1
            elif texto.upper() == "COUNT":
                 estado = 1
            elif texto.upper() == "REPORT":
                 estado = 1
            elif texto.upper() == "SCRIPT":
                 estado = 1
    
#---------------------COMANDO CREATE SET
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
                
                #for i in range(len(var_global.arregloSEts)): #para ver el contenido de el arreglo
                   # averlosnombres = var_global.arregloSEts[i]
                   # print(averlosnombres.getnombre())
            else:
                texto = texto + cadenita[pos]

#-----------------COMANDO LOAD INTO -------------------------------------
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
                    set_work = ""
                elif pos == (len(cadenita)-1):
                    texto = texto + cadenita[pos]
                    verpaso = readFile.openFile(texto)
                    leeraon.leercontenido(readFile.openFile(texto),set_work)
                    print("Archivo -> " + texto + " <-  cargado a memoria")
                    texto = ""
                    set_work = ""

                  #  for i in range(len(var_global.arregloSEts)):            #para ver el contenido de el arreglo
                     #   averlosnombres = var_global.arregloSEts[i]
                      #  print(averlosnombres.getlist())
                else:
                    texto = texto + cadenita[pos]

#--------------------------------------COMANDO USE SET----------------------------------------
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
                    set_work = texto
                    print("El set de memoria a utilizar ahora es = " + set_work)
                else:
                    print("Set " + texto + " no existe")
                        
            else:
                texto = texto + cadenita[pos]
        elif estado == 9:
            pass
        elif estado == 10:
            pass
        elif estado == 11:
            pass
        elif estado == 12:
            pass
        elif estado == 13:
            pass
        elif estado == 14:
            pass
        elif estado == 15:
            pass
        elif estado == 16:
            pass
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
    
    

main()
