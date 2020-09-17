# Invocamos la libreria de tkinter
from tkinter import *
import os.path
# creamos la ventana
ventana = Tk()
ventana.geometry("600x400")

icono_ventana = os.path.abspath('./imagenes/rostro.ico')
if not os.path.isfile(icono_ventana):
    icono_ventana = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(icono_ventana)

# Para los menus
mi_menu = Menu(ventana)
ventana.config(
    menu=mi_menu
   
)

archivo = Menu(mi_menu)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abril archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir")

editar = Menu(mi_menu)
editar.add_command(label="Seleccionar")
editar.add_command(label="copiar")
editar.add_command(label="cortar")

mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_cascade(label="Editar", menu=editar)

selecciona = Menu(mi_menu)
selecciona.add_command(label="Expandir todo")
selecciona.add_command(label="Shrink Selection")
selecciona.add_command(label="Copy Line Up")

mi_menu.add_cascade(label="Seleccion", menu=selecciona)

ventana.mainloop()
