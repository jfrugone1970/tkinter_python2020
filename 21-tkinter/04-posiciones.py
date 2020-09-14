# Importamos la libreria tkinter
from tkinter import *
import os.path
# Creamos la ventana raiz
ventana = Tk()
# Tamaño de la ventana
ventana.geometry("500x500")

icono_alt = os.path.abspath('./imagenes/rostro.ico')

# Para añadir icono en la ventana
if not os.path.isfile('./imagenes/rostro.ico'):
    icono_alt = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(icono_alt)

def caracteres(saludo):
    return f"Hola! {saludo}"

# Añadir texto a la ventana
texto = Label(ventana, text=caracteres(saludo="Bienvenido a mi programa"))
texto.config(
    fg="white",
    bg="black",
    padx=10,
    pady=20,
    font=("Tahoma", 15),
    cursor="arrow"
)
texto.pack(side=TOP, fill=X, expand=YES)

def pruebas(nombre):
    return f"Soy {nombre} "

texto = Label(ventana, text=pruebas(nombre="Lcdo. José Fernando Frugone Jaramillo"))
texto.config(
     fg="black",
     bg="orange",
     padx=10,
     pady=20,
     font=("Tahoma", 15),
     cursor="arrow"
)
texto.pack(side=TOP, fill=X, expand=YES)

def addTexto(curso):
    return f"{curso}"

texto = Label(ventana, text=addTexto(curso="Basico 1"))
texto.config(
    height=3,
    bg="green",
    padx=10,
    pady=20,
    font=("Arial", 18),
    cursor="spider"
)

texto.pack(side=LEFT, fill=X, expand=YES)

def addTexto1(curso):
    return f"{curso}"

texto = Label(ventana, text=addTexto1(curso="Basico 2"))
texto.config(
    height=3,
    bg="red",
    padx=10,
    pady=20,
    font=("Arial", 18),
    cursor="spider"
)

texto.pack(side=LEFT, fill=X, expand=YES)

def addTexto2(curso):
    return f"{curso}"

texto = Label(ventana, text=addTexto2(curso="Basico 3"))
texto.config(
    height=3,
    bg="yellow",
    padx=10,
    pady=20,
    font=("Arial", 18),
    cursor="spider"
)

texto.pack(side=LEFT, fill=X, expand=YES)

ventana.resizable(1,1)

ventana.mainloop()
