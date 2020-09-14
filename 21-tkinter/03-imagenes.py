# Importamos tkinter
from tkinter import *
# Cargamos el modulo de Imagenes Pillow Python
from PIL import Image, ImageTk
# Creamos la ventana raiz
ventana = Tk()
ventana.title("Imagenes | Curso de master en Python")
ventana.geometry("700x500")

Label(ventana, text="Hola!!, Soy Lcdo. José Fernando Frugone Jaramillo").pack(anchor=CENTER)

dibujo = Image.open("./21-tkinter/imagenes/leon.jpg")
render = ImageTk.PhotoImage(dibujo)

Label(ventana, image=render).pack(anchor=CENTER)

ventana.mainloop()
