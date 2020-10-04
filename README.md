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

## - LIST ATTRIBUTES
Este comando permite listar los atributos que componen a cada registro del set.

```bash
>>LIST ATTRIBUTTES
```
## - PRINT IN 
Este comando permite al usuario elegir el color en el que serán presentados los
resultados en la línea de comandos. 
Los valores a elegir serán:
- BLUE, 
- RED, 
- GREEN,
- YELLOW, 
- ORANGE y 
- PINK. 

Ejemplo:


```bash
>>PRINT IN BLUE
```



## - MAX | MIN 
Permiten encontrar el valor máximo o el valor mínimo que se encuentre en el atributo de uno de los registros del conjunto en memoria. En caso de seleccionar el valor máximo de un valor de tipo String la comparación será realizada de forma lexicográfica. 
Ejemplos:
```bash
>>MAX edad
>>MIN precio
```
## - SUM
Permite obtener la suma de todos los valores de un atributo especificado en el comando. Este comando solamente se utilizará sobre valores de tipo numérico, no se realizarán sumas sobre valores de tipo cadena o booleanos. En caso de seleccionarse varios atributos deberá reportar cada atributo con su respectiva suma, en caso de que el atributo tenga valor null se ignorará. El comando SUM acepta el uso del operador *.
Ejemplos:
```bash
>>SUM edad, promedio, faltas
```

## - COUNT 
Permite contar el número de registros que se han cargado a memoria. En caso de que alguno de los atributos tenga valor null se ignorará. El comando COUNT permite el uso del operador *.
Ejemplos:
```bash
>>COUNT edad, promedio, faltas
```

## - REPORT TO < id > < comando >
Este comando permite crear un reporte en html a partir de cualquier otro comando
de análisis o selección. El reporte debe ser agradable a la vista y fácil de leer. El id
define el nombre del archivo sobre el que se crea el reporte.

```bash
REPORT TO reporte1 COUNT *
REPORT TO reporte2 SUM *
REPORT TO reporte3 SELECT * WHERE edad != 44
```

## - SCRIPT 
Este comando permite cargar scripts con extensión .siql que contienen series de instrucciones y comandos SimpleQL, esto con el objetivo de que el usuario no tenga que escribir uno por uno los comandos que se desee ejecutar. Algunos lineamientos para este tipo de archivo se dan más adelante.
```bash
>>SCRIPT C://User/Descktop/carga_masiva.siql
>>SCRIPT carga_masiva.siql
```
## - REPORT TOKENS
Este comando crea un reporte en html que muestra una lista de todos los lexemas encontrados por el AFD, mostrando también a cual token pertenece
el lexema y una breve descripción del mismo.
```bash
>>REPORT TOKENS
```
