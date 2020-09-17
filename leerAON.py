
def leerArchivo(self, set_id, path):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, path)
    
    with open (path, 'r') as data: 
        contenido = data.read()
        print("Archivos cargados con exito\n")