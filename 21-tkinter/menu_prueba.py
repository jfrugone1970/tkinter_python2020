from tkinter import *
from tkinter import messagebox
import os.path
# creamos la ventana
ventana = Tk()
ventana.geometry("600x400")

icono_ventana = os.path.abspath('./imagenes/rostro.ico')

if not os.path.isfile(icono_ventana):
    icono_ventana = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(icono_ventana)

ventana.title("Menus con colores | Lcdo Jose Fernando Frugone Jaramillo")

mi_menu = Menu(ventana)
ventana.config(
    menu=mi_menu,
    bg="green",
    bd=25

)

def rojo():
    ventana.config(
        menu=mi_menu,
        bg="red",
        bd=25
    )

def amarillo():
    ventana.config(
        menu=mi_menu,
        bg="yellow",
        bd=25
    )

def magenta():
    ventana.config(
        menu=mi_menu,
        bg="magenta",
        bd=25
    )

def verde():
    ventana.config(
        menu=mi_menu,
        bg="green",
        bd=25
    )

def acercaDe():
    messagebox.showinfo("Realizado por :","Lcdo Jose Fernando Frugone Jaramillo")                

colores = Menu(ventana, tearoff=0)
colores.add_command(label="Rojo", command=rojo)
colores.add_command(label="Amarillo", command=amarillo)
colores.add_command(label="Magenta", command=magenta)
colores.add_command(label="Verde", command=verde)
colores.add_command(label="Acerca de", command=acercaDe)

terminar = Menu(ventana, tearoff=0)
terminar.add_command(label="Salir", command=ventana.quit)

mi_menu.add_cascade(label="Colores", menu=colores)
mi_menu.add_cascade(label="Finalizar", menu=terminar)


ventana.mainloop()
