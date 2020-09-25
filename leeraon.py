import var_global
import obj_set


list_llaves = []
list_valores = []

token = {"(" : "tk_inicio",
        "<" : "tk_ini_objeto",
        "[" : "tk_ini_atributo",
        "texto" : "tk_texto",
        "]" : "tk_fin_atributo",
        "=" : "tk_signo_igual",
        "numero" : "tk_numero",
        "\"": "tk_comilla",
        "," : "tk_coma",
        ">" : "tk_fin_objeto",
        ")" : "tk_fin"
        }



def leercontenido(contenido,id_set):
    estado = 0
    caracter_Sig = ""
    tmp_string = ""
    numero = ""
    boleano = ""
    texto = ""
    encontrocomilla = False
    for pos in range(len(contenido)):
        
        if estado == 0:
            if contenido[pos] == "(":
                #print(contenido[pos]+" <-- "+ token.get(contenido[pos]))
                estado = 1
            else:
                print("Error de lectura") 
        elif estado == 1:
            if contenido[pos] == "<":
                #print(contenido[pos] +" <-- "+ token.get(contenido[pos]))
                estado = 2
        elif estado == 2:
            if contenido[pos] == "[" :
               # print( contenido[pos] +" <-- "+ token.get(contenido[pos]))
                estado = 3

        elif estado == 3:
            caracter_Sig = contenido[pos+1]
            if caracter_Sig == "]":
                tmp_string = tmp_string + contenido[pos]
                list_llaves.append(tmp_string)
               # print(tmp_string + " <-- "+ token.get("texto"))
                tmp_string = ""
                estado = 4  
            elif contenido[pos].isascii():
                tmp_string = tmp_string + contenido[pos]

        elif estado == 4:
            if contenido[pos] == "]" :
               # print( contenido[pos] +" <-- "+ token.get(contenido[pos]))
                estado = 5

        elif estado == 5:
            if contenido[pos] == "=" :
               # print( contenido[pos] +" <-- "+ token.get(contenido[pos]))
                estado = 6
        elif estado == 6:     #estado 6
            caracter_Sig = contenido[(pos+1)]
            if contenido[pos].isspace():
                continue
            else:
                if contenido[pos].isascii():
                    if contenido[pos] == "\"":
                       # print(contenido[pos] + " <-- "+ token.get(contenido[pos]))
                        estado = 8
                    elif caracter_Sig == ",":
                        texto = texto + contenido[pos]
                       # print(texto + " <-- "+ token.get("numero"))
                        encontrocomilla = False
                        list_valores.append(texto)
                        texto = ""
                        estado = 7
                    elif caracter_Sig == "\n":
                        texto = texto + contenido[pos]
                       # print(texto + " <-- "+ token.get("texto"))
                        list_valores.append(texto)
                        encontrocomilla = False
                        texto = ""
                        estado = 7
                    else:
                        texto = texto + contenido[pos]
 
        elif estado == 7:
            if contenido[pos] == "," :
                #print( contenido[pos] +" <-- "+ token.get(contenido[pos]))
                estado = 2
            elif contenido[pos] == ">":
                #print( contenido[pos] +" <-- "+ token.get(contenido[pos]))
                estado = 10
                elemento = dict(zip(list_llaves , list_valores))
                for i in range(len(var_global.arregloSEts)):            #buscar en el arreglo de sets
                    nuevos_datos = var_global.arregloSEts[i]
                    if nuevos_datos.getnombre() == id_set:     #veo si es el set correcto
                        nuevos_datos.setElementList(elemento)             #agrego la informacion
                        break                                           #detengo el ciclo
                    else:
                        continue                                        #si no es el set continua el ciclo
                list_llaves.clear()
                list_valores.clear()


        elif estado == 8:
            caracter_Sig = contenido[pos+1]
            if contenido[pos].isascii():
                if caracter_Sig == "\"":
                    texto = texto + contenido[pos]
                    list_valores.append(texto)
                   # print(texto + " <-- "+ token.get("texto"))
                    texto = ""
                    estado = 9
                else:
                    texto = texto + contenido[pos]
                
            elif contenido[pos].isascii():
                texto = texto + contenido[pos]

        elif estado == 9:
            caracter_Sig = contenido[pos+1]
            if contenido[pos] == "\"" :
               # print( contenido[pos] +" <-- "+ token.get(contenido[pos]))
                estado = 7
        elif estado == 10:
            if contenido[pos] == ")" :
                #print( contenido[pos] +" <-- "+ token.get(contenido[pos]))
                estado = 11
            elif contenido[pos] == ",":
                #print( contenido[pos] +" <-- "+ token.get(contenido[pos]))
                estado = 1
        elif estado == 11:
            pass

