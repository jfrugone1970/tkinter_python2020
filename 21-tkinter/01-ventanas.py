# Tkinter_
# Es un módulo para crear interfaz gráficas de usuario
from tkinter import *
# Importamos la libreria de la ruta para comprobar donde
# esta el archivo de imagen
import os.path
# crear la lventa razi
class Programa:

    def __init__(self, title, icon, icon_alt, size, resizable):
        self.title = title
        self.icon = icon
        self.icon_alt = icon_alt
        self.size = size
        self.resizable = resizable
  
    def cargar(self):

        ventana = Tk()

        self.ventana = ventana
        # Titulo de la ventana
        ventana.title(self.title)


        #Comprobar si existe el archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(self.icon):
            ruta_icono = os.path.abspath(self.icon_alt)


        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)
        #Cambio tamaño de la ventana
        ventana.geometry(self.size)

        #Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)

        else:
            ventana.resizable(0,0)   

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()
    

# Instanciar mi programa mediante la clase
programa = Programa('Curso de Master en Python con Victor Robles','./imagenes/07_linkedin.ico','./21-tkinter/imagenes/07_linkedin.ico','1350x500',FALSE)
programa.cargar()
programa.addTexto("Hola! Soy Jose Fernando Frugone Jaramillo")
programa.addTexto("soy Lcdo en Informatica")
programa.addTexto("graduado en la Universidad de Guayaquil")
programa.addTexto("Facultad de Filosofia")
programa.addTexto("tambien realice estudio de Programacion de Microcomputadoras")
programa.addTexto("En la ESPOL")
programa.addTexto("tengo conocimiento de algunos lenguajes como Java, Laravel, Visual Basic.NET")
programa.addTexto("Fox fox, Visual Fox Pro 9, Python y otras herramientas")
programa.mostrar()



