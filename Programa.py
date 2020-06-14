from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as FileDialog
import webbrowser
import tkinter
import math
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#VENATANA PRINCIPAL
class menu(tkinter.Tk):
    def __init__(menu):
        tkinter.Tk.__init__(menu)
        #Titulo
        menu.title("Programa de Encriptacion y Desencriptacion")
        
        #Tamaño (cambiar al gusto)
        menu.geometry("500x500")
        menu.config(bg="gray")
        menu.config(bd="25")
        menu.config(relief="groove")
        menu.resizable(False, False)

        #Label titulo
        menu.label= Label(menu, text= "Encriptar y Desencriptar", bg ='gray', fg= 'white', font = ("Arial Narrow", 20))
        menu.label.grid(row=1, column= 3, padx= 20, pady= 5) #(x=125, y=10)

        #Label indicación
        menu.label= Label(menu, text= "Este programa fue creado para encriptar y desencriptar texto\nSi necesitas encriptar presiona el primer botón\nSi necesitas desencriptar presiona el segundo botón", bg ='gray', fg= 'white', font = ("Arial Narrow", 14))
        menu.label.grid(row=12, column= 3, padx= 20, pady= 15)
        
        #Botone encriptar
        menu.buttonEncriptar= Button(menu, text="Encriptar",width=18, activebackground="#696969",command= menu.encriptar, fg = "white", bg = "#3f3f3f", font = ("Arial Narrow", 14))
        menu.buttonEncriptar.grid(row=3, column= 3, padx= 50, pady= 15)
        
        #Boton desencriptar
        menu.buttonDesencriptar= Button(menu, text="Desencriptar",width=18, activebackground="#696969",command= menu.desencriptar, fg = "white", bg = "#3f3f3f", font = ("Arial Narrow", 14))
        menu.buttonDesencriptar.grid(row=5, column= 3, padx=50, pady= 10 )

        #Boton del Ayuda de usuario
        menu.buttonAyuda= Button(menu, text="Ayuda", width= 18, activebackground= "#696969", command= menu.ayuda, fg= "white", bg= "#3f3f3f", font= ("Arial Narrow", 14))
        menu.buttonAyuda.grid(row=7, column= 3, padx=50, pady= 10 )


        #Boton de información del programa
        menu.buttonInfo= Button(menu, text="Info", width= 18, activebackground= "#696969", command= menu.Info, fg= "white", bg= "#3f3f3f", font= ("Arial Narrow", 14))
        menu.buttonInfo.grid(row=9, column= 3, padx=50, pady= 10 )

        #Boton para salir
        menu.buttonSalir= Button(menu, text="Salir",width=18, activebackground="#696969",command= menu.salir, fg = "white", bg = "#3f3f3f", font = ("Arial Narrow", 14))
        menu.buttonSalir.grid(row=11, column=3, padx=50, pady=10)


    def encriptar(menu):
        menu.destroy()
        ingresar_encriptacion().mainloop()

    def desencriptar(menu):
        menu.destroy()
        ingresar_desencriptacion().mainloop()
    
    def salir(menu):
        menu.destroy()
        mainloop()

    def ayuda(menu): #cambiar localizacion cuando el manual de usuario este terminado
        webbrowser.open("https://estudianteccr-my.sharepoint.com/:b:/g/personal/danny_jimenez_estudiantec_cr/EbVoy4g0dS5Oo3Spt24_JoIBgP3jRA-jDLys0OzgZfw56w?e=2oVKLq", new=2, autoraise=True)
        
        
    def Info(menu):
        messagebox.showinfo("Acerca De", "Nombre del Programa: Encriptacion y Desencriptacion \nAutores: Roberto José Garita Mata\n               Danny Jossiel Jimenez Sevilla \nFecha: 06/12/2020 \nVersión: 1.0")

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#VENATANA DE ENCRIPTAR
class ingresar_encriptacion(tkinter.Tk):  
    def __init__(self):
        global nombre
        tkinter.Tk.__init__(self)
        self.title("Encriptar")
        self.geometry("580x500")
        self.config(bg= "gray", bd= "20", relief= "groove")
        self.resizable(False, False)

        #Labels
        self.labelDescripcion= Label(self, text= "Encriptación de texto", fg =  "white", bg= "gray", font = ("Arial Narrow", 20))
        self.labelDescripcion.grid(row= 1, column= 1, sticky= "w", padx=0, pady= 5)

        self.label= Label(self, text= "Ingrese la llave:", fg =  "white", bg= "gray", font = ("Arial Narrow", 16))
        self.label.grid(row= 3, column= 0, padx=5, sticky= "w", pady= 10)

        self.label= Label(self, text= "Escriba el texto:", fg =  "white", bg= "gray", font = ("Arial Narrow", 16))
        self.label.grid(row= 5, column= 0, padx=5, sticky= "w", pady= 10)

        #TextBox
        self.textBoxLlave = Entry(self, width=10, font = ("Arial Narrow", 12))
        self.textBoxLlave.grid(row= 3, column= 1, sticky= "w", pady= 10)

        self.textBoxTexto = Text (self, width= 33, height= 14, font = ("Arial Narrow", 12))
        self.textBoxTexto.grid(row= 5, column= 1, sticky= "w", pady= 10)

        #Botones
        self.buttonEncriptar= Button(self, text="Encriptar",width=14, activebackground="#696969",command= self.display_encriptacion, fg = "white", bg = "#3f3f3f", font = ("Arial Narrow", 14))
        self.buttonEncriptar.grid(row= 9, column= 0, sticky="s", padx=5, pady= 10)

        #Boton para acceder a arhivo
        self.buttonArchivo= Button(self, text="Archivo",width=14, activebackground="#696969",command= self.archivo, fg = "white", bg = "#3f3f3f", font = ("Arial Narrow", 14))
        self.buttonArchivo.grid(row= 9, column= 1, sticky="s", padx=5, pady= 10)

        #Boton para salir
        self.buttonSalir= Button(self, text="Regresar al menú",width=16, activebackground="#696969",command= self.salir, fg = "white", bg = "#3f3f3f", font = ("Arial Narrow", 14))
        self.buttonSalir.grid(row= 9, column= 2, sticky="s", pady= 10)

        #Funciones de la ventana

    def display_encriptacion(self):
        entry=self.textBoxLlave.get()
        number=int(entry)
        llave=number
        msj=self.textBoxTexto.get("1.0",END)
        texto= msj.replace("\n", " ")
        resultado=encriptar(texto,llave)
        fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode='w', defaultextension=".txt", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if fichero is not None:
            fichero.write(resultado)
            fichero.close()
        messagebox.showinfo("El texto encriptado es", resultado)
        self.destroy()
        menu().mainloop()

    def archivo(self):
        ruta= FileDialog.askopenfilename(filetypes=(("Archivos de texto","*.txt"),("Todos los archivos", "*.*")), title= "Abrir un archivo")
        archivo = open(ruta, 'r')
        textoConSaltos= archivo.read()
        texto1 = textoConSaltos.replace("\n"," ")
        entry = self.textBoxLlave.get()
        number=int(entry)
        llave = number
        resultado = encriptar(texto1,llave)
        fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode='w', defaultextension=".txt", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if fichero is not None:
            fichero.write(resultado)
            fichero.close()
        messagebox.showinfo("El texto encriptado es:", resultado)
        self.destroy()
        menu().mainloop()
        #Parte donde se escribe en un texto

    def salir(self):
        self.destroy()
        menu().mainloop()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#VENTANA DE DESENCRIPTAR
class ingresar_desencriptacion(tkinter.Tk):  
    def __init__(self):
        global nombre
        tkinter.Tk.__init__(self)
        self.title("Desencriptar")
        self.geometry("580x500")
        self.config(bg="gray", bd=20, relief= "groove")
        self.resizable(False,False)

        #Labels
        self.labelDescripcion= Label(self, text= "Desencriptación de texto", fg =  "white", bg= "gray", font = ("Arial Narrow", 20))
        self.labelDescripcion.grid(row= 1, column= 1, sticky= "w", padx=0, pady= 5)

        self.label= Label(self, text= "Ingrese la llave:", fg =  "white", bg= "gray", font = ("Arial Narrow", 16))
        self.label.grid(row= 3, column= 0, padx=5, sticky= "w", pady= 10)

        self.label= Label(self, text= "Escriba el texto:", fg =  "white", bg= "gray", font = ("Arial Narrow", 16))
        self.label.grid(row= 5, column= 0, padx=5, sticky= "w", pady= 10)

        #TextBox
        self.textBoxLlave = Entry(self, width=10, font = ("Arial Narrow", 12))
        self.textBoxLlave.grid(row= 3, column= 1, sticky= "w", pady= 10)

        self.textBoxTexto=Text(self, width=33, height= 14, font = ("Arial Narrow", 12))
        self.textBoxTexto.grid(row= 5, column= 1, sticky= "w", pady= 10)

        #Boton para desencriptar
        self.buttonDesencriptar=Button(self, text= "Desencriptar", width=14, activebackground="#696969", command= self.realizar_desencriptacion, fg= "white", bg= "#3f3f3f", font= ("Arial Narrow", 14))
        self.buttonDesencriptar.grid(row=9, column= 0, sticky="s", padx=5, pady= 10)

        #Boton para acceder a arhivo
        self.buttonArchivo= Button(self, text="Archivo",width=14, activebackground="#696969",command= self.archivo, fg = "white", bg = "#3f3f3f", font = ("Arial Narrow", 14))
        self.buttonArchivo.grid(row= 9, column= 1, sticky="s", padx=5, pady= 10)

        #Boton para salir
        self.buttonSalir= Button(self, text="Regresar al menú", width=14, activebackground="#696969",command= self.salir, fg = "white", bg = "#3f3f3f", font = ("Arial Narrow", 14))
        self.buttonSalir.grid(row= 9, column= 2, sticky="s", pady= 10)

        #Funciones de la ventana

    def realizar_desencriptacion(self):
        entry=self.textBoxLlave.get()
        number=int(entry)
        llave=number
        msj=self.textBoxTexto.get("1.0", END)
        texto=msj.replace("\n", " ")
        resultado=desencriptar(texto,llave)
        fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode='w', defaultextension=".txt", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if fichero is not None:
            fichero.write(resultado)
            fichero.close()
        messagebox.showinfo("El texto desencriptado es", resultado)
        self.destroy()
        menu().mainloop()

    def archivo(self): 
        ruta= FileDialog.askopenfilename(filetypes=(("Archivos de texto","*.txt"),("Todos los archivos", "*.*")), title= "Abrir un archivo")
        archivo= open(ruta, 'r')
        textoConSaltos= archivo.read()
        texto1=textoConSaltos.replace("\n", " ")
        entry=self.textBoxLlave.get()
        number=int(entry)
        llave=number
        resultado= desencriptar(texto1,llave)
        fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode='w', defaultextension=".txt", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if fichero is not None:
            fichero.write(resultado)
            fichero.close()
        messagebox.showinfo("El texto desencriptado es:", resultado)
        self.destroy()
        menu().mainloop()

    def salir(self):
        self.destroy()
        menu().mainloop()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#FUNCIONES PRINCIPALES (PARTE LOGICA)

#generacion del valor de la llave

#funciones auxiliares de la funcion principal get llave

#1
def decimal_binario(numero):
    #""""
    #La funcion binario auxiliar de la get llave

    #Parametros:
    #numero: cualquier numero entero

    #Retorna:
    #pasa cualquier numero a base 2 osea binaria
    #"""
    cadena='01' 
    if numero<2:
        return cadena[numero]
    else:
        return decimal_binario(numero//2)+cadena[numero%2]
#2
def pasa_a_lista(n):
    #"""
    #La funcion pasa a lista auxiliar de la get llave

    #Parametros:
    #n: cualquier numero entero

    #Retorna:
    #pasa los digitos de cualquier numero a una lista
    #"""
    if n==0:
        return [0]
    else:
        return pasa_a_lista(n//10)+[n%10]
#3
def largo(n):
    #"""
    #La funcion largo auxiliar de binario decimal

    #Parametros:
    #n: cualquier numero entero

    #Retorna:
    #cuenta el largo de un numero entero
    #"""
    if n<10:
        return 1
    else:
        return 1 + largo(n//10)
#4
def binario_decimal(numero,base=2):
    #"""
    #La funcion binario decimal auxiliar de la get llave

    #Parametros:
    #numero: cualquier numero entero

    #Retorna:
    #pasa un numero en base 2 osea notacion binaria a base decimal osea base 10
    #"""
    if numero<10:
        return numero
    else:
        return (numero//10**(largo(numero)-1))*base**(largo(numero)-1)+binario_decimal(numero%10**(largo(numero)-1),base)

#5
def binario_en_lista_a_numero_binario(lista,num=0,i=0):
    #"""
    #La funcion binario en lista a numero binario auxiliar de la get llave

    #Parametros:
    #lista: digitos de un numero binario en una lista como elementos de una lista

    #Retorna:
    #pasa los digitos de un numero binario en una lista a un numero binario
    #"""
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
    #"""
    #La funcion get llave

    #Parametros:
    #num: cualquier numero entre 1 y 255

    #Retorna:
    #da como resultado una llave especifica que se necesita para encriptar y desencriptar
    #"""
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

help(decimal_binario)
help(pasa_a_lista)
help(largo)
help(binario_decimal)
help(binario_en_lista_a_numero_binario)
help(get_llave)
       
#--------------------------------------------------------------------------------
#encriptacion del texto

#funciones auxiliares de la funcion principal encriptar

#1
def rotar(llave):
    #"""
    #La funcion rotar auxiliar de la de encriptar

    #Parametros:
    #llave: cualquier numero entero entre 1 y 255

    #Retorna:
    #retorna la rotacion de la lista segun el generador de la llave
    #"""
    return rotar_aux(llave, "abcdefghijklmnñopqrstuvwxyz")

def rotar_aux(llave, cinta2):
    #"""
    #La funcion rotar aux auxiliar de la funcion rotar

    #Parametros:
    #llave: cualquier numero entero entre 1 y 255
    #cinta2: parametro especifico

    #Retorna:
    #retrona la llamada recursiva de la funcion rotar
    #"""
    if 1<=llave<=255:
        if llave==1:
            return cinta2[26] + cinta2[0:26] 
        else:
            return rotar_aux(llave-1, cinta2[26] + cinta2[0:26])
    elif llave== 0:
        return cinta2
    else: 
        return "Introduzca un numero entre 1 y 255"
 
print(rotar(2))
#2
#funcion para reemplazar la letra "x" por la que corresponderia por en la cinta2
def reemplazar(letra, llave):
    #"""
    #La funcion reemplazar auxiliar de la de encriptar

    #Parametros:
    #letra: cualquier letra minuscula o mayuscula
    #llave: cualquier numero entero entre 1 y 255

    #Retorna:
    #retorna una letra en especifico segun segun la letra ingresada y segun la llave ingresada
    #"""
    cinta= "abcdefghijklmnñopqrstuvwxyz"
    cinta_M= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cinta2= rotar(llave)
    cinta2_M= cinta2.upper()

    if letra == " ":
        return letra
    elif letra == "\n":
        return letra
    if letra == "," or letra == "." or letra == "¿":
        return letra
    elif letra == " " or letra == "\n":
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

# funcion principal

#llave= int(input("Ingrese la llave: "))
#texto= input("Ingrese el texto a leer: ")
def encriptar(texto, llave):
    #"""
    #La funcion encriptar

    #Parametros:
    #texto: cualquier texto que el usuario introduzca
    #llave: cualquier numero entero entre 1 y 255

    #Retorna:
    #retorna el texto encriptado segun el texto introducido y segun la lave ingresada
    #"""
    if len(texto)==0:
        return " "
    else:
        if texto[0] ==" ":
            return " " + encriptar(texto[1:], get_llave(llave))
        else:
            return reemplazar(texto[0], llave) + encriptar(texto[1:], get_llave(llave))

help(rotar)
help(rotar_aux)
help(reemplazar)
help(encriptar)

#--------------------------------------------------------------------------------
#desencriptacion del texto

#funciones auxiliares de la funcion principal desencriptar

#1
#funcion para rotar el string
def rotarR(llave):
    #"""
    #La funcion rotar R auxiliar de desencriptacion

    #Parametros:
    #llave: cualquier numero entero entre 1 y 255

    #Retorna:
    #retorna la rotacion del string en la lista de abecedario
    #"""
    return rotarR_aux(llave, "abcdefghijklmnñopqrstuvwxyz")

def rotarR_aux(llave, cinta2):
    #"""
    #La funcion rotar R aux auxiliar de rotar R

    #Parametros:
    #llave: cualquier numero entero entre 1 y 255
    #cinta2: parametro especifico

    #Retorna:
    #retrona la llamada recursiva de la funcion rotar R
    #"""
    if 1<=llave<=255:
        if llave==1:
            return cinta2[1:27] + cinta2[0]
        else:
            return rotarR_aux(llave-1, cinta2[1:27] + cinta2[0])
    elif llave== 0:
        return cinta2
    else: 
        return "Introduzca un numero entre 1 y 255"

#2
#funcion para reemplazar una letra
def reemplazar_D(letra, llave):
    #"""
    #La funcion reemplazar D auxiliar de la de desencriptar

    #Parametros:
    #letra: cualquier letra minuscula o mayuscula
    #llave: cualquier numero entero entre 1 y 255

    #Retorna:
    #retorna una letra en especifico segun segun la letra ingresada y segun la llave ingresada
    #"""
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

# funcion principal

#llave= int(input("Ingrese la llave: "))
#texto= input("Ingrese el texto a leer: ")
def desencriptar(texto, llave):
    #"""
    #La funcion desencriptar

    #Parametros:
    #texto: cualquier texto que el usuario introduzca
    #llave: cualquier numero entero entre 1 y 255

    #Retorna:
    #retorna el texto desencriptado segun el texto introducido y segun la lave ingresada
    #"""
    if len(texto)==0:
        return ""
    else:
        if texto[0] == " ":
            return " " + desencriptar(texto[1:], get_llave(llave))
        else:
            return reemplazar_D(texto[0], llave) + desencriptar(texto[1:], get_llave(llave))

help(rotarR)
help(rotarR_aux)
help(reemplazar_D)
help(desencriptar)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Loop de la ventana
menu().mainloop()





