# importamos tkinter
from tkinter import *
# importamos mensajes para alertas
from tkinter import messagebox
import os.path
# para importar imagenes
from PIL import Image, ImageTk


ventana = Tk()
ventana.geometry("700x500")
ventana.title("Alertas en Tkinter | Lcdo José Fernando Frugone Jatamillo")
ventana.config(
    bd=70,
    bg="#ccc"
)

#icono de la ventana
icono_ventana = os.path.abspath('./imagenes/rostro.ico')

if not os.path.isfile('./imagenes/rostro.ico'):
    icono_ventana = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(icono_ventana)
# Marco para la Imagen
marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="cyan",
    bd=5,
    relief="raised"
)
marco.pack(side=RIGHT, anchor=NE)

dibujo = Image.open("./21-tkinter/imagenes/ardilla.jpg")
render = ImageTk.PhotoImage(dibujo)

def sacarAlerta():
    messagebox.showinfo("Alerta","Soy Lcdo. Jose Fernando Frugone Jaramillo")

def salir(nombre):
    resultado = messagebox.askquestion("Salir","¿Continuar con la ejecucion (S/N) :")

    if resultado !="yes":
        messagebox.showinfo("Adios!!!", f"Hasta pronto {nombre}")
        ventana.destroy()


Label(marco, image=render).pack()
boton = Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta)
boton.config(
    bg="green",
    fg="white",
    width=20,
    height=5,
    padx=5,
    pady=5
)
boton.pack(side=BOTTOM, anchor=SW)

boton = Button(ventana, text="Salir!!", command=lambda: salir("Lcdo Jose Fernando Frugone Jaramillo"))
boton.config(
    bg="magenta",
    fg="white",
    width=20,
    height=5,
    padx=5,
    pady=5
)
boton.pack(side=BOTTOM, anchor=SW)


ventana.mainloop()
