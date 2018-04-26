#Ventana Prueba
from tkinter import *


ventana = Tk()
ventana.title("Proyecto 2 - Compiladores")
ventana.geometry("400x400")
etiqueta1 = Label(ventana, text= "Ingrese la cadena: ").place(x=80, y=80)
expresion = Entry(ventana).place(x=190, y=80)
boton = Button(ventana, fg="Red", text="Ejecutar").place(x=180, y=200)
opcion1B = Radiobutton(ventana, text="Automata Par", value=1).place(x=100, y= 120)
opcion2B = Radiobutton(ventana, text="Automata Impar", value=2).place(x=210, y=120)
etiqueta2 = Label(ventana, text= "(c)2018 Hecho por Julian Rueda y Andres Mercado").place(x= 5, y= 380)
ventana.mainloop()

