# Neftali Nohema Ramos Arriga 7°A

# comienzo proceso cifrado
#funcion de codificar
def cifrado( texto, s ):
#Trndremos un ingreo de un string
    result = ""

# Se agrega un for y un range por que representa el rango de la longitud del texto
    for i in range( len( texto ) ):
# Se creo la variable char que se ira incrementando segun la variabale i
#Con esto alimentamos nuestra cadena que se va ir incrementando 
        char = texto[ i ]
# Se crea un ciclo if con la variable char.isupper en caso de que se encuentra alguna mayuscula
        if( char.isupper() ):
# Con la linea 18 se encaragara de generar la operación para generar el valor de char y poder hacer la operación matematica
# Como se esta desifrando se considera apropado coloar un + y verificamos que se encuentre dentro del rango de las mayusculas
            result += chr( ( ord( char ) + s - 65 ) % 26 + 65 )
# Se crea el else para poder manejar las minusculas
        else:
            result += chr( ( ord( char ) + s - 97 ) % 26 + 97 )
# Se retorna a nuestra oción return que es el resultado que arroja el ciclo for 
    return result

# Se solicitara un mensaje al usuario 
mensaje = input( "El texto plano a cifrar es: " )
# Se solicta al usuario el valor de desplaciamiento que se asignara al mensaje
s = int( input( "El desplazamiento de cifrado es: " ) )

# Esta opcion nos permite desplegar el texto cifrado
textCifrado = cifrado( mensaje, s )
# La opcion print nos permite imprimir el texto cifrado obtenido
print("El texto cifrado resultante es: " +  textCifrado )




# comienzo proceso decifrado
#funcion de codificar
def decifrado( texto, s ):
#Tedremos un ingreo de un string
    result = ""

# Se agrega un for y un range por que representa el rango de la longitud del texto
    for i in range( len( texto ) ):
# Se creo la variable char que se ira incrementando segun la variabale i
#Con esto alimentamos nuestra cadena que se va ir incrementando 
        char = texto[ i ]
# Se crea un ciclo if con la variable char.isupper en caso de que se encuentra alguna mayuscula
        if( char.isupper() ):
# Con la linea 52 se encaragara de generar la operación para generar el valor de char y poder hacer la operación matematica
# Como se esta desifrando se considera apropado coloar un + y verificamos que se encuentre dentro del rango de las mayusculas
            result += chr( ( ord( char ) - s - 65 ) % 26 + 65 )
# Se crea el else para poder manejar las minusculas
        else:
            result += chr( ( ord( char ) - s - 97 ) % 26 + 97 )
# Se retorna a nuestra oción return que es el resultado que arroja el ciclo for 
    return result

# Se solicitara el mensaje al usuario que desea decifrar
mensaje = input( "El texto a decifrar es: " )
# Se solicta al usuario el valor de desplaciamiento que se asigno al mensaje
s = int( input( "El desplazamiento de decifrado es: " ) )

# Esta opcion nos permite desplegar el texto decifrado
textCifrado = decifrado( mensaje, s )
# La opcion print nos permite imprimir el texto decifrado obtenido
print("El texto plano decifrado resultante es: " +  textCifrado )