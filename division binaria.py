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
    print("DIVISION BINARIA\n-----------------------------------------")
    introducirnumero1 = list(map(int,str(input("introduzca el primer numero:\t "))))
    introducirnumero2 = list(map(int,str(input("introduzca el segundo numero:\t "))))
    introducirnumero2=[0] * (len(introducirnumero1) - len(introducirnumero2)) + introducirnumero2
    crearnumero1="".join(map(str,introducirnumero1))
    crearnumero2="".join(map(str,introducirnumero2))
    numero1=list(map(int,str(crearnumero1)))
    numero2=list(map(int,str(crearnumero2)))
    cociente, resto=crear_division_binaria(numero1,numero2)
    cocientebinario=bin(cociente)[2:]
    restobinario=bin(resto)[2:]
    resultadobinario="el cociente binario es:\t"+str("{:>9}".format(cocientebinario))+"\nel resto binario es:\t"+str("{:>9}".format(restobinario))
    resultadodecimal="el cociente decimal es: "+str(cociente)+" y el resto decimal es: "+str(resto)
    print(resultadobinario)
    print (resultadodecimal)

