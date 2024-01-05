import os
import sys

def checkear_version_de_python():
    version_requerida = [(3, 10), (3, 11), (3, 12)]
    version_instalada = sys.version_info[:2]
    if version_instalada in version_requerida:
        verificacion="version de python: "+str(version_instalada)+"\nla version de python instalada es compatible."
        print(verificacion)
        os.system("pause")
        print("\n\n")
        borrar_consola()
    else:
        verificacion="la version de python instalada es compatible\nes necesario tener instalado Python3.10, 3.11, o 3.12"
        print(verificacion)

def borrar_consola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def crear_portada():
    portada="---------------------------CALCULADORA BINARIA---------------------------"
    print(portada)

def seleccionar_calculo():
    calculo=input("elige una opcion (suma, resta, multiplicacion o division): ")
    while (calculo not in ["suma","resta","multiplicacion","division"]):
        print("opcion invalida => vuelve a intentarlo")
        calculo=input("elige una opcion (suma, resta, multiplicacion o division): ")
    return calculo

def crear_separacion():
    separacion="-------------------------------------------------------------------------"
    print(separacion)

def crear_suma_binaria(numero1, numero2):
    resultado = [0] * len(numero1)
    acarreo = 0
    for n in reversed(range(len(numero1))):
        bit1 = numero1[n]
        bit2 = numero2[n]
        if bit1 == 0 and bit2 == 0 and acarreo == 0:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 1 and bit2 == 0 and acarreo == 0:
            resultado[n] = 1
            acarreo = 0
        elif bit1 == 0 and bit2 == 1 and acarreo == 0:
            resultado[n] = 1
            acarreo = 0
        elif bit1 == 1 and bit2 == 1 and acarreo == 0:
            resultado[n] = 0
            acarreo = 1
        elif bit1 == 0 and bit2 == 0 and acarreo == 1:
            resultado[n] = 1
            acarreo = 0
        elif bit1 == 1 and bit2 == 0 and acarreo == 1:
            resultado[n] = 0
            acarreo = 1
        elif bit1 == 0 and bit2 == 1 and acarreo == 1:
            resultado[n] = 0
            acarreo = 1
        elif bit1 == 1 and bit2 == 1 and acarreo == 1:
            resultado[n] = 1
            acarreo = 1
    if numero1[0] == 1 and numero2[0] == 1:
        resultado.insert(0,1)
    binario = "".join(map(str,resultado))
    return binario

def crear_resta_binaria(numero1, numero2):
    resultado = [0] * len(numero1)
    acarreo = 0
    for n in reversed(range(len(numero1))):
        bit1 = numero1[n]
        bit2 = numero2[n]
        if bit1 == 0 and bit2 == 0 and acarreo == 0:
            resultado[n] = 0
            acarreo=0
        elif bit1 == 1 and bit2 == 0 and acarreo == 0:
            resultado[n] = 1 
            acarreo = 0
        elif bit1 == 0 and bit2 == 1 and acarreo == 0:
            resultado[n] = 1
            acarreo = 1
        elif bit1 == 1 and bit2 == 1 and acarreo == 0:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 0 and bit2 == 0 and acarreo == 1:
            resultado[n] = 1
            acarreo = 1
        elif bit1 == 1 and bit2 == 0 and acarreo == 1:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 0 and bit2 == 1 and acarreo == 1:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 1 and bit2 == 1 and acarreo == 1:
            resultado[n] = 1
            acarreo = 1
    binario = "".join(map(str,resultado))
    return binario

def crear_multiplicacion_binaria(numero1,numero2):
    numero3=numero1
    numero4=numero1
    numero_repeticion=numero2
    binario=suma_binaria_en_multiplicacion_binaria(numero3,numero4)
    crear_repeticion= "".join(map(str,numero_repeticion))
    repeticion=int(crear_repeticion, 2)
    for _ in range(repeticion-2):
        introducirnumero5 = list(map(int,str(binario)))
        introducirnumero6 = numero1
        introducirnumero6=[0] * (len(introducirnumero5) - len(introducirnumero6)) + introducirnumero6
        crearnumero5="".join(map(str,introducirnumero5))
        crearnumero6="".join(map(str,introducirnumero6))
        numero5=list(map(int,str(crearnumero5)))
        numero6=list(map(int,str(crearnumero6)))
        binario=repetir_suma_binaria_en_multiplicacion_binaria(numero5,numero6)
    return binario

def suma_binaria_en_multiplicacion_binaria(numero3, numero4): 
    resultado = [0] * len(numero3)
    acarreo = 0
    for n in range(len(numero3) - 1, -1, -1):
        bit1 = numero3[n]
        bit2 = numero4[n]
        if bit1 == 0 and bit2 == 0 and acarreo == 0:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 1 and bit2 == 0 and acarreo == 0:
            resultado[n] = 1
            acarreo = 0
        elif bit1 == 0 and bit2 == 1 and acarreo == 0:
            resultado[n] = 1
            acarreo = 0
        elif bit1 == 1 and bit2 == 1 and acarreo == 0:
            resultado[n] = 0
            acarreo = 1
        elif bit1 == 0 and bit2 == 0 and acarreo == 1:
            resultado[n] = 1
            acarreo = 0
        elif bit1 == 1 and bit2 == 0 and acarreo == 1:
            resultado[n] = 0
            acarreo = 1
        elif bit1 == 0 and bit2 == 1 and acarreo == 1:
            resultado[n] = 0
            acarreo = 1
        elif bit1 == 1 and bit2 == 1 and acarreo == 1:
            resultado[n] = 1
            acarreo = 1
    if numero3[0] == 1 and numero4[0] == 1:
        resultado.insert(0,1)
    binario = "".join(map(str,resultado))
    return binario

def repetir_suma_binaria_en_multiplicacion_binaria(numero5, numero6):
    resultado = [0] * len(numero5)
    acarreo = 0
    for n in range(len(numero5) - 1, -1, -1):
        bit1 = numero5[n]
        bit2 = numero6[n]
        if bit1 == 0 and bit2 == 0 and acarreo == 0:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 1 and bit2 == 0 and acarreo == 0:
            resultado[n] = 1
            acarreo = 0
        elif bit1 == 0 and bit2 == 1 and acarreo == 0:
            resultado[n] = 1
            acarreo = 0
        elif bit1 == 1 and bit2 == 1 and acarreo == 0:
            resultado[n] = 0
            acarreo = 1
        elif bit1 == 0 and bit2 == 0 and acarreo == 1:
            resultado[n] = 1
            acarreo = 0
        elif bit1 == 1 and bit2 == 0 and acarreo == 1:
            resultado[n] = 0
            acarreo = 1
        elif bit1 == 0 and bit2 == 1 and acarreo == 1:
            resultado[n] = 0
            acarreo = 1
        elif bit1 == 1 and bit2 == 1 and acarreo == 1:
            resultado[n] = 1
            acarreo = 1
    if numero5[0] == 1 and numero6[0] == 1:
        resultado.insert(0,1)
    elif numero5[1] == 1 and numero6[1] == 1:
        resultado.insert(0,1)
    else:
        resultado.insert(0,0)
    binario = "".join(map(str,resultado))
    return binario

def crear_division_binaria(numero1,numero2):
    repeticiones=[]
    binario=crear_resta_binaria_en_division_binaria(numero1,numero2)
    repeticiones.append(binario)
    decimal=int(binario, 2)
    if decimal==0 or decimal==1:
        cociente=len(repeticiones)
        resto=decimal
        return cociente, resto
    else:
        while decimal!=0 or decimal!=1:
            introducirnumero3 = list(map(int,str(binario)))
            introducirnumero4 = numero2
            introducirnumero4=[0] * (len(introducirnumero3) - len(introducirnumero4)) + introducirnumero4
            crearnumero3="".join(map(str,introducirnumero3))
            crearnumero4="".join(map(str,introducirnumero4))
            numero3=list(map(int,str(crearnumero3)))
            numero4=list(map(int,str(crearnumero4)))
            binario=repetir_resta_binaria_en_division_binaria(numero3,numero4)
            repeticiones.append(binario)
            decimal=int(binario, 2)
            if decimal==0 or decimal==1:
                cociente=len(repeticiones)
                resto=decimal
                return cociente, resto

def crear_resta_binaria_en_division_binaria(numero1, numero2):
    resultado = [0] * len(numero1)
    acarreo = 0
    for n in range(len(numero1) - 1, -1, -1):
        bit1 = numero1[n]
        bit2 = numero2[n]
        if bit1 == 0 and bit2 == 0 and acarreo == 0:
            resultado[n] = 0
            acarreo=0
        elif bit1 == 1 and bit2 == 0 and acarreo == 0:
            resultado[n] = 1 
            acarreo = 0
        elif bit1 == 0 and bit2 == 1 and acarreo == 0:
            resultado[n] = 1
            acarreo = 1
        elif bit1 == 1 and bit2 == 1 and acarreo == 0:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 0 and bit2 == 0 and acarreo == 1:
            resultado[n] = 1
            acarreo = 1
        elif bit1 == 1 and bit2 == 0 and acarreo == 1:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 0 and bit2 == 1 and acarreo == 1:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 1 and bit2 == 1 and acarreo == 1:
            resultado[n] = 1
            acarreo = 1
    binario = "".join(map(str,resultado))
    return binario

def repetir_resta_binaria_en_division_binaria(numero3, numero4):
    resultado = [0] * len(numero3)
    acarreo = 0
    for n in range(len(numero3) - 1, -1, -1):
        bit1 = numero3[n]
        bit2 = numero4[n]
        if bit1 == 0 and bit2 == 0 and acarreo == 0:
            resultado[n] = 0
            acarreo=0
        elif bit1 == 1 and bit2 == 0 and acarreo == 0:
            resultado[n] = 1 
            acarreo = 0
        elif bit1 == 0 and bit2 == 1 and acarreo == 0:
            resultado[n] = 1
            acarreo = 1
        elif bit1 == 1 and bit2 == 1 and acarreo == 0:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 0 and bit2 == 0 and acarreo == 1:
            resultado[n] = 1
            acarreo = 1
        elif bit1 == 1 and bit2 == 0 and acarreo == 1:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 0 and bit2 == 1 and acarreo == 1:
            resultado[n] = 0
            acarreo = 0
        elif bit1 == 1 and bit2 == 1 and acarreo == 1:
            resultado[n] = 1
            acarreo = 1
    binario = "".join(map(str,resultado))
    return binario

if __name__=="__main__":
    borrar_consola()
    checkear_version_de_python()
    crear_portada()
    calculo=seleccionar_calculo()
    crear_separacion()
    error="solo se pueden introducir ocho digitos de 0 y 1"
    try:
        introducirnumero1 = list(map(int,str(input("introduzca el primer numero:\t "))))
        introducirnumero2 = list(map(int,str(input("introduzca el segundo numero:\t "))))
        # se autoañaden numeros 0 a la segunda lista hasta tener la misma longitud que la primera
        introducirnumero2=[0] * (len(introducirnumero1) - len(introducirnumero2)) + introducirnumero2
        crearnumero1="".join(map(str,introducirnumero1))
        crearnumero2="".join(map(str,introducirnumero2))
        numero1=list(map(int,str(crearnumero1)))
        numero2=list(map(int,str(crearnumero2)))
        if (len(numero1) > 0 and len(numero1) < 9) or (len(numero2) > 0 and len(numero2) < 9):
            for n in (numero1 and numero2):
                if (n == 0 or n == 1):
                    if calculo == "suma":
                        binario = crear_suma_binaria(numero1,numero2)
                    elif calculo == "resta":
                        binario = crear_resta_binaria(numero1,numero2)
                    elif calculo == "multiplicacion":
                        binario = crear_multiplicacion_binaria(numero1,numero2)
                    elif calculo == "division":
                        cociente, resto=crear_division_binaria(numero1,numero2)
                else:
                    raise ValueError (error)
            if calculo=='suma' or calculo=='resta' or calculo=='multiplicacion':
                crear_separacion()
                decimal=int(binario, 2)
                resultado="el resultado binario es:\t"+str("{:>9}".format(binario))+"\nel resultado decimal es:\t"+str("{:>9}".format(decimal))
                print(resultado)
            elif calculo=="division":
                crear_separacion()
                cocientebinario=bin(cociente)[2:]
                restobinario=bin(resto)[2:]
                resultadobinario="el cociente binario es:\t"+str("{:>9}".format(cocientebinario))+"\nel resto binario es:\t"+str("{:>9}".format(restobinario))
                print(resultadobinario)
                crear_separacion()
                resultadodecimal="el cociente decimal es: "+str(cociente)+" y el resto decimal es: "+str(resto)
                print(resultadodecimal)
        else:
            raise ValueError (error)
    except ValueError:
        print (error)
