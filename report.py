import var_global
import base_html
import listaTokens
import webbrowser
import os

def reportTokens(name_set):
        lst_head = ['No.','Lexema','Token','Descripción']
    #try: 
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, name_set + ".html")
        with  open(path, 'w+') as file_reporte:
            file_reporte.write(base_html.html_head("ReportTokens","Tokens"))
            file_reporte.write("<thead class=\"thead-dark\">")
            file_reporte.write("<tr>")
            for columna in lst_head:
                file_reporte.write("<th>"+ columna+ "</th>")
            file_reporte.write("</tr>")
            file_reporte.write("</thead")
            file_reporte.write("<tbody>")
            for cont in range(len(var_global.lst_tokens)):
                file_reporte.write("<tr>")
                file_reporte.write("<th>"+ str(cont+1) + "</th>")
                file_reporte.write("<td>"+ var_global.lst_tokens[cont] + "</td>")
                file_reporte.write("<td>"+ listaTokens.tokens.get(var_global.lst_tokens[cont]) + "</td>")
                file_reporte.write("<td>"+ listaTokens.definicion_token.get(var_global.lst_tokens[cont]) + "</td>")
                file_reporte.write("</tr>")
            file_reporte.write("</tbody>")
            file_reporte.write(base_html.final_hmtl)
        webbrowser.open_new_tab(path)
        print("Reporte de Tokens creado con Exito")
    #except:
    #    print("Algo Paso")
    


def reportTo(name_set):
    try:  
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, name_set + ".html")
        with  open(path, 'w+') as file_reporte:
            file_reporte.write(report.codinicio)
            for i in range(int(numero_reporte)):    
                file_reporte.write("<tr>") 
                file_reporte.write("<td>" + str(i+1) + "</td>")                                    
                for atributo in allatrib:
                    file_reporte.write("<td>" + str(arreglo[i].get(atributo)) + "</td>" )
                file_reporte.write("</tr>")
            file_reporte.write(report.final_hmtl)
            file_reporte.close()
        webbrowser.open_new(path)
        print("Reporte Creado con Exito")
    except:
          print("Etoma este")