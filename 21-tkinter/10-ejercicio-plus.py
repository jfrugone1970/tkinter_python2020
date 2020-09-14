"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones
- debe mostrar los resultados en una alerta
"""
from tkinter import *
from tkinter import messagebox
import os.path

ventana = Tk()
ventana.geometry("600x400")

ventana.title("Calculadora | Lcdo Jose Fernando Frugone Jaramillo")

# Icono en la ventana
icono_ventana = os.path.abspath('./imagenes/rostro.ico')

if not os.path.isfile(icono_ventana):
    icono_ventana = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(icono_ventana)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()



# Clase Calculadora
class Calculadora:

    # constructor

    def __init__(self, alertas):

        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas
    
    #Funcion para convertir
    def cfloat(self, numero):
        try:
            self.result = float(numero)
        except:
            self.result = 0
            self.alertas.messagebox.showerror("Error","Introduce bien los datos")

        return self.result        


    # Funciones para las operaciones
    def sumar(self):
        self.resultado.set(self.cfloat(self.numero1.get()) + self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(self.cfloat(self.numero1.get())-self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.cfloat(self.numero1.get())*self.cfloat(self.numero2.get()))
        self.mostrarResultado()
        
    def dividir(self):
        self.resultado.set(self.cfloat(self.numero1.get())/self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado",f"el resultado de la operacion es {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


# Instanciar la clase calculadora
calculadora = Calculadora(messagebox)


# Marco para la ventana
marco = Frame(ventana)
marco.config(
    width="400",
    height="400",
    bd=5,
    bg="yellow",
    padx=5,
    pady=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

# Para el Numero 1

texto = Label(marco, text="Primer Numero")
texto.config(
    bg="darkgray",
    fg="red",
    font=("Tahoma",10)
)

texto.pack(side=TOP,anchor=NW,padx=10,pady=10)

campo_requerido = Entry(marco, textvariable=calculadora.numero1, justify="center")
campo_requerido.config(
    bg="green",
    fg="white",
    font=("Tahoma",10)
)
campo_requerido.pack(side=TOP,anchor=NW,padx=10,pady=10)

# Para el Numero 2

texto = Label(marco, text="Segundo Numero")
texto.config(
    bg="darkgray",
    fg="red",
    font=("Tahoma",10)
)

texto.pack(side=TOP,anchor=NW,padx=10,pady=10)

campo_requerido = Entry(marco, textvariable=calculadora.numero2, justify="center")
campo_requerido.config(
    bg="green",
    fg="white",
    font=("Tahoma",10)
)
campo_requerido.pack(side=TOP,anchor=NW,padx=10,pady=10)

# Botones de operaciones
boton1 = Button(marco, text="Sumar",command=calculadora.sumar)
boton1.config(
    width="10",
    height="5",
    bg="red",
    fg="yellow",
    font=("Tahoma",10)

)
boton1.pack(side=LEFT,anchor=SW,padx=10,pady=10,fill=X,expand=YES)

boton2 = Button(marco, text="Restar",command=calculadora.restar)
boton2.config(
    width="10",
    height="5",
    bg="red",
    fg="yellow",
    font=("Tahoma",10)

)
boton2.pack(side=LEFT,anchor=SW,padx=10,pady=10,fill=X,expand=YES)

boton3 = Button(marco, text="Multiplicar", command=calculadora.multiplicar)
boton3.config(
    width="10",
    height="5",
    bg="red",
    fg="yellow",
    font=("Tahoma",10)

)
boton3.pack(side=LEFT,anchor=SW,padx=10,pady=10,fill=X,expand=YES)

boton4 = Button(marco, text="Dividir", command=calculadora.dividir)
boton4.config(
    width="10",
    height="5",
    bg="red",
    fg="yellow",
    font=("Tahoma",10)

)
boton4.pack(side=LEFT,anchor=SW,padx=10,pady=10,fill=X,expand=YES)



ventana.mainloop()
