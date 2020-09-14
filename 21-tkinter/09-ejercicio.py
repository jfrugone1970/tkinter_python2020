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

#Funcion para convertir
def cfloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error","Introduce bien los datos")

    return result    


# Funciones para las operaciones
def sumar():
    resultado.set(cfloat(numero1.get()) + cfloat(numero2.get()))
    mostrarResultado()

def restar():
    resultado.set(cfloat(numero1.get())-cfloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(cfloat(numero1.get())*cfloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(cfloat(numero1.get())/cfloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resultado",f"el resultado de la operacion es {resultado.get()}")
    numero1.set("")
    numero2.set("")



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

campo_requerido = Entry(marco, textvariable=numero1, justify="center")
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

campo_requerido = Entry(marco, textvariable=numero2, justify="center")
campo_requerido.config(
    bg="green",
    fg="white",
    font=("Tahoma",10)
)
campo_requerido.pack(side=TOP,anchor=NW,padx=10,pady=10)

# Botones de operaciones
boton1 = Button(marco, text="Sumar",command=sumar)
boton1.config(
    width="10",
    height="5",
    bg="red",
    fg="yellow",
    font=("Tahoma",10)

)
boton1.pack(side=LEFT,anchor=SW,padx=10,pady=10,fill=X,expand=YES)

boton2 = Button(marco, text="Restar",command=restar)
boton2.config(
    width="10",
    height="5",
    bg="red",
    fg="yellow",
    font=("Tahoma",10)

)
boton2.pack(side=LEFT,anchor=SW,padx=10,pady=10,fill=X,expand=YES)

boton3 = Button(marco, text="Multiplicar", command=multiplicar)
boton3.config(
    width="10",
    height="5",
    bg="red",
    fg="yellow",
    font=("Tahoma",10)

)
boton3.pack(side=LEFT,anchor=SW,padx=10,pady=10,fill=X,expand=YES)

boton4 = Button(marco, text="Dividir", command=dividir)
boton4.config(
    width="10",
    height="5",
    bg="red",
    fg="yellow",
    font=("Tahoma",10)

)
boton4.pack(side=LEFT,anchor=SW,padx=10,pady=10,fill=X,expand=YES)



ventana.mainloop()
