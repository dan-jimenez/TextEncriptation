#generacion del valor de la llave

#funciones auxiliares

def decimal_binario(numero):
    """
    La funcion binario auxiliar de la get llave

    Parametros:
    numero: cualquier numero entero

    Retorna:
    pasa cualquier numero a base 2 osea binaria
    """
    cadena='01' 
    if numero<2:
        return cadena[numero]
    else:
        return decimal_binario(numero//2)+cadena[numero%2]

def pasa_a_lista(n):
    """
    La funcion pasa a lista auxiliar de la get llave

    Parametros:
    n: cualquier numero entero

    Retorna:
    pasa los digitos de cualquier numero a una lista
    """
    if n==0:
        return [0]
    else:
        return pasa_a_lista(n//10)+[n%10]

def largo(n):
    """
    La funcion largo auxiliar de binario decimal

    Parametros:
    n: cualquier numero entero

    Retorna:
    cuenta el largo de un numero entero
    """
    if n<10:
        return 1
    else:
        return 1 + largo(n//10)

def binario_decimal(numero,base=2):
    """
    La funcion binario decimal auxiliar de la get llave

    Parametros:
    numero: cualquier numero entero

    Retorna:
    pasa un numero en base 2 osea notacion binaria a base decimal osea base 10
    """
    if numero<10:
        return numero
    else:
        return (numero//10**(largo(numero)-1))*base**(largo(numero)-1)+binario_decimal(numero%10**(largo(numero)-1),base)

def binario_en_lista_a_numero_binario(lista,num=0,i=0):
    """
    La funcion binario en lista a numero binario auxiliar de la get llave

    Parametros:
    lista: digitos de un numero binario en una lista como elementos de una lista

    Retorna:
    pasa los digitos de un numero binario en una lista a un numero binario
    """
    if i!=len(lista):
        num=num*10+lista[i]
        i=i+1
    else:
        return num
    return binario_en_lista_a_numero_binario(lista,num,i)

#funcion principal

#del 1 al 63 no funciona

#del 64 al 127 funciona perfecto

#del 128 al 255 tira con 9 bits

LONG_LLAVE = 255

def get_llave(num):
    """
    La funcion get llave

    Parametros:
    num: cualquier numero entre 1 y 255

    Retorna:
    da como resultado una llave especifica que se necesita para encriptar y desnecriptar
    """
    if num ==1:
        llave=(int(decimal_binario(num)))
        #print(llave)
        final=pasa_a_lista(llave)
        final.reverse()
        final.append(0)
        final.append(0)
        final.append(0)
        final.append(0)
        final.append(0)
        final.append(0)
        final.reverse()
        #print(final)
        pos7=final[7]
        pos5=final[5]
        pos3=final[3]
        pos2=final[2]
        #print(final[7],final[5],final[3],final[2])
        xor1=final[7]^final[5]
        #print(xor1)
        xor2=xor1^final[3]
        #print(xor2)
        xor3=xor2^final[2]
        #print(xor3)
        final.insert(0,xor3)
        final.pop()
        #print(final)
        lista_final=binario_en_lista_a_numero_binario(final)
        num_final=binario_decimal(lista_final)
        return(num_final)

    elif num >= 2 and num <= 3:
        llave=(int(decimal_binario(num)))
        #print(llave)
        final=pasa_a_lista(llave)
        final.reverse()
        final.append(0)
        final.append(0)
        final.append(0)
        final.append(0)
        final.append(0)
        final.reverse()
        #print(final)
        pos7=final[7]
        pos5=final[5]
        pos3=final[3]
        pos2=final[2]
        #print(final[7],final[5],final[3],final[2])
        xor1=final[7]^final[5]
        #print(xor1)
        xor2=xor1^final[3]
        #print(xor2)
        xor3=xor2^final[2]
        #print(xor3)
        final.insert(0,xor3)
        final.pop()
        #print(final)
        lista_final=binario_en_lista_a_numero_binario(final)
        num_final=binario_decimal(lista_final)
        return(num_final)

    elif num >= 4 and num <= 7:
        llave=(int(decimal_binario(num)))
        #print(llave)
        final=pasa_a_lista(llave)
        final.reverse()
        final.append(0)
        final.append(0)
        final.append(0)
        final.append(0)
        final.reverse()
        #print(final)
        pos7=final[7]
        pos5=final[5]
        pos3=final[3]
        pos2=final[2]
        #print(final[7],final[5],final[3],final[2])
        xor1=final[7]^final[5]
        #print(xor1)
        xor2=xor1^final[3]
        #print(xor2)
        xor3=xor2^final[2]
        #print(xor3)
        final.insert(0,xor3)
        final.pop()
        #print(final)
        lista_final=binario_en_lista_a_numero_binario(final)
        num_final=binario_decimal(lista_final)
        return(num_final)

    elif num >= 8 and num <= 15:
        llave=(int(decimal_binario(num)))
        #print(llave)
        final=pasa_a_lista(llave)
        final.reverse()
        final.append(0)
        final.append(0)
        final.append(0)
        final.reverse()
        #print(final)
        pos7=final[7]
        pos5=final[5]
        pos3=final[3]
        pos2=final[2]
        #print(final[7],final[5],final[3],final[2])
        xor1=final[7]^final[5]
        #print(xor1)
        xor2=xor1^final[3]
        #print(xor2)
        xor3=xor2^final[2]
        #print(xor3)
        final.insert(0,xor3)
        final.pop()
        #print(final)
        lista_final=binario_en_lista_a_numero_binario(final)
        num_final=binario_decimal(lista_final)
        return(num_final)

    elif num >= 16 and num <= 31:
        llave=(int(decimal_binario(num)))
        #print(llave)
        final=pasa_a_lista(llave)
        final.reverse()
        final.append(0)
        final.append(0)
        final.reverse()
        #print(final)
        pos7=final[7]
        pos5=final[5]
        pos3=final[3]
        pos2=final[2]
        #print(final[7],final[5],final[3],final[2])
        xor1=final[7]^final[5]
        #print(xor1)
        xor2=xor1^final[3]
        #print(xor2)
        xor3=xor2^final[2]
        #print(xor3)
        final.insert(0,xor3)
        final.pop()
        #print(final)
        lista_final=binario_en_lista_a_numero_binario(final)
        num_final=binario_decimal(lista_final)
        return(num_final)

    elif num >= 32 and num <= 63:
        llave=(int(decimal_binario(num)))
        #print(llave)
        final=pasa_a_lista(llave)
        final.reverse()
        final.append(0)
        final.reverse()
        #print(final)
        pos7=final[7]
        pos5=final[5]
        pos3=final[3]
        pos2=final[2]
        #print(final[7],final[5],final[3],final[2])
        xor1=final[7]^final[5]
        #print(xor1)
        xor2=xor1^final[3]
        #print(xor2)
        xor3=xor2^final[2]
        #print(xor3)
        final.insert(0,xor3)
        final.pop()
        #print(final)
        lista_final=binario_en_lista_a_numero_binario(final)
        num_final=binario_decimal(lista_final)
        return(num_final)
    
    elif num >= 64 and num <= 127:
        llave=(int(decimal_binario(num)))
        #print(llave)
        final=pasa_a_lista(llave)
        #print(final)
        pos7=final[7]
        pos5=final[5]
        pos3=final[3]
        pos2=final[2]
        #print(final[7],final[5],final[3],final[2])
        xor1=final[7]^final[5]
        #print(xor1)
        xor2=xor1^final[3]
        #print(xor2)
        xor3=xor2^final[2]
        #print(xor3)
        final.insert(0,xor3)
        final.pop()
        #print(final)
        lista_final=binario_en_lista_a_numero_binario(final)
        num_final=binario_decimal(lista_final)
        return(num_final)
    
    elif num >= 128 and num <= LONG_LLAVE:
        llave=(int(decimal_binario(num)))
        #print(llave)
        final=pasa_a_lista(llave)
        final.reverse()
        final.pop()
        final.reverse()
        #print(final)
        pos7=final[7]
        pos5=final[5]
        pos3=final[3]
        pos2=final[2]
        #print(final[7],final[5],final[3],final[2])
        xor1=final[7]^final[5]
        #print(xor1)
        xor2=xor1^final[3]
        #print(xor2)
        xor3=xor2^final[2]
        #print(xor3)
        final.insert(0,xor3)
        final.pop()
        #print(final)
        lista_final=binario_en_lista_a_numero_binario(final)
        num_final=binario_decimal(lista_final)
        return(num_final)
    
    else:
        return"El numero ingresado es 0 o es mayor a 255"

#help(decimal_binario)
#help(pasa_a_lista)
#help(largo)
#help(binario_decimal)
#help(binario_en_lista_a_numero_binario)
#help(get_llave)
        
#--------------------------------------------------------------------------------
#encriptacion del texto
import string

def recorrer_lista(n):
    """
    La funcion recorrer lista

    Parametros:
    n: cualquier numero entero

    Retorna:
    da como resultado la primera letra para encriptar el texto 
    """
    alfabeto=list(string.ascii_lowercase)
    nueva_lista=[]
    letra=alfabeto[n]
    nueva_lista+=letra
    print(nueva_lista)
    recorrer_lista_aux(letra,n+1,alfabeto,nueva_lista)
    return nueva_lista

def recorrer_lista_aux(letra,n,alfabeto,nueva_lista):
    """
    La funcion recorrer lista aux

    Parametros:
    letra: parametro expecifico
    n: parametro expecifico
    alfabeto: parametro expecifico
    nueva lista: parametro expecifico

    Retorna:
    es la llamda recursiva de la funcion recorrer lista 
    """
    if(n>25):
        return recorrer_lista_aux(letra,0,alfabeto,nueva_lista)
    elif (letra==alfabeto[n]):
        return nueva_lista
    else:
        nueva_lista+=alfabeto[n]
        return recorrer_lista_aux(letra,n+1,alfabeto,nueva_lista)

def recorrer_lista_final(n):
    """
    La funcion recorrer lista final

    Parametros:
    n: cualquier numero entero entre 1 y 255

    Retorna:
    da como resultado la primera letra para encriptar el texto ya aplicando la funcion de generar la llave de valor con la funcion get llave
    """
    total=n%26
    total_final=recorrer_lista(total)
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print(abc)
    return(total_final)

def encriptar(n):
    final=get_llave(n)
    print(final)
    total=final%26
    final2=recorrer_lista(total)
    print(final2)


##-------------------------------------------------------##
#funcion para rotar la lista#
def rotar(llave):
    return rotar_aux(llave, "abcdefghijklmnñopqrstuvwxyz")
def rotar_aux(llave, cinta2):
    if 0<llave<255:
        if llave==1:
            return cinta2[26] + cinta2[0:26] 
        else:
            return rotar_aux(llave-1, cinta2[26] + cinta2[0:26])
    elif llave== 0:
        return cinta2
    else: 
        return "Introduzca un numero entre 0 y 255"
##------------------------------------------------------##
#funcion para reemplazar la letra "x" por la que corresponderia por en la cinta2
def reemplazar(letra, llave):
    cinta= "abcdefghijklmnñopqrstuvwxyz"
    cinta_M= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cinta2= rotar(llave)
    cinta2_M= cinta2.upper()

    if letra == "," or letra == "." or letra == "¿":
        return letra
    elif letra == "?" or letra == "!" or letra == "¡":
        return letra
    elif letra == "/" or letra == "-" or letra == "_":
        return letra
    elif letra==":" or letra == ";" or letra == "(" or letra == ")":
        return letra
    elif letra == "[" or letra == "]" or letra == "{" or letra == "}":
        return letra
    elif letra == "<" or letra == ">" or letra == "#" or letra == "%" or letra == " &":
        return letra
    elif letra == "+" or letra == "*" or letra == "°" or letra == "|":
        return letra
    elif cinta.count(letra) == 1:
        if cinta == cinta2:
            return letra
        else:
            indiceLetra= cinta.index(letra)
            return cinta2[indiceLetra]
    else:
        if cinta_M== cinta2_M:
            return letra
        else:
            indiceLetra_M= cinta_M.index(letra)
            return cinta2_M[indiceLetra_M]
##-------------------------------------------------------##
#la siguiente función es para poder cifrar un texto
#llave= int(input("Ingrese la llave: "))
#texto= input("Ingrese el texto a leer: ")
def cifrado(texto, llave):
    if len(texto)==0:
        return "."
    else:
        if texto[0] ==" ":
            return " " + cifrado(texto[1:], get_llave(llave))
        else:
            return reemplazar(texto[0], llave) + cifrado(texto[1:], get_llave(llave))

#--------------------------------------------------------------------------------
#desencriptacion del texto
##-------------------------------------------------------##
#funcion para rotar el string#
def rotarR(llave):
    return rotarR_aux(llave, "abcdefghijklmnñopqrstuvwxyz")
def rotarR_aux(llave, cinta2):
    if 0<llave<255:
        if llave==1:
            return cinta2[1:27] + cinta2[0]
        else:
            return rotarR_aux(llave-1, cinta2[1:27] + cinta2[0])
    elif llave== 0:
        return cinta2
    else: 
        return "Introduzca un numero entre 0 y 255"
##---------------------------------------------------------##
#funcion para reemplazar una letra# 
def reemplazar_D(letra, llave):
    cinta= "abcdefghijklmnñopqrstuvwxyz"
    cinta_M= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cinta2= rotarR(llave)
    cinta2_M= cinta2.upper()

    if letra == "," or letra == "." or letra == "¿":
        return letra
    elif letra == "?" or letra == "!" or letra == "¡":
        return letra
    elif letra == "/" or letra == "-" or letra == "_":
        return letra
    elif letra==":" or letra == ";" or letra == "(" or letra == ")":
        return letra
    elif letra == "[" or letra == "]" or letra == "{" or letra == "}":
        return letra
    elif letra == "<" or letra == ">" or letra == "#" or letra == "%" or letra == " &":
        return letra
    elif letra == "+" or letra == "*" or letra == "°" or letra == "|":
        return letra
    elif cinta.count(letra) == 1:
        if cinta == cinta2:
            return letra
        else:
            indiceLetra= cinta.index(letra)
            return cinta2[indiceLetra]
    else:
        if cinta_M== cinta2_M:
            return letra
        else:
            indiceLetra_M= cinta_M.index(letra)
            return cinta2_M[indiceLetra_M]
#-------------------------------------------------------#
#funcion para desencriptar un texto
#llave= int(input("Ingrese la llave: "))
#texto= input("Ingrese el texto a leer: ")
def desencriptar(texto, llave):
    if len(texto)==0:
        return ""
    else:
        if texto[0] == " ":
            return " " + desencriptar(texto[1:], get_llave(llave))
        else:
            return reemplazar_D(texto[0], llave) + desencriptar(texto[1:], get_llave(llave))


