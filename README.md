# SimpleQL CLI

SimpleQL CLI es una interfaz de línea de comandos que permite utilizar SimpleQL para
realizar diferentes operaciones de análisis y consultas sobre un conjuto de datos que se
encuentra alojado en memoria. Puede verse como una versión 2.0 del SimpleQL original,
con la diferencia de que esta versión amplía las capacidades de análisis, consulta y
búsqueda, al mismo tiempo que permite trabajar con registros que tengan estructuras
diferentes. Esta versión de SimpleQL también implementa su propia notación de objetos
para los archivos de texto que contienen la información inicial, esta se conoce como AON
(Alternative Object Notation) y su estructura se define más adelante.


## Funciones y Comandos
## - CREATE SET

Tiene la función de crear sets de memoria donde se alojarán ciertos conjuntos de
datos cargados por el usuario. La aplicación tiene la capacidad de poseer activos N conjuntos de datos.
Ejemplo:
```bash
>>CREATE SET EJEMPLO_SET
```

## - LOAD INTO 
Este comando carga al conjunto especificado por set_id la información contenida en la los archivos de la lista de archivos definida después de la keyword FILES.

```bash
>>LOAD INTO EJEMPLO_SET FILES ARCIVO1.AON, ARCHIVO2.AON
```


## - USE SET
Este comando define el set de datos a utilizar para las siguientes operaciones, si se intenta realizar operaciones sin haber definido un set de datos la aplicación debe
mostrar un error.
```bash
>>USE SET EJEMPLO_SET
```

## -SELECT atrib_uno, atrib_dos, etc  WHERE condiciones
Permite seleccionar uno o más registros o atributos de los mismos con base encondiciones simples que pueden aplicarse a los atributos de los mismos.En lugar de listar los atributos también es posible utilizar el operador *, esto
automáticamente seleccionará todos los campos del registro.
Ejemplo:
```bash
>>SELECT modelo, tipo, marca, año WHERE color = “rojo”
```
Las condiciones pueden ser:
- "<"  menor que,
- ">" mayorque,
- "<="  menor o igual que,
- ">=" mayor o igual que,
- "="  igual,
- "!=" no igual,

Ademas de poder combinarlo con los Operadores:

- "AND"
- "OR"
- "XOR"
```bash
>>SELECT * WHERE marca = “Mazda” AND año < 1996
```
