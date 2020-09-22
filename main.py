from colorama import Fore, Back, Style
import colorama.ansi
import var_global
import readFile
import obj_set
salir = False





def main():
    while not salir:
        entrada = input(">>")
        cadena_Entrada(entrada)



def cadena_Entrada(cadenita):
    estado = 0
    texto = ""
    for pos in range(len(cadenita)):
        if estado == 0:
            texto = texto + cadenita[pos]
            if texto == "CREATE":
                estado = 1
                texto = ""
            elif texto == "LOAD":
                estado = 3
                texto = ""
            elif texto =="USE":
                estado = 1
            elif texto == "SELECT":
                estado = 1
            elif texto == "LIST":
                 estado = 1
            elif texto == "PRINT":
                 estado = 1
            elif texto == "MAX":
                 estado = 1
            elif texto == "MIN":
                 estado = 1
            elif texto == "SUM":
                 estado = 1
            elif texto == "COUNT":
                 estado = 1
            elif texto == "REPORT":
                 estado = 1
            elif texto == "SCRIPT":
                 estado = 1
            else:
                print("Comando inexistente")
            
    

        elif estado == 1:
            if  cadenita[pos].isspace():
                if texto == "SET":
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
                for i in range(len(var_global.arregloSEts)): #para ver el contenido de el arreglo
                    averlosnombres = var_global.arregloSEts[i]
                    print(averlosnombres.getnombre())
            else:
                texto = texto + cadenita[pos]
        elif estado == 3:
            pass
            
        elif estado == 4:
            pass
        elif estado == 5:
            pass
        elif estado == 6:
            pass
        elif estado == 7:
            pass
        elif estado == 8:
            pass
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
for i in range(len(var_global.arregloSEts)):
    print(var_global.arregloSEts[i].getnombre())