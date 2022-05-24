import hashlib

menu = 0

while menu != 1 and menu != 2:
    print("")
    print(">>>>Bienvenido al programa de cifrado con Hashlib<<<<")
    print("")
    print("  >>Introduzca el numero (1) para Cifrado de Cadena de Texto<<")
    print("")
    print("  >>Introduzca el numero (2) para Cifrado de Archivo<<")
    print("  ")
    menu = int(input(" Introduzca su opción: "))

    if menu == 1:
        cifrado = 0
        while cifrado > 10 or cifrado <= 0:
            
            print("  ")
            print(" 1.-Cifrado MD5")
            print(" 2.-Cifrado sha1")
            print(" 3.-Cifrado sha256")
            print(" 4.-Cifrado sha224")
            print(" 5.-Cifrado sha384")
            print(" 6.-Cifrado sha512")
            print(" 7.-Cifrado sha3_224")
            print(" 8.-Cifrado sha3_256")
            print(" 9.-Cifrado sha3_384")
            print(" 10.-Cifrado sha3_512")
            print("  ")
            cifrado = int(input("Seleccione Cifrado a utilizar: "))
        string = input("Introduzca mensaje a cifrar: ")

        if cifrado == 1:
            
            md5 = hashlib.md5()
            md5.update(string.encode('utf-8'))
            res = md5.hexdigest()
            print("El Resultado de cifrado md5:", res)

        elif cifrado == 2:
            
            sha1 = hashlib.sha1()
            sha1.update(string.encode('utf-8'))
            res = sha1.hexdigest()
            print("El Resultado de cifrado sha1:", res)

        elif cifrado == 3:
            
            sha256 = hashlib.sha256()
            sha256.update(string.encode('utf-8'))
            res = sha256.hexdigest()
            print("El Resultado de cifrado sha256:", res)

        elif cifrado == 4:
            
            sha224 = hashlib.sha224()
            sha224.update(string.encode('utf-8'))
            res = sha224.hexdigest()
            print("El Resultado de cifrado sha224:", res)

        elif cifrado == 5:
            
            sha384 = hashlib.sha384()
            sha384.update(string.encode('utf-8'))
            res = sha384.hexdigest()
            print("El Resultado de cifrado sha384:", res)

        elif cifrado == 6:
            
            sha512 = hashlib.sha512()
            sha512.update(string.encode('utf-8'))
            res = sha512.hexdigest()
            print("El Resultado de cifrado sha512:", res)

        elif cifrado == 7:
            
            sha3_224 = hashlib.sha3_224()
            sha3_224.update(string.encode('utf-8'))
            res = sha3_224.hexdigest()
            print("El Resultado de cifrado sha3_224:", res)

        elif cifrado == 8:
            
            sha3_256 = hashlib.sha3_256()
            sha3_256.update(string.encode('utf-8'))
            res = sha3_256.hexdigest()
            print("El Resultado de cifrado sha3_256:", res)

        elif cifrado == 9:
            
            sha3_256 = hashlib.sha3_256()
            sha3_256.update(string.encode('utf-8'))
            res = sha3_256.hexdigest()
            print("El Resultado de cifrado sha3_256:", res)

        elif cifrado == 10:
            
            sha3_512 = hashlib.sha3_512()
            sha3_512.update(string.encode('utf-8'))
            res = sha3_512.hexdigest()
            print("El Resultado de cifrado sha3_512:", res)

     

    elif menu == 2:
        cifrado = 0
        while cifrado > 12 or cifrado <= 0:
          
            print("  ")
            print(" 1.-Cifrado MD5")
            print(" 2.-Cifrado sha1")
            print(" 3.-Cifrado sha256")
            print(" 4.-Cifrado sha224")
            print(" 5.-Cifrado sha384")
            print(" 6.-Cifrado sha512")
            print(" 7.-Cifrado sha3_224")
            print(" 8.-Cifrado sha3_256")
            print(" 9.-Cifrado sha3_384")
            print(" 10.-Cifrado sha3_512")
            print("  ")
            cifrado = int(input("Seleccione Cifrado a utilizar: "))

        string = input("Ingrese ruta y nombre del archivo: ")
        
        
        openedFile = open(string, 'rb')
        readFile = openedFile.read()

        if cifrado == 1:
            
            md5 = hashlib.md5()
            md5.update(string.encode('utf-8'))
            res = md5.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Hash MD5: %r" % res)

        elif cifrado == 2:
            
            sha1 = hashlib.sha1()
            sha1.update(string.encode('utf-8'))
            res = sha1.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Resultado del Hash sha1: %r" % res)

        elif cifrado == 3:
            
            sha256 = hashlib.sha256()
            sha256.update(string.encode('utf-8'))
            res = sha256.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Resultado del Hash sha256: %r" % res)

        elif cifrado == 4:
            
            sha224 = hashlib.sha224()
            sha224.update(string.encode('utf-8'))
            res = sha224.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Resultado del Hash sha224: %r" % res)

        elif cifrado == 5:
            
            sha384 = hashlib.sha384()
            sha384.update(string.encode('utf-8'))
            res = sha384.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Resultado del Hash sha384: %r" % res)

        elif cifrado == 6:
            
            sha512 = hashlib.sha512()
            sha512.update(string.encode('utf-8'))
            res = sha512.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Resultado del Hash sha512: %r" % res)

        elif cifrado == 7:
            
            sha3_224 = hashlib.sha3_224()
            sha3_224.update(string.encode('utf-8'))
            res = sha3_224.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Resultado del Hash sha3_224: %r" % res)

        elif cifrado == 8:
            
            sha3_256 = hashlib.sha3_256()
            sha3_256.update(string.encode('utf-8'))
            res = sha3_256.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Resultado del Hash sha3_256: %r" % res)

        elif cifrado == 9:
            
            sha3_256 = hashlib.sha3_256()
            sha3_256.update(string.encode('utf-8'))
            res = sha3_256.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Resultado del Hash sha3_384: %r" % res)

        elif cifrado == 10:
            
            sha3_512 = hashlib.sha3_512()
            sha3_512.update(string.encode('utf-8'))
            res = sha3_512.hexdigest()
            print("Nombre del Archivo: %s" % string)
            wait = input("PRESIONA ENTER PARA PARA CONTINUAR")
            print("Resultado del Hash sha3_512: %r" % res)

       