import os
import var_global


def buscarCondicion(name_atrib,condicion,value_atrib,lst_resultado):
    for set_memoria in var_global.arregloSEts:
        if set_memoria.getnombre() == var_global.trabajar_set:
            for objeto_lista in set_memoria.getlist():
                valor_buscar = objeto_lista.get(name_atrib)
                if condicion == "<":
                   if valor_buscar < value_atrib:
                       lst_resultado.append(objeto_lista)
                elif condicion == ">":
                    if valor_buscar > value_atrib:
                       lst_resultado.append(objeto_lista)
                elif condicion == "<=":
                    if valor_buscar <= value_atrib:
                       lst_resultado.append(objeto_lista)
                elif condicion == ">=":
                    if valor_buscar >= value_atrib:
                       lst_resultado.append(objeto_lista)
                elif condicion == "=":
                    if valor_buscar == value_atrib:
                       lst_resultado.append(objeto_lista)
                elif condicion == "!=":
                    if valor_buscar != value_atrib:
                       lst_resultado.append(objeto_lista)
                else:
                    print("condicion \"" + condicion + "\" no reconocida")
            
        else:
            continue

def buscarOperador():
    if var_global.lst_segundaCond:
        if var_global.operator == "AND":
            for elemento_cuno in var_global.lst_primeraCond:
                for elemento_cdos in var_global.lst_segundaCond:    
                    if elemento_cuno == elemento_cdos: # reviso si no existe en resultados 
                        if elemento_cuno in var_global.lista_res_final:
                            continue
                        else:
                            var_global.lista_res_final.append(elemento_cuno)
        
        elif var_global.operator == "OR":
            tmp_list = var_global.lst_primeraCond + var_global.lst_segundaCond       
            for elemento in tmp_list:
                if elemento in var_global.lista_res_final:
                    continue
                else:
                    var_global.lista_res_final.append(elemento)
                    
        elif var_global.operator == "XOR":
            for elemento in var_global.lst_primeraCond:
                if elemento not in var_global.lst_segundaCond:
                    var_global.lista_res_final.append(elemento)  
            for elemento in var_global.lst_segundaCond:
                if elemento not in var_global.lst_primeraCond:
                    var_global.lista_res_final.append(elemento) 
    
    else:
        var_global.lista_res_final = var_global.lst_primeraCond.copy()
    imprimir_resultado()



def imprimir_resultado():
    for element in var_global.lista_res_final:
        for atributo in var_global.lst_atributos:
            valor_elemento = element.get(atributo)
            print(atributo + " = " + valor_elemento)
        print("---------------------------------------------------")
    var_global.lst_primeraCond.clear()
    var_global.lst_segundaCond.clear()
    var_global.lista_res_final.clear()
    var_global.lst_atributos.clear()
            