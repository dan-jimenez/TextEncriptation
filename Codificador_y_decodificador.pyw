from tkinter import *
from tkinter.filedialog import askopenfilename

ventanaprincipal=Tk()
ventanaprincipal.title("Codificador y decodificador de texto")
ventanaprincipal.config(bg="gray")
ventanaprincipal.config(bd="30")
ventanaprincipal.resizable(False, False)
ventanaprincipal.geometry("400x400")
ventanaprincipal.config(relief="groove")
miframe=Frame(ventanaprincipal)
miframe.pack()
nombre=Label(miframe, text= "¿Qué desea hacer?", font=("Times New Roman", 18), bg="gray")
nombre.pack()






ventanaprincipal.mainloop()