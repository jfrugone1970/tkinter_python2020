# importamos tkinter
from tkinter import *
# para importar el logo en la ventana
import os.path

ventanas = Tk()
ventanas.title("Marcos | Curso de Master en Python")
ventanas.geometry("700x700")

ruta_icono = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

if not os.path.abspath('./imagenes/rostro.ico'):
    ruta_icono = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventanas.iconbitmap(ruta_icono)
# 1er Marco Padre
marco_padre = Frame(ventanas, width=250, height=250)
marco_padre.config(
    bg="lightblue",
    bd=5,
    relief="raised"
)
marco_padre.pack(side=TOP, anchor=N,fill=X,expand=YES)

# Elemento de cuadro 1 del 1er Marco padre
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=12,
    relief="raised"
)
marco.pack(side=LEFT, anchor=NW)
marco.pack_propagate(False)
# Centrado de texto
texto = Label(marco, text="1er. marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial",20),
    height=10,
    width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(side=BOTTOM, anchor=CENTER)


# Elemento del cuadro 2 del 1er Marco padre
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="orange",
    bd=12,
    relief="raised"
)
marco.pack(side=RIGHT, anchor=NE)
marco.pack_propagate(False)

texto = Label(marco, text="2do. marco")
# Centrar el texto
texto.config(
    bg="red",
    fg="white",
    font=("Arial",20),
    height=10,
    width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(side=BOTTOM, anchor=CENTER)

# 2do marco Padre
marco_padre = Frame(ventanas, width=250, height=250)
marco_padre.config(
    bg="cyan",
    bd=5,
    relief="raised"
)
marco_padre.pack(side=TOP, anchor=CENTER, fill=X, expand=YES)

# Elemento cuadro 1 del 2do marco padre
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="blue",
    bd=12,
    relief="raised"
)
marco.pack(side=LEFT,anchor=W)
marco.pack_propagate(False)

texto = Label(marco, text="3er. marco")
# Centrar el texto
texto.config(
    bg="red",
    fg="white",
    font=("Arial",20),
    height=10,
    width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(side=BOTTOM, anchor=CENTER)

# Elemento cuadro 2 del 2do marco padre
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="brown",
    bd=12,
    relief="raised"
)
marco.pack(side=RIGHT,anchor=E)
marco.pack_propagate(False)

texto = Label(marco, text="4to. marco")
# centrar el texto
texto.config(
    bg="red",
    fg="white",
    font=("Arial",20),
    height=10,
    width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(side=BOTTOM, anchor=CENTER)

# 3er Marco Padre
marco_padre = Frame(ventanas, width=250, height=250)
marco_padre.config(
    bg="lightblue",
    bd=5,
    relief="raised"
)
marco_padre.pack(side=TOP, anchor=S,fill=X,expand=YES)

# 1er cuadro del 3er marco padre
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=12,
    relief="raised"
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="5to. marco")
# centrar el texto
texto.config(
    bg="red",
    fg="white",
    font=("Arial",20),
    height=10,
    width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(side=BOTTOM,anchor=CENTER)
# 2do cuadro del 3er marco padre
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=12,
    relief="raised"
)
marco.pack(side=RIGHT, anchor=SE)
marco.pack_propagate(False)

texto = Label(marco, text="6to. marco")
# centrar el texto
texto.config(
    bg="red",
    fg="white",
    font=("Arial",20),
    height=10,
    width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack(side=BOTTOM,anchor=CENTER)
ventanas.mainloop()
