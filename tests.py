from Programa import *

#PRUEBAS DE LAS FUNCIONES DE LA FUNCION PRINCIPAL GET LLAVE
# decimal_binario
def test_decimal_binario():
    try:
        assert decimal_binario(111)=='1101111'
        assert decimal_binario(255)=='11111111'
        print("Correcto")
    except:
        print("Incorrecto")

# pasa a lista
def test_pasa_a_lista():
    try:
        assert pasa_a_lista(111)==[0, 1, 1, 1]
        assert pasa_a_lista(255)==[0, 2, 5, 5]
        print("Correcto")
    except:
        print("Incorrecto")

# largo
def test_largo():
    try:
        assert largo(111)==3
        assert largo(255)==3
        print("Correcto")
    except:
        print("Incorrecto")

# binario decimal
def test_binario_decimal():
    try:
        assert binario_decimal(1101111)==111
        assert binario_decimal(11111111)==255
        print("Correcto")
    except:
        print("Incorrecto")

# binario en lista a numero binario
def test_binario_en_lista_a_numero_binario():
    try:
        assert binario_en_lista_a_numero_binario([0,1,1,0,1,1,1,1])==1101111
        assert binario_en_lista_a_numero_binario([1,1,1,1,1,1,1,1])==11111111
        print("Correcto")
    except:
        print("Incorrecto")

def test_get_llave():
    try:
        assert get_llave(111)==183
        assert get_llave(255)==127
        print("Correcto")
    except:
        print("Incorrecto")

#get llave
print("Pruebas de las funciones de la funcion principal get llave")
test_decimal_binario()
test_pasa_a_lista()
test_largo()
test_decimal_binario()
test_binario_en_lista_a_numero_binario()
test_binario_en_lista_a_numero_binario()
test_get_llave()
print("")

#-------------------------------------------------------------------------------

#PRUEBAS DE LAS FUNCIONES DE LA FUNCION PRINCIPAL ENCRIPTAR
# rotar
def test_rotar():
    try:
        assert rotar(111)=='xyzabcdefghijklmnñopqrstuvw'
        assert rotar(255)=='opqrstuvwxyzabcdefghijklmnñ'
        print("Correcto")
    except:
        print("Incorrecto")

# reemplazar
def test_reemplazar():
    try:
        assert reemplazar('a',111)=='x'
        assert reemplazar('a',255)=='o'
        print("Correcto")
    except:
        print("Incorrecto")

# encriptar
def test_encriptar():
    try:
        assert encriptar('hola mundo',111)=='eubj rrsnh.'
        assert encriptar('hola mundo',255)=='vwcw vnwvl.'
        print("Correcto")
    except:
        print("Incorrecto")

#encriptar
print("Pruebas de la funcion principal encriptar")
test_rotar()
test_reemplazar()
test_encriptar()
print("")

#-------------------------------------------------------------------------------

#PRUEBAS DE LA FUNCION DESENCRIPTAR
# rotar R
def test_rotarR():
    try:
        assert rotarR(111)=='defghijklmnñopqrstuvwxyzabc'
        assert rotarR(255)=='mnñopqrstuvwxyzabcdefghijkl'
        print("Correcto")
    except:
        print("Incorrecto")

# reemplazar D
def test_reemplazar_D():
    try:
        assert reemplazar_D('a',111)=='d'
        assert reemplazar_D('a',255)=='m'
        print("Correcto")
    except:
        print("Incorrecto")

#
def test_desencriptar():
    try:
        assert desencriptar('hola mundo',111)=='kjur gxhtw'
        assert desencriptar('hola mundo',255)=='shte ccdls'
        print("Correcto")
    except:
        print("Incorrecto")

#DESENCRIPTAR
print("Pruebas de la funcion principal encriptar")
test_rotarR()
test_reemplazar_D()
test_desencriptar()
print("")
