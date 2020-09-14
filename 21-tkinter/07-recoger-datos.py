from tkinter import *
from PIL import Image, ImageTk
import os.path
# Se crea la ventana
ventana = Tk()
ventana.geometry("700x400")
ventana.title("Tkinter Recoger datos de un formulario")
# Icono para la ventana
icono_ventana = os.path.abspath('./imagenes/rostro.ico')

if not os.path.isfile('./imagenes/rostro.ico'):
    icono_ventana = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(icono_ventana)

texto = Label(ventana, text="Ingresa un texto :")
texto.config(
    bg="darkgrey",
    fg="blue",
    font=("Arial",10)
)
texto.pack(side=TOP, anchor=NW)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="cyan",
    bd=5,
    relief="raised"
)
marco.pack(side=RIGHT, anchor=NE)

dibujo = Image.open("./21-tkinter/imagenes/conejo.jpg")
render = ImageTk.PhotoImage(dibujo)

Label(marco, image=render).pack()

def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        texto.config(
            bg="green",
            fg="white"
        )

dato = StringVar()
resultado = StringVar()

campo = Entry(ventana, textvariable=dato)
campo.config(
    bg="yellow",
    fg="red",
    font=("Tahoma",10)
)
campo.pack(side=TOP, anchor=NW, padx=10, pady=10)

texto = Label(ventana, text="Datos Recogido :")
texto.config(
    bg="darkgrey",
    fg="blue",
    font=("Arial",10)
)
texto.pack(side=TOP, anchor=NW)

texto = Label(ventana, textvariable=resultado)
texto.config(
    width="80",
    height="5",
    bg="cyan",
    fg="red",
    font=("Tahoma",10)
)
texto.pack(side=TOP, anchor=W, padx=10, pady=10)

# Boton
boton = Button(ventana, text="Mostrar dato", command=getDato)
boton.config(
    width="10",
    height="5",
    bg="yellow",
    fg="red",
    font=("Tahoma",10)
)
boton.pack(side=LEFT, anchor=SW, padx=10, pady=10)


ventana.mainloop()
