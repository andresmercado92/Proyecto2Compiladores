#Ventana Prueba
from tkinter import *
from Automata_impar import *
from Automata_par import *

def enviar():
    print("Enviar...")
    if OpcionRadioButton.get()==1:
        print("Seleccionaste AUTOMATA PAR")
        auto=Automata_par(expresionVar.get())
        auto.programa()
        
    elif OpcionRadioButton.get()==2:
        print("Seleccionaste AUTOMATA IMPAR")
        auto=Automata_impar(expresionVar.get())
        auto.programa()
        

ventana = Tk()
expresionVar = StringVar()
OpcionRadioButton = IntVar()

exp1 = StringVar()
exp2 = StringVar()
exp3 = StringVar()
exp4 = StringVar()
exp5 = StringVar()
exp6 = StringVar()
exp7 = StringVar()
exp8 = StringVar()
exp9 = StringVar()
exp10 = StringVar()

exp1.set("1")
exp2.set("2")
exp3.set("3")
exp4.set("4")
exp5.set("5")
exp6.set("6")
exp7.set("7")
exp8.set("8")
exp9.set("9")
exp10.set("10")


ventana.title("Proyecto 2 - Compiladores")
ventana.geometry("800x400")
etiqueta1 = Label(ventana, text= "Ingrese la cadena: ").place(x=80, y=80)
expresionTextBox = Entry(ventana, textvariable= expresionVar).place(x=190, y=80)
boton = Button(ventana, fg="Red", text="Ejecutar", command= enviar).place(x=180, y=200)
opcion1B = Radiobutton(ventana, text="Automata Par", value=1, variable = OpcionRadioButton).place(x=100, y= 120)
opcion2B = Radiobutton(ventana, text="Automata Impar", value=2, variable = OpcionRadioButton).place(x=210, y=120)
etiqueta2 = Label(ventana, text= "(c)2018 Hecho por Julian Rueda y Andres Mercado").place(x= 5, y= 380)


#------------------ Pila -----------------------------
pila1 = Entry(ventana, width= 5, state= "disabled", textvariable=exp1).place(x=400, y=20)
pila2 = Entry(ventana, width= 5, state= "disabled", textvariable=exp2).place(x=400, y=40)
pila3 = Entry(ventana, width= 5, state= "disabled", textvariable=exp3).place(x=400, y=60)
pila4 = Entry(ventana, width= 5, state= "disabled", textvariable=exp4).place(x=400, y=80)
pila5 = Entry(ventana, width= 5, state= "disabled", textvariable=exp5).place(x=400, y=100)
pila6 = Entry(ventana, width= 5, state= "disabled", textvariable=exp6).place(x=400, y=120)
pila7 = Entry(ventana, width= 5, state= "disabled", textvariable=exp7).place(x=400, y=140)
pila8 = Entry(ventana, width= 5, state= "disabled", textvariable=exp8).place(x=400, y=160)
pila9 = Entry(ventana, width= 5, state= "disabled", textvariable=exp9).place(x=400, y=180)
pila10 = Entry(ventana, width= 5, state= "disabled", textvariable=exp10).place(x=400, y=200)



ventana.mainloop()
