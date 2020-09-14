# Programa para crear formularios en tkinter
from tkinter import *
# ventana del formulario
import os.path
ventana = Tk()
# dimensiones de la ventana
ventana.geometry("700x500")
# icono
icono_ventana = os.path.abspath('./imagenes/rostro.ico')

if not os.path.isfile('./imagenes/rostro.ico'):
    icono_ventana = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(icono_ventana)
ventana.title("Formularios en tkinter | Lcdo Jose Frugone")

# texto encabezado
encabezado = Label(ventana, text="Formulario en Tkinter | Lcdo Jose Frugone")
encabezado.config(
    fg="white",
    bg="darkgrey",
    font=("Open Sans",18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=6, sticky=N)

# Label para el campo (Nombre)
etiqueta = Label(ventana, text="Nombre")
etiqueta.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal", bg="yellow",fg="red", font=("Tahoma",10))

# Label para el campo (Apellido)
etiqueta = Label(ventana, text="Apellidos")
etiqueta.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal", bg="yellow",fg="red", font=("Tahoma",10))

# Label para el campo (Descripcion)
etiqueta = Label(ventana, text="descripcion")
etiqueta.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Campo de texto para ingresar datos grandes
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, sticky=W)
campo_grande.config(
     width="15",
     height="5",
     bg="cyan",
     fg="red",
     font=("Tahoma",10),
     padx=5,
     pady=5
)
# Para crear botones
Label(ventana).grid(row=8, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=9, column=1, sticky=W)
boton.config(
    padx=10,
    pady=10,
    bg="green",
    fg="white"
)    

ventana.mainloop()



