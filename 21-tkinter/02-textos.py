# Importamos la libreria tkinter
from tkinter import *
import os.path
import datetime
# Creamos la ventana raiz
ventana = Tk()
# Tamaño de la ventana
ventana.geometry("500x500")

icono_alt = os.path.abspath('./imagenes/rostro.ico')

# Para añadir icono en la ventana
if not os.path.isfile('./imagenes/rostro.ico'):
    icono_alt = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(icono_alt)

def caracteres(saludo, nombre):
    return f"Hola! {saludo} ¿como estas {nombre}"

# Añadir texto a la ventana
texto = Label(ventana, text=caracteres(saludo="Bienvenido a mi programa",nombre="Lcdo. Jose Fernando"))
texto.config(
    fg="green",
    bg="yellow",
    padx=20,
    pady=20,
    font=("Tahoma", 12),
    anchor=W,
    cursor="arrow"
)
texto.pack(side=TOP)

def pruebas(apellido, pais):
    return f"{apellido} veo que eres de {pais}"

texto = Label(ventana, text=pruebas(apellido="Frugone Jaramillo?",pais="Ecuador"))
texto.config(
     fg="green",
     bg="orange",
     padx=20,
     pady=20,
     font=("Tahoma", 15),
     justify=RIGHT,
     cursor="arrow"
)
texto.pack(side=TOP)

def addTexto(est_sup, universidad):
    return f"{est_sup} de la {universidad}"

texto = Label(ventana, text=addTexto(est_sup="Lcdo. en Informatica",universidad="Universidad de Guayaquil"))
texto.config(
    fg="red",
    bg="cyan",
    padx=20,
    pady=20,
    font=("Tahoma", 15),
    justify=CENTER,
    cursor="arrow"
)

texto.pack(side=TOP, fill=X, expand=YES)

def addText2(otros_est):
    return f"{otros_est}"

texto = Label(ventana, text=addText2(otros_est="Prog. de Microcomputadoras"))
texto.config(
    fg="blue",
    bg="yellow",
    padx=20,
    pady=20,
    font=("Tahoma",15),
    justify=CENTER,
    cursor="arrow"
)

texto.pack(side=TOP, fill=X, expand=YES)

def addTexto3(fecha):
    return f"{fecha}"

texto = Label(ventana, text=addTexto3(fecha=datetime.datetime.now()))
texto.config(
    fg="green",
    bg="red",
    padx=20,
    pady=20,
    font=("Tahoma",15),
    justify=CENTER,
    anchor=SW,
    cursor="arrow"
)

texto.pack(side=TOP)

ventana.resizable(1,1)

ventana.mainloop()
