import os

def leerArchivo(nameFile):
    my_path = os.path.abspath(os.path.dirname(__file__))
    print(my_path)
    path = os.path.join(my_path, nameFile)
    print (path)
    
    with open (path, 'r+') as data: 
        contenido = data.read()
        return contenido


